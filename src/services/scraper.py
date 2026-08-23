import os
import asyncio
import json
import re
import aiohttp
from typing import List, Set
from telethon import TelegramClient
from telethon.sessions import StringSession
from src.config import TG_CHANNELS_FILE, TG_FORUMS_FILE, URLS_FILE, TG_API_ID, TG_API_HASH, TG_SESSION
from src.models.base import BaseVPNConfig
from src.models.protocols import parse_link, safe_b64decode
from src.utils import logger, decode_maybe_base64
from src.services.source_manager import SourceManager, fetch_all_sources
from src.services.happ_manager import decrypt_happ
import urllib.parse

CONFIG_RE = re.compile(
    r"(vmess://[a-zA-Z0-9+/=_-]+|vless://[^\s#]+(?:#[^\s]*)?|trojan://[^\s#]+(?:#[^\s]*)?|ss://[^\s#]+(?:#[^\s]*)?)", 
    re.IGNORECASE
)
HAPP_RE = re.compile(r"happ://[^\s]+", re.IGNORECASE)

def load_sources(file_path) -> List[str]:
    if not file_path.exists():
        return []
    sources = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                sources.append(line)
    return sources

def convert_json_to_uris(text: str) -> List[str]:
    uris = []
    text = text.strip()
    if not (text.startswith('[') or text.startswith('{')):
        return uris
    
    try:
        data = json.loads(text)
    except Exception:
        return uris
        
    if isinstance(data, dict):
        configs = [data]
    elif isinstance(data, list):
        configs = data
    else:
        return uris
        
    for item in configs:
        if not isinstance(item, dict):
            continue
        remarks = item.get("remarks") or item.get("tag") or "Free_VPN"
        outbounds = item.get("outbounds") or []
        proxy_outbound = None
        for out in outbounds:
            proto = out.get("protocol")
            if proto in ["vless", "vmess", "trojan", "shadowsocks", "ss", "hysteria", "hysteria2", "tuic"]:
                proxy_outbound = out
                break
        
        if not proxy_outbound:
            if item.get("protocol") in ["vless", "vmess", "trojan", "shadowsocks", "ss", "hysteria", "hysteria2", "tuic"]:
                proxy_outbound = item
            else:
                continue
                
        proto = proxy_outbound.get("protocol")
        settings = proxy_outbound.get("settings") or {}
        stream = proxy_outbound.get("streamSettings") or {}
        
        host = ""
        port = 0
        user_id = ""
        
        if proto in ["vless", "vmess"]:
            vnext = settings.get("vnext") or []
            if vnext:
                srv = vnext[0]
                host = srv.get("address") or ""
                port = srv.get("port") or 0
                users = srv.get("users") or []
                if users:
                    user_id = users[0].get("id") or ""
                    
        elif proto == "trojan":
            servers = settings.get("servers") or []
            if servers:
                srv = servers[0]
                host = srv.get("address") or ""
                port = srv.get("port") or 0
                user_id = srv.get("password") or ""
                
        elif proto in ["shadowsocks", "ss"]:
            servers = settings.get("servers") or []
            if servers:
                srv = servers[0]
                host = srv.get("address") or ""
                port = srv.get("port") or 0
                method = srv.get("method") or ""
                password = srv.get("password") or ""
                user_id = f"{method}:{password}"
                
        if not host or not port:
            continue
            
        params = {}
        net = stream.get("network") or "tcp"
        security = stream.get("security") or "none"
        
        params["type"] = net
        if security:
            params["security"] = security
            
        if security == "reality":
            reality = stream.get("realitySettings") or {}
            params["sni"] = reality.get("serverName") or ""
            params["pbk"] = reality.get("publicKey") or ""
            params["sid"] = reality.get("shortId") or ""
            params["fp"] = reality.get("fingerprint") or "firefox"
            
        elif security == "tls":
            tls = stream.get("tlsSettings") or {}
            params["sni"] = tls.get("serverName") or ""
            
        if net == "ws":
            ws = stream.get("wsSettings") or {}
            params["path"] = ws.get("path") or "/"
            headers = ws.get("headers") or {}
            params["host"] = headers.get("Host") or ""
        elif net == "grpc":
            grpc = stream.get("grpcSettings") or {}
            params["serviceName"] = grpc.get("serviceName") or ""
            
        if proto == "vless":
            vnext = settings.get("vnext") or []
            if vnext and vnext[0].get("users"):
                flow = vnext[0]["users"][0].get("flow") or ""
                if flow:
                    params["flow"] = flow
                    
        query = urllib.parse.urlencode({k: v for k, v in params.items() if v})
        remark_encoded = urllib.parse.quote(remarks)
        
        if proto == "vless":
            uri = f"vless://{user_id}@{host}:{port}?{query}#{remark_encoded}"
            uris.append(uri)
        elif proto == "vmess":
            vmess_json = {
                "v": "2",
                "ps": remarks,
                "add": host,
                "port": port,
                "id": user_id,
                "aid": 0,
                "scy": "auto",
                "net": net,
                "type": "none",
                "host": params.get("host", ""),
                "path": params.get("path", ""),
                "tls": "tls" if security == "tls" else ""
            }
            if security == "tls":
                vmess_json["sni"] = params.get("sni", "")
            import base64
            encoded = base64.b64encode(json.dumps(vmess_json).encode("utf-8")).decode("utf-8")
            uri = f"vmess://{encoded}"
            uris.append(uri)
        elif proto == "trojan":
            uri = f"trojan://{user_id}@{host}:{port}?{query}#{remark_encoded}"
            uris.append(uri)
        elif proto in ["shadowsocks", "ss"]:
            import base64
            user_b64 = base64.b64encode(user_id.encode("utf-8")).decode("utf-8").replace("=", "")
            uri = f"ss://{user_b64}@{host}:{port}#{remark_encoded}"
            uris.append(uri)
            
    return uris

B64_BLOCK_RE = re.compile(r"([A-Za-z0-9+/=]{32,})")

def extract_configs_from_text(text: str) -> List[BaseVPNConfig]:
    text_stripped = text.strip()
    configs = []
    found_keys = set()

    def add_cfg(cfg):
        if cfg:
            key = f"{cfg.protocol}://{cfg.host}:{cfg.port}"
            if key not in found_keys:
                found_keys.add(key)
                configs.append(cfg)

    # 1. Try full base64 decode
    try:
        decoded_full = safe_b64decode(text_stripped).decode("utf-8", errors="ignore")
        if decoded_full and decoded_full != text_stripped:
            for m in CONFIG_RE.findall(decoded_full):
                add_cfg(parse_link(m.strip()))
            for uri in convert_json_to_uris(decoded_full):
                add_cfg(parse_link(uri))
    except Exception:
        pass

    # 2. Try JSON formats (e.g. Nekobox)
    json_uris = convert_json_to_uris(text_stripped)
    for m in json_uris:
        add_cfg(parse_link(m))

    # 3. Direct URI regex
    matches = CONFIG_RE.findall(text)
    for m in matches:
        add_cfg(parse_link(m.strip()))

    # 4. Search for embedded base64 blocks inside HTML or text (e.g. Yandex Translate HTML pages)
    if not configs:
        b64_blocks = B64_BLOCK_RE.findall(text)
        for block in b64_blocks:
            try:
                dec = safe_b64decode(block).decode("utf-8", errors="ignore")
                if any(p in dec for p in ["vless://", "vmess://", "trojan://", "ss://"]):
                    for m in CONFIG_RE.findall(dec):
                        add_cfg(parse_link(m.strip()))
            except Exception:
                pass

    return configs


def unwrap_proxy_urls(url: str) -> List[str]:
    """Unwrap proxy/translator wrapper URLs like Yandex Translate."""
    urls = [url]
    if "translate." in url and "url=" in url:
        try:
            parsed = urllib.parse.urlparse(url)
            qs = urllib.parse.parse_qs(parsed.query)
            if "url" in qs and qs["url"]:
                target_url = urllib.parse.unquote(qs["url"][0])
                if target_url.startswith("http"):
                    # Add target URL to list (try direct first, then translator URL)
                    urls.insert(0, target_url)
        except Exception as e:
            logger.debug(f"[Scraper] Failed to unwrap translate URL: {e}")
    return list(dict.fromkeys(urls))  # deduplicate preserving order


async def fetch_url(session: aiohttp.ClientSession, url: str, max_retries: int = 3) -> List[BaseVPNConfig]:
    if url.startswith("happ://"):
        logger.info(f"[Scraper] Decrypting encrypted HAPP link: {url}")
        decrypted = await decrypt_happ(url)
        if decrypted:
            if decrypted.startswith("http"):
                url = decrypted
            else:
                configs = extract_configs_from_text(decrypted)
                logger.info(f"[Scraper] Found {len(configs)} configs in decrypted HAPP link")
                return configs
        else:
            logger.warning(f"[Scraper] Failed to decrypt HAPP link: {url}")
            return []

    candidate_urls = unwrap_proxy_urls(url)
    
    for candidate in candidate_urls:
        for attempt in range(1, max_retries + 1):
            logger.info(f"[Scraper] Fetching (Attempt {attempt}/{max_retries}): {candidate}")
            try:
                # Use ssl=False to support direct IP addresses with custom/self-signed certs
                async with session.get(candidate, timeout=12, ssl=False) as response:
                    if response.status == 200:
                        raw = await response.read()
                        try:
                            text = safe_b64decode(raw.decode("utf-8")).decode("utf-8", errors="ignore")
                        except Exception:
                            text = raw.decode("utf-8", errors="ignore")
                        
                        configs = extract_configs_from_text(text)
                        if configs:
                            logger.info(f"[Scraper] Found {len(configs)} configs at {candidate}")
                            return configs
                    else:
                        logger.warning(f"[Scraper] Bad status {response.status} for {candidate}")
            except Exception as e:
                logger.error(f"[Scraper] URL failed {candidate}: {e}")
            
            if attempt < max_retries:
                await asyncio.sleep(2 * attempt)
                
    return []

def parse_tg_target(target: str):
    target = target.strip()
    if not target:
        return None
    # Handle private channel link: https://t.me/c/3965700735/123 -> -1003965700735
    c_match = re.search(r"t\.me/c/(\d+)", target)
    if c_match:
        return int(f"-100{c_match.group(1)}")
    
    # Handle numeric ID strings e.g. "-1003965700735" or "1003965700735"
    num_str = target.replace("https://t.me/", "").replace("t.me/", "").strip("@/ ")
    if num_str.lstrip("-").isdigit():
        val = int(num_str)
        if val > 0:
            if not str(val).startswith("100"):
                return int(f"-100{val}")
            else:
                return int(f"-{val}")
        return val

    # Handle standard URLs e.g. https://t.me/channelname -> channelname
    if "t.me/" in target:
        path = target.split("t.me/")[-1].strip("/")
        if not path.startswith("+") and not path.startswith("joinchat/"):
            return path

async def fetch_telegram_web_preview(username: str):
    configs = []
    urls = set()
    happ_urls = set()
    clean_name = str(username).replace("https://t.me/", "").replace("t.me/", "").strip("@/ ")
    web_url = f"https://t.me/s/{clean_name}"
    
    URL_RE = re.compile(r"https?://[^\s\"'>]+", re.IGNORECASE)
    HAPP_RE = re.compile(r"happ://[^\s\"'>]+", re.IGNORECASE)

    logger.info(f"[Scraper] Trying public web preview fallback for @{clean_name}: {web_url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(web_url, timeout=12, ssl=False) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    configs.extend(extract_configs_from_text(html))
                    for u in URL_RE.findall(html):
                        urls.add(u)
                    for hu in HAPP_RE.findall(html):
                        happ_urls.add(hu)
                    logger.info(f"[Scraper] Web preview @{clean_name} fetched {len(configs)} configs")
    except Exception as e:
        logger.warning(f"[Scraper] Web preview fallback failed for @{clean_name}: {e}")
        
    return configs, urls, happ_urls


async def fetch_telegram() -> List[BaseVPNConfig]:
    configs = []
    if not TG_API_ID or not TG_API_HASH or not TG_SESSION:
        logger.warning("[Scraper] No Telegram secrets found. Skipping Telethon.")
        return configs

    channels = load_sources(TG_CHANNELS_FILE)
    forums = load_sources(TG_FORUMS_FILE)
    if not channels and not forums:
        return configs

    URL_RE = re.compile(r"https?://[^\s]+", re.IGNORECASE)
    collected_urls = set()

    logger.info("[Scraper] Connecting to Telegram...")
    try:
        import python_socks
        client = TelegramClient(
            StringSession(TG_SESSION), 
            int(TG_API_ID), 
            TG_API_HASH, 
            proxy=(python_socks.ProxyType.SOCKS5, "127.0.0.1", int(os.environ.get("PROXY_PORT", 10000)), False)
        )
        await client.connect()
        if not await client.is_user_authorized():
            logger.error("[Scraper] Telegram session invalid.")
            return configs

        # Fetch dialogs to populate Telethon's entity cache for private channels/groups
        try:
            logger.info("[Scraper] Fetching TG dialogs to cache private channel entities...")
            await client.get_dialogs(limit=300)
        except Exception as d_err:
            logger.warning(f"[Scraper] Could not fetch dialogs cache: {d_err}")

        collected_happ_urls = set()

        targets = [(c, 20) for c in channels] + [(f, 100) for f in forums]

        for target_raw, limit in targets:
            target = parse_tg_target(target_raw)
            if not target:
                continue
            logger.info(f"[Scraper] Scraping TG: {target} (raw='{target_raw}', limit={limit})")
            try:
                async for message in client.iter_messages(target, limit=limit):
                    text_content = message.message or ""
                    configs.extend(extract_configs_from_text(text_content))
                    for url in URL_RE.findall(text_content):
                        collected_urls.add(url)
                    for happ_url in HAPP_RE.findall(text_content):
                        collected_happ_urls.add(happ_url)
                    
                    # Extract URLs from inline buttons
                    if message.buttons:
                        for row in message.buttons:
                            for button in row:
                                if hasattr(button, 'url') and button.url:
                                    if button.url.startswith('http'):
                                        collected_urls.add(button.url)
                                    elif button.url.startswith('happ://'):
                                        collected_happ_urls.add(button.url)
                                    else:
                                        configs.extend(extract_configs_from_text(button.url))
                                        
                    # Extract URLs from formatted text (Markdown/HTML links)
                    if message.entities:
                        for entity, text in message.get_entities_text():
                            if hasattr(entity, 'url') and entity.url:
                                if entity.url.startswith('http'):
                                    collected_urls.add(entity.url)
                                elif entity.url.startswith('happ://'):
                                    collected_happ_urls.add(entity.url)
                                else:
                                    configs.extend(extract_configs_from_text(entity.url))
            except Exception as err:
                logger.error(f"[Scraper] TG Channel {target} error: {err}")
                # If banned/blocked in a public channel, fall back to Telegram's public web preview t.me/s/channel
                if isinstance(target, str) and not str(target).startswith("-"):
                    w_cfgs, w_urls, w_happ = await fetch_telegram_web_preview(target)
                    configs.extend(w_cfgs)
                    collected_urls.update(w_urls)
                    collected_happ_urls.update(w_happ)

                
        await client.disconnect()

        # Decrypt HAPP links first
        if collected_happ_urls:
            logger.info(f"[Scraper] Found {len(collected_happ_urls)} HAPP encrypted links. Decrypting...")
            for happ_url in collected_happ_urls:
                decrypted = await decrypt_happ(happ_url)
                if decrypted:
                    if decrypted.startswith('http'):
                        collected_urls.add(decrypted)
                    else:
                        configs.extend(extract_configs_from_text(decrypted))

        if collected_urls:
            logger.info(f"[Scraper] Found {len(collected_urls)} HTTP links in Telegram. Fetching...")
            async with aiohttp.ClientSession() as session:
                urls_list = list(collected_urls)
                chunk_size = 5000
                for i in range(0, len(urls_list), chunk_size):
                    chunk = urls_list[i:i+chunk_size]
                    tasks = [fetch_url(session, url) for url in chunk]
                    results = await asyncio.gather(*tasks)
                    for res in results:
                        configs.extend(res)

    except Exception as e:
        logger.error(f"[Scraper] Telegram error: {e}")
        
    return configs

async def scrape_all() -> List[BaseVPNConfig]:
    all_configs = []
    
    # 1. HTTP Sources (sources.json)
    logger.info("[Scraper] Fetching HTTP sources...")
    src_manager = SourceManager()
    http_data = await fetch_all_sources(src_manager)
    
    for source_name, text in http_data.items():
        if not text:
            src_manager.update_health(source_name, downloaded=0, parsed=0)
            continue
            
        lines_count = len(text.splitlines())
        decoded = decode_maybe_base64(text)
        links = CONFIG_RE.findall(decoded)
        
        parsed_count = 0
        for link in links:
            try:
                cfg = parse_link(link)
                if cfg:
                    all_configs.append(cfg)
                    parsed_count += 1
            except Exception:
                pass
                
        src_manager.update_health(source_name, downloaded=lines_count, parsed=parsed_count)
        
    src_manager.save_health()

    # 2. HTTP urls.txt (direct fallback sources)
    urls_txt = load_sources(URLS_FILE)
    if urls_txt:
        logger.info(f"[Scraper] Fetching {len(urls_txt)} URLs from urls.txt...")
        async with aiohttp.ClientSession() as session:
            chunk_size = 5000
            for i in range(0, len(urls_txt), chunk_size):
                chunk = urls_txt[i:i+chunk_size]
                tasks = [fetch_url(session, url) for url in chunk]
                results = await asyncio.gather(*tasks)
                for res in results:
                    all_configs.extend(res)
    
    # 3. Telegram Sources
    logger.info("[Scraper] Attempting to scrape Telegram channels...")
    try:
        tg_configs = await fetch_telegram()
        if tg_configs:
            all_configs.extend(tg_configs)
            logger.info(f"[Scraper] Telegram scraping successful. Collected {len(tg_configs)} configs.")
            try:
                import os
                os.makedirs("configs/tgk", exist_ok=True)
                with open("configs/tgk/tgk_raw.txt", "w", encoding="utf-8") as f:
                    for c in tg_configs:
                        f.write(c.raw_link + "\n")
            except Exception as e:
                logger.error(f"[Scraper] Failed to save tgk_raw.txt: {e}")
        else:
            logger.warning("[Scraper] No configs collected from Telegram. Check your TG_SESSION, API keys, or tg_channels.txt.")
    except Exception as e:
        logger.error(f"[Scraper] Telegram scraper failed: {e}")

    # Deduplicate by protocol, host, and port
    unique = {}
    for c in all_configs:
        key = f"{c.protocol}://{c.host}:{c.port}"
        if key not in unique:
            unique[key] = c
    final_list = list(unique.values())
    
    logger.info(f"[Scraper] Scrape complete. Total unique configs: {len(final_list)}")
    return final_list

