import asyncio
import json
import time
import socket
import statistics
from typing import List, Optional, Tuple
import aiohttp
from src.config import CORE_DIR, XRAY_FALLBACK_PORT_START, TEST_TIMEOUT, TEST_URL
from src.models.base import BaseVPNConfig
from src.services.xray_manager import get_xray_binary_path
from src.services.blocklist import is_whitelist_config
from src.services.history import HistoryManager
from src.services.whitelist_db import is_ip_whitelisted, is_sni_whitelisted
from src.utils import logger

# Phase 1 & 2 & 3 endpoints
PING_ENDPOINTS = [
    "https://cp.cloudflare.com/generate_204",
    "https://www.gstatic.com/generate_204",
    "https://www.google.com/generate_204",
]
URL_RU_CHECK = "http://ya.ru"
URL_SPEED_TEST = "https://speed.cloudflare.com/__down?bytes=1000000"

VPS_PUBLIC_IP = None

async def get_direct_ip() -> str | None:
    global VPS_PUBLIC_IP
    if VPS_PUBLIC_IP: return VPS_PUBLIC_IP
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.ipify.org?format=json", timeout=10) as resp:
                data = await resp.json()
                VPS_PUBLIC_IP = data.get("ip")
                return VPS_PUBLIC_IP
    except Exception:
        return None

async def get_exit_ip(port: int, timeout: float = 7.0) -> str | None:
    from aiohttp_socks import ProxyConnector
    connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
    timeout_config = aiohttp.ClientTimeout(total=timeout)
    try:
        async with aiohttp.ClientSession(connector=connector, timeout=timeout_config) as session:
            async with session.get("https://api.ipify.org?format=json") as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("ip")
    except Exception:
        return None
    finally:
        await connector.close()
    return None

# Whitelist control endpoints
WHITELIST_TEST_URLS = (
    "https://www.gstatic.com/generate_204",
    "https://cp.cloudflare.com/generate_204",
)
EXTERNAL_CONTROL_URLS = (
    "https://www.youtube.com/generate_204",
    "https://github.com/",
)


async def tcp_ping_best(host: str, port: int, tries: int = 2, timeout: float = 1.5) -> Optional[float]:
    best = None
    for _ in range(tries):
        try:
            start_time = time.perf_counter()
            _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=timeout)
            writer.close()
            await writer.wait_closed()
            rtt = (time.perf_counter() - start_time) * 1000.0
            best = rtt if best is None else min(best, rtt)
            if best < 80:
                break
        except Exception:
            pass
    return best


async def measure_entry_latency(host: str, port: int, attempts: int = 5, timeout: float = 3.0) -> tuple[Optional[float], float, Optional[float]]:
    latencies: list[float] = []
    for _ in range(attempts):
        started_at = time.perf_counter()
        try:
            _, writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=timeout,
            )
            latency = (time.perf_counter() - started_at) * 1000
            latencies.append(latency)
            writer.close()
            await writer.wait_closed()
        except (asyncio.TimeoutError, ConnectionError, OSError):
            pass
        await asyncio.sleep(0.2)
        
    success_rate = len(latencies) / attempts
    if not latencies:
        return None, success_rate, None
        
    median_latency = statistics.median(latencies)
    deviations = [abs(value - median_latency) for value in latencies]
    jitter = statistics.median(deviations)
    return round(median_latency, 2), round(success_rate, 3), round(jitter, 2)



async def wait_port(port: int, deadline: float = 10.0) -> bool:
    end = time.monotonic() + deadline
    while time.monotonic() < end:
        if await tcp_ping("127.0.0.1", port, timeout=0.5) is not None:
            return True
        await asyncio.sleep(0.1)
    return False


async def pre_filter_configs(configs: List[BaseVPNConfig], blocked_ips: set, history_manager, concurrency: int = 200) -> List[BaseVPNConfig]:
    logger.info(f"[Validator] Pre-filtering {len(configs)} configs (Syntax -> DNS -> TCP)...")
    import ipaddress
    from src.config import DATA_DIR
    REJECT_DIR = DATA_DIR / "rejected"
    REJECT_DIR.mkdir(parents=True, exist_ok=True)
    
    rejected = {
        "invalid_syntax": [],
        "private_ip": [],
        "dns_failed": [],
        "tcp_failed": []
    }
    
    def add_rejected(reason: str, cfg: BaseVPNConfig):
        rejected[reason].append(cfg.raw_link)
        history_manager.update_record(cfg.get_fingerprint(), success=False, failure_reason=reason)

    alive = []
    sem = asyncio.Semaphore(concurrency)
    loop = asyncio.get_running_loop()
    
    dns_cache = {}
    seen_endpoints = set()
    
    async def check(cfg):
        # 1. Syntax check
        if cfg.port <= 0 or cfg.port > 65535:
            add_rejected("invalid_syntax", cfg)
            return
            
        fingerprint = cfg.get_fingerprint()
        if fingerprint in seen_endpoints:
            return
        seen_endpoints.add(fingerprint)
            
        # 2. DNS and Private IP check
        resolved_ips = []
        if cfg.host in dns_cache:
            resolved_ips = dns_cache[cfg.host]
        else:
            try:
                ip_obj = ipaddress.ip_address(cfg.host)
                if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_link_local:
                    add_rejected("private_ip", cfg)
                    return
                resolved_ips = [cfg.host]
            except ValueError:
                try:
                    infos = await asyncio.wait_for(loop.getaddrinfo(cfg.host, cfg.port, proto=socket.IPPROTO_TCP), timeout=2.0)
                    if not infos:
                        add_rejected("dns_failed", cfg)
                        return
                    for info in infos:
                        candidate = info[4][0]
                        try:
                            ip_obj = ipaddress.ip_address(candidate)
                        except ValueError:
                            continue
                        if (
                            ip_obj.is_private
                            or ip_obj.is_loopback
                            or ip_obj.is_reserved
                            or ip_obj.is_link_local
                            or ip_obj.is_multicast
                            or ip_obj.is_unspecified
                        ):
                            continue
                        if candidate not in resolved_ips:
                            resolved_ips.append(candidate)
                    
                    if not resolved_ips:
                        add_rejected("private_ip", cfg)
                        return
                        
                    dns_cache[cfg.host] = resolved_ips
                except Exception:
                    add_rejected("dns_failed", cfg)
                    return

        # 3. TCP Pre-check
        best_result = None
        async with sem:
            for candidate_ip in resolved_ips[:2]:
                rtt = await tcp_ping_best(candidate_ip, cfg.port, tries=2, timeout=1.5)
                if rtt is not None:
                    if best_result is None or rtt < best_result[1]:
                        best_result = (candidate_ip, rtt)
                        if rtt < 80:
                            break

        if best_result is None:
            add_rejected("tcp_failed", cfg)
            return
            
        ip, rtt = best_result
        cfg.tcp_rtt_ms = round(rtt, 2)
        
        cfg.is_ip_whitelisted = is_ip_whitelisted(ip)
        cfg.is_sni_whitelisted = is_sni_whitelisted(cfg.sni)
        
        sec = cfg.security.lower() if cfg.security else ""
        cfg.is_reality = (cfg.protocol == "vless" and "reality" in sec) or ("security=reality" in cfg.raw_link.lower())
        
        whitelist_candidate = is_whitelist_config(cfg.raw_link, cfg.host, cfg.port, ip, blocked_ips)
        if whitelist_candidate:
            entry_latency, entry_success, entry_jitter = await measure_entry_latency(cfg.host, cfg.port)
            cfg.entry_latency_ms = entry_latency
            cfg.entry_success_rate = entry_success
            
            if entry_latency is None or entry_success < 0.80 or entry_latency > 1000:
                # Reject candidate if it fails the multi-connect entry ping
                add_rejected("tcp_failed", cfg)
                return
            cfg.whitelist_candidate = True
        else:
            cfg.whitelist_candidate = False
            
        alive.append(cfg)
                
    chunk_size = 5000
    for i in range(0, len(configs), chunk_size):
        chunk = configs[i:i+chunk_size]
        await asyncio.gather(*(check(c) for c in chunk))
    
    # Save rejections
    for reason, links in rejected.items():
        if links:
            with open(REJECT_DIR / f"{reason}.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(links))
        logger.info(f"[Validator] Rejected - {reason}: {len(links)}")
        
    logger.info(f"[Validator] Pre-filter completed. {len(alive)} nodes have open ports.")
    return alive


async def check_proxy_phase1(port: int, timeout: float) -> Tuple[bool, bool, bool]:
    """Phase 1: Fast functional test. Returns (is_alive, ru_reachable, exit_ip_verified)."""
    try:
        from aiohttp_socks import ProxyConnector
        connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
        
        is_alive = False
        ru_reachable = False
        exit_ip_verified = False
        
        async with aiohttp.ClientSession(connector=connector) as session:
            # 1. Check 204
            successful_endpoints = 0
            for url in PING_ENDPOINTS:
                try:
                    async with session.get(url, timeout=timeout) as resp:
                        if resp.status in (200, 204):
                            successful_endpoints += 1
                except Exception:
                    pass
            
            is_alive = successful_endpoints >= 2
                
            # 2. Check RU
            if is_alive:
                try:
                    async with session.head(URL_RU_CHECK, timeout=timeout) as resp:
                        if resp.status < 500:
                            ru_reachable = True
                except Exception:
                    pass
                    
        if is_alive:
            vps_ip = await get_direct_ip()
            exit_ip = await get_exit_ip(port, timeout=timeout)
            if exit_ip is not None and exit_ip != vps_ip:
                exit_ip_verified = True
                
        return is_alive, ru_reachable, exit_ip_verified
    except Exception:
        pass
    finally:
        try:
            await connector.close()
        except:
            pass
    return False, False, False


async def single_proxy_request(port: int, url: str, timeout: float) -> Optional[float]:
    from aiohttp_socks import ProxyConnector
    connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
    timeout_config = aiohttp.ClientTimeout(
        total=timeout,
        connect=min(timeout, 4.0),
        sock_connect=min(timeout, 4.0),
        sock_read=timeout,
    )
    started_at = time.perf_counter()
    try:
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout_config,
        ) as session:
            async with session.get(
                url,
                allow_redirects=False,
                headers={
                    "Connection": "close",
                    "Cache-Control": "no-cache",
                },
            ) as response:
                await response.read()
                if response.status in {200, 204, 301, 302, 303, 307, 308, 400, 403}:
                    return (time.perf_counter() - started_at) * 1000
    except (asyncio.TimeoutError, aiohttp.ClientError, OSError):
        pass
    finally:
        await connector.close()
    return None

async def check_whitelist_proxy(
    port: int,
    attempts: int = 7,
    warmup: int = 1,
    timeout: float = 8.0,
) -> tuple[Optional[float], float, Optional[float], Optional[float], bool]:
    """
    Whitelist deep-check via cold-start HTTP requests through the Xray SOCKS proxy.
    - warmup: 1 discarded request (JIT/TLS handshake warm-up)
    - attempts: measured samples (default 7)
    - Alternates between WHITELIST_TEST_URLS (cdn endpoints)
    - External control check: 2 blocked-in-RU targets
    Returns (median_ms, success_rate, jitter_mad_ms, p95_ms, external_reachable)
    """
    latencies: list[float] = []
    external_successes = 0

    # Warmup: 1 cold-start request, result discarded
    for _ in range(warmup):
        await single_proxy_request(port, WHITELIST_TEST_URLS[0], timeout)
        await asyncio.sleep(0.15)

    # Measured requests
    for i in range(attempts):
        url = WHITELIST_TEST_URLS[i % len(WHITELIST_TEST_URLS)]
        latency = await single_proxy_request(port, url, timeout)
        if latency is not None:
            latencies.append(latency)
        await asyncio.sleep(0.20)

    # External control: check access to YouTube/GitHub (blocked in RU without whitelist)
    for url in EXTERNAL_CONTROL_URLS:
        latency = await single_proxy_request(port, url, timeout)
        if latency is not None:
            external_successes += 1

    success_rate = len(latencies) / attempts
    external_reachable = external_successes > 0

    if not latencies:
        return None, success_rate, None, None, False

    # Trim single worst outlier if sample is large enough
    sorted_latencies = sorted(latencies)
    trimmed = sorted_latencies[:-1] if len(sorted_latencies) >= 5 else sorted_latencies

    median_latency = statistics.median(trimmed)

    # Jitter via MAD (robust vs outliers)
    deviations = [abs(v - median_latency) for v in trimmed]
    mad = statistics.median(deviations)
    jitter = round(mad * 1.4826, 2)

    # p95 from the full (non-trimmed) array for honest tail estimation
    p95_index = max(0, int(0.95 * (len(sorted_latencies) - 1)))
    p95_latency = sorted_latencies[p95_index]

    return round(median_latency, 2), round(success_rate, 3), jitter, round(p95_latency, 2), external_reachable


async def check_proxy_phase2(
    port: int,
    timeout: float,
    attempts: int = 8,
    warmup_attempts: int = 1,
) -> Tuple[Optional[float], float, Optional[float], Optional[float], Optional[float], bool]:
    """Phase 2: Accurate ping and DPI check. Returns (median_latency, success_rate, jitter, p90_latency, proxy_latency_ms, dpi_bypassed)."""
    from src.config import PING_ENDPOINTS
    try:
        from aiohttp_socks import ProxyConnector

        connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")

        raw_rtts: list[float] = []
        ttfb_rtts: list[float] = []
        errors = 0
        total_attempts = warmup_attempts + attempts

        timeout_config = aiohttp.ClientTimeout(
            total=timeout,
            connect=min(timeout, 4.0),
            sock_connect=min(timeout, 4.0),
            sock_read=timeout,
        )

        async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout_config,
        ) as session:
            for attempt_idx in range(total_attempts):
                is_warmup = attempt_idx < warmup_attempts
                started_at = time.perf_counter()
                test_url = PING_ENDPOINTS[attempt_idx % len(PING_ENDPOINTS)]

                ok = False
                ttfb = None
                try:
                    async with session.get(
                        test_url,
                        headers={"Connection": "close", "Cache-Control": "no-cache"},
                    ) as response:
                        # Capture TTFB on first byte
                        await response.content.read(1)
                        ttfb = (time.perf_counter() - started_at) * 1000
                        await response.read()
                        if response.status in {200, 204}:
                            ok = True

                except (asyncio.TimeoutError, aiohttp.ClientError, OSError):
                    pass

                if not is_warmup:
                    if ok:
                        rtt = (time.perf_counter() - started_at) * 1000
                        raw_rtts.append(rtt)
                        if ttfb is not None:
                            ttfb_rtts.append(ttfb)
                    else:
                        errors += 1

                await asyncio.sleep(0.15)

            # --- Metrics ---
            if not raw_rtts:
                return None, 0.0, None, None, None, False

            success_rate = len(raw_rtts) / attempts

            # Trim single worst outlier if we have enough samples
            rtts_sorted = sorted(raw_rtts)
            trimmed = rtts_sorted[:-1] if len(rtts_sorted) >= 5 else rtts_sorted

            # p50 from trimmed, p90 from full to preserve tail info
            p50 = trimmed[len(trimmed) // 2]
            p90_idx = max(0, int(0.90 * (len(rtts_sorted) - 1)))
            p90 = rtts_sorted[p90_idx]

            # TTFB median (proxy latency / connection overhead)
            ttfb_sorted = sorted(ttfb_rtts)
            proxy_latency = ttfb_sorted[len(ttfb_sorted) // 2] if ttfb_sorted else p50

            # Jitter via Median Absolute Deviation (robust, ignores outliers)
            med = statistics.median(trimmed)
            mad = statistics.median([abs(v - med) for v in trimmed])
            jitter = mad * 1.4826  # scale factor: makes MAD comparable to stdev for Gaussian

            # DPI bypass check via YouTube (2 tries, 3s timeout each)
            dpi_bypassed = False
            if success_rate > 0:
                for _ in range(2):
                    try:
                        async with session.get(
                            "https://www.youtube.com/generate_204",
                            allow_redirects=False,
                            headers={"Connection": "close"},
                            timeout=aiohttp.ClientTimeout(total=3.0),
                        ) as response:
                            if response.status in {200, 204, 301, 302, 303, 307, 308, 400, 403}:
                                dpi_bypassed = True
                                break
                    except (asyncio.TimeoutError, aiohttp.ClientError, OSError):
                        pass

            return (
                round(p50, 2),
                round(success_rate, 3),
                round(jitter, 2),
                round(p90, 2),
                round(proxy_latency, 2),
                dpi_bypassed,
            )

    except Exception as error:
        logger.debug(f"[Validator] Phase 2 error on local port {port}: {error}")
        return None, 0.0, None, None, None, False
    finally:
        try:
            await connector.close()
        except:
            pass


async def check_proxy_speed(port: int, timeout: float) -> Optional[float]:
    """Phase 3: Download speed test. Returns MB/s."""
    try:
        from aiohttp_socks import ProxyConnector
        connector = ProxyConnector.from_url(f"socks5://127.0.0.1:{port}")
        
        start = time.perf_counter()
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(URL_SPEED_TEST, timeout=timeout) as resp:
                if resp.status == 200:
                    data = await resp.read()
                    elapsed = time.perf_counter() - start
                    if elapsed > 0:
                        megabytes_per_second = len(data) / elapsed / (1024 * 1024)
                        megabits_per_second = megabytes_per_second * 8
                        return round(megabits_per_second, 2)
    except Exception:
        pass
    finally:
        try:
            await connector.close()
        except:
            pass
    return None


async def wait_all_ports(start_port: int, count: int, deadline: float = 15.0) -> bool:
    async def check_one(port):
        return await tcp_ping_best("127.0.0.1", port, tries=1, timeout=0.5) is not None

    end = time.monotonic() + deadline
    while time.monotonic() < end:
        results = await asyncio.gather(*[check_one(p) for p in range(start_port, start_port + count)])
        if all(results):
            return True
        await asyncio.sleep(0.2)
    return False

async def start_xray_batch(configs: List[BaseVPNConfig], batch_idx: int) -> Tuple[Optional[asyncio.subprocess.Process], str]:
    if not configs:
        return None, ""
        
    inbounds = []
    outbounds = []
    rules = []
    
    for i, cfg in enumerate(configs):
        local_port = XRAY_FALLBACK_PORT_START + i
        in_tag = f"in_{i}"
        out_tag = f"out_{i}"
        
        inbounds.append({
            "port": local_port,
            "listen": "127.0.0.1",
            "protocol": "socks",
            "tag": in_tag,
            "settings": {"udp": False}
        })
        
        try:
            out_conf = cfg.generate_xray_outbound()
            net = out_conf.get("streamSettings", {}).get("network", "")
            if net and net not in ["tcp", "kcp", "ws", "http", "domainsocket", "quic", "grpc", "httpupgrade"]:
                continue
            out_conf["tag"] = out_tag
            outbounds.append(out_conf)
            rules.append({
                "type": "field",
                "inboundTag": [in_tag],
                "outboundTag": out_tag
            })
        except:
            continue

    xray_conf = {
        "log": {"loglevel": "none"},
        "inbounds": inbounds,
        "outbounds": outbounds,
        "routing": {"rules": rules}
    }
    
    conf_path = CORE_DIR / f"temp_batch_{batch_idx}.json"
    with open(conf_path, "w", encoding="utf-8") as f:
        json.dump(xray_conf, f)

    bin_path = get_xray_binary_path()
    process = await asyncio.create_subprocess_exec(
        str(bin_path), "-c", str(conf_path),
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.PIPE
    )
    
    ready = await wait_all_ports(XRAY_FALLBACK_PORT_START, len(configs), deadline=15.0)
    
    if not ready:
        logger.error(f"[Validator] Xray batch {batch_idx} failed to bind ports.")
        try:
            if process.returncode is None:
                process.terminate()
        except:
            pass
        return None, str(conf_path)

    return process, str(conf_path)


async def cleanup_xray(process: Optional[asyncio.subprocess.Process], conf_path: str):
    if process:
        try:
            if process.returncode is None:
                process.terminate()
                await process.wait()
        except Exception:
            pass
    import os
    try:
        if os.path.exists(conf_path):
            os.remove(conf_path)
    except Exception:
        pass


async def run_phase1(configs: List[BaseVPNConfig], batch_idx: int) -> List[BaseVPNConfig]:
    process, conf_path = await start_xray_batch(configs, batch_idx)
    if not process:
        return []

    working = []
    sem = asyncio.Semaphore(40)
    
    async def check(i, cfg):
        async with sem:
            local_port = XRAY_FALLBACK_PORT_START + i
            is_alive, ru_reachable, exit_ip_verified = await check_proxy_phase1(local_port, TEST_TIMEOUT)
            if is_alive:
                cfg.ru_reachable = ru_reachable
                cfg.exit_ip_verified = exit_ip_verified
                working.append(cfg)
            else:
                cfg.exit_ip_verified = False

    await asyncio.gather(*(check(i, cfg) for i, cfg in enumerate(configs)))
    await cleanup_xray(process, conf_path)
    return working


async def run_phase2(configs: List[BaseVPNConfig]) -> List[BaseVPNConfig]:
    from src.config import PING_ATTEMPTS, PING_WARMUP_ATTEMPTS, MIN_SUCCESS_RATE, MAX_LATENCY_HARD_MS, MAX_JITTER_MS, MAX_LATENCY_P90_MS
    process, conf_path = await start_xray_batch(configs, 999) # special batch id for phase 2
    if not process:
        return []

    working = []
    sem = asyncio.Semaphore(15) # low concurrency for precise ping
    
    async def check(i, cfg):
        async with sem:
            local_port = XRAY_FALLBACK_PORT_START + i
            (
                latency,
                success_rate,
                jitter,
                p90_latency,
                proxy_latency,
                dpi_bypassed,
            ) = await check_proxy_phase2(
                local_port,
                TEST_TIMEOUT,
                attempts=PING_ATTEMPTS,
                warmup_attempts=PING_WARMUP_ATTEMPTS
            )
            
            borderline = (
                latency is None
                or success_rate < 0.875
                or jitter is None
                or jitter > 100
                or p90_latency is None
                or p90_latency > 1000
            )
            if borderline:
                await asyncio.sleep(1.0)
                retry_res = await check_proxy_phase2(
                    local_port,
                    10.0,
                    attempts=6,
                    warmup_attempts=1
                )
                if retry_res[0] is not None:
                    success_rate = (success_rate + retry_res[1]) / 2
                    latency = retry_res[0] if latency is None else (latency + retry_res[0]) / 2
                    jitter = retry_res[2] if jitter is None else (jitter + retry_res[2]) / 2
                    p90_latency = retry_res[3] if p90_latency is None else (p90_latency + retry_res[3]) / 2
                    proxy_latency = retry_res[4]
                    dpi_bypassed = dpi_bypassed or retry_res[5]

            if latency is None or jitter is None or p90_latency is None:
                return

            if success_rate < MIN_SUCCESS_RATE:
                return

            if latency > MAX_LATENCY_HARD_MS:
                return

            if p90_latency > MAX_LATENCY_P90_MS:
                return

            if jitter > MAX_JITTER_MS:
                return

            cfg.latency_ms = latency
            cfg.success_rate = success_rate
            cfg.dpi_bypassed = dpi_bypassed
            cfg.jitter_std_ms = jitter
            cfg.latency_p90_ms = p90_latency
            cfg.proxy_latency_ms = proxy_latency
            
            if getattr(cfg, "whitelist_candidate", False):
                (
                    wl_latency,
                    wl_success_rate,
                    wl_jitter,
                    wl_p95_latency,
                    wl_external_reachable,
                ) = await check_whitelist_proxy(
                    local_port,
                    attempts=7,
                    timeout=8.0,
                )
                
                if wl_latency is not None and wl_jitter is not None:
                    cfg.whitelist_latency_ms = wl_latency
                    cfg.whitelist_success_rate = wl_success_rate
                    cfg.whitelist_jitter_ms = wl_jitter
                    cfg.whitelist_p95_ms = wl_p95_latency
                    
                    cfg.whitelist_verified = (
                        wl_external_reachable
                        and wl_success_rate >= 0.75
                        and wl_latency <= 1500
                        and wl_jitter <= 500
                        and wl_p95_latency is not None
                        and wl_p95_latency <= 2500
                    )
                else:
                    cfg.whitelist_verified = False
            
            working.append(cfg)

    await asyncio.gather(*(check(i, cfg) for i, cfg in enumerate(configs)))
    await cleanup_xray(process, conf_path)
    return working


async def run_phase3_speedtest(configs: List[BaseVPNConfig]):
    process, conf_path = await start_xray_batch(configs, 888)
    if not process:
        return

    sem = asyncio.Semaphore(3)
    async def check(i, cfg):
        async with sem:
            local_port = XRAY_FALLBACK_PORT_START + i
            speed = await check_proxy_speed(local_port, 15.0)
            if speed is not None:
                cfg.download_speed_mbps = speed

    await asyncio.gather(*(check(i, cfg) for i, cfg in enumerate(configs)))
    await cleanup_xray(process, conf_path)


async def validate_all_xray(configs: List[BaseVPNConfig], blocked_ips: set, batch_size: int = 150) -> List[BaseVPNConfig]:
    import urllib.parse
    valid_configs = []
    for c in configs:
        if c.protocol == "vless" and "security=reality" in c.raw_link.lower():
            parsed = urllib.parse.urlparse(c.raw_link)
            query = urllib.parse.parse_qs(parsed.query)
            if "fp" not in query or not query["fp"][0]:
                logger.warning(f"[Validator] Dropping Reality config without fp: {c.host}")
                continue
        valid_configs.append(c)

    history_manager = HistoryManager()
    
    non_quarantined = []
    for c in valid_configs:
        if history_manager.is_quarantined(c.get_fingerprint()):
            continue
        non_quarantined.append(c)
        
    alive_tcp = await pre_filter_configs(non_quarantined, blocked_ips, history_manager)
    
    logger.info(f"[Validator] PHASE 1: Functional tests for {len(alive_tcp)} nodes in batches of {batch_size}...")
    phase1_working = []
    for i in range(0, len(alive_tcp), batch_size):
        batch = alive_tcp[i:i + batch_size]
        logger.info(f"[Validator] Phase 1 - Batch {i // batch_size + 1}")
        res = await run_phase1(batch, i // batch_size)
        phase1_working.extend(res)
        
    logger.info(f"[Validator] PHASE 1 Complete. {len(phase1_working)} nodes alive.")
    
    if not phase1_working:
        return []

    logger.info(f"[Validator] PHASE 2: Accurate ping for {len(phase1_working)} nodes...")
    phase2_working = []
    for i in range(0, len(phase1_working), batch_size):
        batch = phase1_working[i:i + batch_size]
        logger.info(f"[Validator] Phase 2 - Batch {i // batch_size + 1}")
        res = await run_phase2(batch)
        phase2_working.extend(res)

    logger.info(f"[Validator] PHASE 2 Complete. {len(phase2_working)} nodes validated.")

    # Phase 3: Speed test for top 100
    # First, apply history score and initial sort
    for cfg in phase2_working:
        fp = cfg.get_fingerprint()
        cfg.stability_score = history_manager.get_stability_score(fp)
        record = history_manager.get_record(fp)
        cfg.ema_latency = record.get("ema_latency")
        cfg.ema_jitter = record.get("ema_jitter")
    
    phase2_working.sort(key=lambda c: c.get_score(), reverse=True)

    import random
    speed_test_candidates = []
    for c in phase2_working[:70]:
        if c not in speed_test_candidates: speed_test_candidates.append(c)
        
    new_nodes = [c for c in phase2_working if history_manager.get_record(c.get_fingerprint()).get("total_successes", 0) == 0]
    for c in new_nodes[:20]:
        if c not in speed_test_candidates: speed_test_candidates.append(c)
        
    remaining = [c for c in phase2_working if c not in speed_test_candidates]
    random.shuffle(remaining)
    for c in remaining[:10]:
        if c not in speed_test_candidates: speed_test_candidates.append(c)
        
    speed_test_list = list(speed_test_candidates)
    logger.info(f"[Validator] PHASE 3: Speedtest for {len(speed_test_list)} nodes...")
    await run_phase3_speedtest(speed_test_list)
    
    # Final sort after speed test
    phase2_working.sort(key=lambda c: c.get_score(), reverse=True)

    # Update history for all configs that entered Phase 1 (to track failures vs successes)
    # If a config is in phase2_working and success_rate > 0, it's a success. Else fail.
    working_fps = {c.get_fingerprint(): c for c in phase2_working if c.success_rate > 0}
    
    for cfg in alive_tcp:
        fp = cfg.get_fingerprint()
        work_cfg = working_fps.get(fp)
        if work_cfg:
            history_manager.update_record(
                fp,
                success=True,
                latency=work_cfg.latency_ms,
                jitter=work_cfg.jitter_std_ms
            )
        else:
            history_manager.update_record(fp, success=False, failure_reason="xray_failed")
            
    # Clean dead records (fail_count >= 3)
    history_manager.clean_dead_records(max_fails=3)
    history_manager.save()

    logger.info(f"[Validator] Validation fully completed.")
    return phase2_working
