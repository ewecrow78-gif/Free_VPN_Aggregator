import base64
import json
import os
import yaml
from collections import defaultdict
from typing import List
from src.models.base import BaseVPNConfig
from src.config import CONFIGS_DIR, ROOT_DIR
from src.utils import logger


# Known Happ/Incy header formats
APP_PROFILE_FORMATS = {
    "Happ": {
        "title_key": "profile-title",
        "update_key": "profile-update-interval",
        "web_key": "profile-web-page",
        "support_key": "support-url",
        "sub_info_key": "subscription-userinfo",
    },
    "Incy": {
        "title_key": "profile-title",
        "update_key": "profile-update-interval",
        "web_key": "profile-web-page",
        "support_key": "support-url",
        "sub_info_key": "subscription-userinfo",
    },
}


def write_subscription_file(
    path: str,
    lines: List[str],
    filter_name: str,
    alive_count: int,
    app_name: str = "",
) -> List[str]:
    full_path = ROOT_DIR / path
    os.makedirs(full_path.parent, exist_ok=True)

    # Human-readable profile title
    if app_name:
        display_title = f"Free VPN · {app_name} · {filter_name} 🚀"
    else:
        display_title = f"Free VPN · {filter_name} 🚀"

    # Days remaining calculation (90 days from now)
    import time
    expire_timestamp = int(time.time()) + (90 * 24 * 60 * 60)

    header = [
        f"#profile-title: base64:{base64.b64encode(display_title.encode('utf-8')).decode('utf-8')}",
        "#profile-web-page: https://github.com/ewecrow78-gif/Free_VPN_Aggregator",
        "#support-url: https://t.me",
        "#profile-update-interval: 1",
        f"#subscription-userinfo: upload=0; download=0; total=854347202560000; expire={expire_timestamp}",
        "#",
        "# ⏱ Нажми на значок спидометра 👆",
        "# 🌐 Подключись к серверу который выдал наименьшее число 🌐",
        "# 🚩 Сервера с отметкой VPN не работают при белых списках 🚩",
        "# 🔑 Полностью бесплатно и Open-Source 🔑",
        "# ⏳ Обновляется каждые 2 часа ⏳",
        "",
    ]

    import urllib.parse
    encoded_name = urllib.parse.quote(display_title)
    dummy_node = f"vless://00000000-0000-0000-0000-000000000000@1.1.1.1:80?security=none&type=tcp#{encoded_name}"

    combined_lines = header + [dummy_node] + lines

    with open(full_path, "w", encoding="utf-8") as f:
        for line in combined_lines:
            f.write(line.strip() + "\n")

    return combined_lines

def write_json_file(path: str, data) -> None:
    full_path = ROOT_DIR / path
    os.makedirs(full_path.parent, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_base64_sub(path: str, lines: List[str]) -> None:
    full_path = ROOT_DIR / path
    os.makedirs(full_path.parent, exist_ok=True)
    content = "\n".join(lines)
    b64_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(b64_content)



def generate_clash_yaml(path: str, configs: List[BaseVPNConfig], filter_name: str) -> None:
    full_path = ROOT_DIR / path
    os.makedirs(full_path.parent, exist_ok=True)

    proxies = []
    proxy_names = []

    for cfg in configs:
        p = cfg.to_clash_proxy()
        proxies.append(p)
        proxy_names.append(cfg.name)

    clash_config = {
        "port": 7890,
        "socks-port": 7891,
        "allow-lan": True,
        "mode": "Rule",
        "log-level": "info",
        "proxies": proxies,
        "proxy-groups": [
            {
                "name": f"Free_VPN_Aggregator [{filter_name}]",
                "type": "select",
                "proxies": proxy_names if proxy_names else ["DIRECT"]
            }
        ],
        "rules": [
            f"MATCH,Free_VPN_Aggregator [{filter_name}]"
        ]
    }

    with open(full_path, "w", encoding="utf-8") as f:
        yaml.dump(clash_config, f, allow_unicode=True, default_flow_style=False)

def generate_sing_box_json(path: str, configs: List[BaseVPNConfig], filter_name: str) -> None:
    full_path = ROOT_DIR / path
    os.makedirs(full_path.parent, exist_ok=True)

    outbounds = []
    proxy_tags = []

    for cfg in configs:
        o = cfg.to_sing_box_outbound()
        outbounds.append(o)
        proxy_tags.append(cfg.name)

    sing_box_config = {
        "log": {"level": "info"},
        "dns": {"servers": [{"address": "https://1.1.1.1/dns-query"}]},
        "outbounds": [
            {
                "type": "selector",
                "tag": "proxy-select",
                "outbounds": proxy_tags if proxy_tags else ["direct"]
            },
            {"type": "direct", "tag": "direct"},
            {"type": "dns", "tag": "dns-out"}
        ] + outbounds,
        "route": {"rules": [{"protocol": "dns", "outbound": "dns-out"}]}
    }

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(sing_box_config, f, ensure_ascii=False, indent=2)

def generate_all_sub_formats(
    txt_path: str,
    b64_path: str,
    clash_path: str,
    sing_box_path: str,
    configs: List[BaseVPNConfig],
    filter_name: str,
    app_name: str = "",
) -> None:
    lines = [c.raw_link for c in configs]
    combined_lines = write_subscription_file(txt_path, lines, filter_name, len(configs), app_name=app_name)
    generate_base64_sub(b64_path, combined_lines)
    generate_clash_yaml(clash_path, configs, filter_name)
    generate_sing_box_json(sing_box_path, configs, filter_name)

def generate_outputs(configs: List[BaseVPNConfig], funnel_stats: dict = None) -> None:
    logger.info(f"[Generator] Generating outputs for {len(configs)} configs...")
    
    if not funnel_stats:
        from src.config import DATA_DIR
        import json
        
        funnel_stats = {
            "downloaded_lines": 0,
            "parsed_configs": 0,
            "rejected_syntax": 0,
            "rejected_dns": 0,
            "rejected_tcp": 0,
            "xray_alive": len(configs),
            "premium": 0
        }
        
        try:
            with open(DATA_DIR / "sources_health.json", "r") as f:
                health = json.load(f)
                funnel_stats["downloaded_lines"] = sum(s.get("downloaded_lines", 0) for s in health.values())
                funnel_stats["parsed_configs"] = sum(s.get("parsed_configs", 0) for s in health.values())
        except: pass
        
        try:
            with open(DATA_DIR / "rejected" / "invalid_syntax.txt", "r") as f: funnel_stats["rejected_syntax"] = len(f.readlines())
        except: pass
        try:
            with open(DATA_DIR / "rejected" / "dns_failed.txt", "r") as f: funnel_stats["rejected_dns"] = len(f.readlines())
        except: pass
        try:
            with open(DATA_DIR / "rejected" / "tcp_failed.txt", "r") as f: funnel_stats["rejected_tcp"] = len(f.readlines())
        except: pass

def is_alive(cfg: BaseVPNConfig) -> bool:
    return cfg.success_rate >= 0.75 and getattr(cfg, "exit_ip_verified", False)

def is_stable(cfg: BaseVPNConfig) -> bool:
    return is_alive(cfg) and getattr(cfg, "stability_score", 0.0) >= 0.70

def is_recommended(cfg: BaseVPNConfig) -> bool:
    if not is_alive(cfg):
        return False
    if cfg.success_rate < 0.875:
        return False
    if getattr(cfg, "stability_score", 0.0) < 0.75:
        return False
    if cfg.latency_ms is None or cfg.latency_ms > 600:
        return False
    if getattr(cfg, "latency_p90_ms", 9999) > 1000:
        return False
    if getattr(cfg, "jitter_std_ms", 9999) > 100:
        return False
    if getattr(cfg, "allow_insecure", False):
        return False
    return True

def load_snis():
    import os
    if not hasattr(load_snis, "cache"):
        load_snis.cache = set()
        if os.path.exists("sni.txt"):
            with open("sni.txt", "r", encoding="utf-8") as f:
                load_snis.cache = {line.strip().lower() for line in f if line.strip()}
    return load_snis.cache

def is_whitelist_candidate(cfg: BaseVPNConfig) -> bool:
    sec = (getattr(cfg, "security", "") or "").lower()
    sni = (getattr(cfg, "sni", "") or "").lower()
    
    if sec not in ("tls", "reality") or not sni:
        return False
    if getattr(cfg, "entry_success_rate", 0) < 0.80:
        return False
        
    snis = load_snis()
    if not snis:
        return True 
        
    for valid_sni in snis:
        if sni == valid_sni or sni.endswith("." + valid_sni):
            return True
    return False

def generate_outputs_old(configs):
    from src.config import DATA_DIR
    
    alive = [c for c in configs if is_alive(c)]
    
    logger.info(f"[Generator] Formatting {len(alive)} alive configs...")
    alive.sort(key=lambda c: getattr(c, "latency_ms", 999999) or 999999)
    for idx, cfg in enumerate(alive):
        flag = getattr(cfg, "flag", "🏳️") or "🏳️"
        cfg.rename(f"{flag} Gh0st #{idx+1}")

    write_json_file("configs/configs.json", [c.model_dump() for c in alive])

    stable = [c for c in alive if is_stable(c)]
    recommended = [c for c in alive if is_recommended(c)]
    whitelist_candidates = [c for c in alive if is_whitelist_candidate(c)]
    top_fast = alive[:50]
    
    # Cap list sizes so they are usable as subscriptions
    alive = alive[:100]
    stable = stable[:100]
    recommended = recommended[:50]
    whitelist_candidates = whitelist_candidates[:100]

    generate_all_sub_formats(
        "configs/all.txt", "configs/base64/all.txt", "configs/clash/all.yaml", "configs/sing-box/all.json",
        configs[:200], "ALL"
    )
    generate_all_sub_formats(
        "configs/top_fast.txt", "configs/base64/top_fast.txt", "configs/clash/top_fast.yaml", "configs/sing-box/top_fast.json",
        top_fast, "TOP_FAST"
    )
    generate_all_sub_formats(
        "configs/alive.txt", "configs/base64/alive.txt", "configs/clash/alive.yaml", "configs/sing-box/alive.json",
        alive, "ALIVE"
    )
    generate_all_sub_formats(
        "configs/stable.txt", "configs/base64/stable.txt", "configs/clash/stable.yaml", "configs/sing-box/stable.json",
        stable, "STABLE"
    )
    generate_all_sub_formats(
        "configs/recommended.txt", "configs/base64/recommended.txt", "configs/clash/recommended.yaml", "configs/sing-box/recommended.json",
        recommended, "RECOMMENDED"
    )
    generate_all_sub_formats(
        "configs/whitelist_candidates.txt", "configs/base64/whitelist_candidates.txt", "configs/clash/whitelist_candidates.yaml", "configs/sing-box/whitelist_candidates.json",
        whitelist_candidates, "WHITELIST_CANDIDATES"
    )

    by_country = defaultdict(list)
    by_proto = defaultdict(list)
    for cfg in alive: # use alive configs for countries/protocols
        by_country[cfg.country_name].append(cfg)
        by_proto[cfg.protocol].append(cfg)

    for country, items in by_country.items():
        safe_name = country.lower().replace(" ", "_")
        generate_all_sub_formats(
            f"configs/countries/{safe_name}.txt", f"configs/base64/country_{safe_name}.txt", f"configs/clash/country_{safe_name}.yaml", f"configs/sing-box/country_{safe_name}.json",
            items, f"COUNTRY_{safe_name.upper()}"
        )

    for proto, items in by_proto.items():
        generate_all_sub_formats(
            f"configs/protocols/{proto}.txt", f"configs/base64/proto_{proto}.txt", f"configs/clash/proto_{proto}.yaml", f"configs/sing-box/proto_{proto}.json",
            items, f"PROTO_{proto.upper()}"
        )

    country_flags = {cfg.country_name: cfg.flag for cfg in alive}
    stats = {
        "funnel": {},
        "total": len(configs), 
        "alive": len(alive),
        "stable": len(stable),
        "recommended": len(recommended),
        "whitelist_candidates": len(whitelist_candidates),
        "by_country": {c: len(items) for c, items in by_country.items()},
        "country_flags": country_flags,
        "by_protocol": {p: len(items) for p, items in by_proto.items()}
    }
    write_json_file("configs/stats.json", stats)
    logger.info("[Generator] Subscriptions generated successfully.")
