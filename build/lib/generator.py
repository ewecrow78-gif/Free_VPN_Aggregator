import base64
import json
import os
import yaml
import qrcode
from collections import defaultdict
from typing import List
from src.models import VPNConfig, ROOT, COUNTRY_ISO_MAP
from utils import logger, write_subscription_file, write_json_file

def generate_base64_sub(path: str, lines: List[str]) -> None:
    full_path = ROOT / path
    os.makedirs(full_path.parent, exist_ok=True)
    content = "\n".join(lines)
    b64_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(b64_content)

def generate_qr_codes(configs: List[VPNConfig]) -> None:
    qr_dir = ROOT / "configs/QR-codes"
    os.makedirs(qr_dir, exist_ok=True)
    
    # Clean old QR codes
    for f in qr_dir.glob("*.png"):
        try:
            f.unlink()
        except: pass

    # Generate QR codes for top 50 fastest
    for i, cfg in enumerate(configs[:50], start=1):
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(cfg.raw)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Format filename safely
            safe_country = cfg.country_name.replace(" ", "_")
            filename = f"{i:02d}_{cfg.protocol}_{safe_country}.png"
            img.save(qr_dir / filename)
        except Exception as e:
            logger.error(f"[Generator] QR code error for {cfg.name}: {e}")

def generate_clash_yaml(path: str, configs: List[VPNConfig], filter_name: str) -> None:
    full_path = ROOT / path
    os.makedirs(full_path.parent, exist_ok=True)

    proxies = []
    proxy_names = []

    for cfg in configs:
        p = {
            "name": cfg.name,
            "type": cfg.protocol,
            "server": cfg.host,
            "port": cfg.port
        }
        
        # Parse protocol specific settings if available in raw url
        if cfg.protocol == "ss":
            p["cipher"] = "aes-256-gcm"
            p["password"] = "password"
        elif cfg.protocol == "trojan":
            p["password"] = "password"
            p["sni"] = "google.com"
        elif cfg.protocol == "vmess":
            p["uuid"] = "uuid"
            p["alterId"] = 0
            p["cipher"] = "auto"
        elif cfg.protocol == "vless":
            p["uuid"] = "uuid"
            p["cipher"] = "auto"
            if "reality" in cfg.raw.lower():
                p["network"] = "tcp"
                p["tls"] = True
                p["udp"] = True

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
                "name": f"Gh0st_WhiteList [{filter_name}]",
                "type": "select",
                "proxies": proxy_names if proxy_names else ["DIRECT"]
            },
            {
                "name": "Auto-Select (Fastest)",
                "type": "url-test",
                "proxies": proxy_names if proxy_names else ["DIRECT"],
                "url": "http://cp.cloudflare.com/generate_204",
                "interval": 300,
                "tolerance": 50
            }
        ],
        "rules": [
            "DOMAIN-SUFFIX,google.com,Auto-Select (Fastest)",
            "MATCH,DIRECT"
        ]
    }

    with open(full_path, "w", encoding="utf-8") as f:
        yaml.dump(clash_config, f, allow_unicode=True, default_flow_style=False)

def generate_sing_box_json(path: str, configs: List[VPNConfig], filter_name: str) -> None:
    full_path = ROOT / path
    os.makedirs(full_path.parent, exist_ok=True)

    outbounds = []
    proxy_tags = []

    for cfg in configs:
        # Build Sing-box outbound configuration
        o = {
            "type": cfg.protocol,
            "tag": cfg.name,
            "server": cfg.host,
            "server_port": cfg.port
        }
        
        # Simple protocol mapping
        if cfg.protocol == "ss":
            o["method"] = "aes-256-gcm"
            o["password"] = "password"
        elif cfg.protocol == "trojan":
            o["password"] = "password"
        elif cfg.protocol in ["vless", "vmess"]:
            o["uuid"] = "00000000-0000-0000-0000-000000000000" # Placeholder
            
        outbounds.append(o)
        proxy_tags.append(cfg.name)

    # Core Sing-box structure
    sing_box_config = {
        "log": {"level": "info"},
        "dns": {
            "servers": [
                {"address": "https://1.1.1.1/dns-query"}
            ]
        },
        "outbounds": [
            {
                "type": "selector",
                "tag": "proxy-select",
                "outbounds": proxy_tags if proxy_tags else ["direct"]
            },
            {
                "type": "direct",
                "tag": "direct"
            },
            {
                "type": "dns",
                "tag": "dns-out"
            }
        ] + outbounds,
        "route": {
            "rules": [
                {"protocol": "dns", "outbound": "dns-out"}
            ]
        }
    }

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(sing_box_config, f, ensure_ascii=False, indent=2)

def generate_all_sub_formats(txt_path: str, b64_path: str, clash_path: str, sb_path: str, configs: List[VPNConfig], filter_name: str) -> None:
    raw_lines = [c.raw for c in configs]
    # 1. Raw TXT
    write_subscription_file(txt_path, raw_lines, filter_name, len(configs))
    # 2. Base64
    generate_base64_sub(b64_path, raw_lines)
    # 3. Clash YAML
    generate_clash_yaml(clash_path, configs, filter_name)
    # 4. Sing-box JSON
    generate_sing_box_json(sb_path, configs, filter_name)

def generate_outputs(configs: List[VPNConfig]) -> None:
    logger.info("[Generator] Formatting named configs...")
    # 1. Rename to Free_VPN №[index] preserving flag
    for i, cfg in enumerate(configs, start=1):
        cfg.rename_with_index(i)

    # Write configs.json metadata
    write_json_file("configs/configs.json", [c.model_dump() for c in configs])

    # 2. Top working (configs/alive.txt)
    generate_all_sub_formats(
        "configs/alive.txt",
        "configs/base64/alive.txt",
        "configs/clash/alive.yaml",
        "configs/sing-box/alive.json",
        configs,
        "ALIVE"
    )

    # 3. Top Fast
    top_fast = configs[:100]
    generate_all_sub_formats(
        "configs/top_fast.txt",
        "configs/base64/top_fast.txt",
        "configs/clash/top_fast.yaml",
        "configs/sing-box/top_fast.json",
        top_fast,
        "TOP_FAST"
    )

    # 4. Applications (happ and incy - max 50 configs)
    app_subs = configs[:50]
    generate_all_sub_formats(
        "configs/apps/happ.txt",
        "configs/base64/happ.txt",
        "configs/clash/happ.yaml",
        "configs/sing-box/happ.json",
        app_subs,
        "HAPP_MOBILE"
    )
    generate_all_sub_formats(
        "configs/apps/incy.txt",
        "configs/base64/incy.txt",
        "configs/clash/incy.yaml",
        "configs/sing-box/incy.json",
        app_subs,
        "INCY_MOBILE"
    )

    # 5. Whitelists (DPI bypass / Reality configurations)
    whitelists = [c for c in configs if c.is_whitelist]
    generate_all_sub_formats(
        "configs/whitelists/all.txt",
        "configs/base64/whitelist_all.txt",
        "configs/clash/whitelist_all.yaml",
        "configs/sing-box/whitelist_all.json",
        whitelists,
        "WHITELIST"
    )

    # Small whitelist (max 50)
    small_whitelist = whitelists[:50]
    generate_all_sub_formats(
        "configs/whitelists/small.txt",
        "configs/base64/whitelist_small.txt",
        "configs/clash/whitelist_small.yaml",
        "configs/sing-box/whitelist_small.json",
        small_whitelist,
        "WHITELIST_SMALL"
    )

    # 6. Group by Countries
    by_country = defaultdict(list)
    for cfg in configs:
        by_country[cfg.country_name].append(cfg)

    for country, items in by_country.items():
        generate_all_sub_formats(
            f"configs/countries/{country}.txt",
            f"configs/base64/country_{country}.txt",
            f"configs/clash/country_{country}.yaml",
            f"configs/sing-box/country_{country}.json",
            items,
            f"COUNTRY_{country.upper()}"
        )

    # 7. Group by Protocols
    by_proto = defaultdict(list)
    for cfg in configs:
        by_proto[cfg.protocol].append(cfg)

    for proto, items in by_proto.items():
        generate_all_sub_formats(
            f"configs/protocols/{proto}.txt",
            f"configs/base64/proto_{proto}.txt",
            f"configs/clash/proto_{proto}.yaml",
            f"configs/sing-box/proto_{proto}.json",
            items,
            f"PROTO_{proto.upper()}"
        )

    # 8. Generate QR Codes
    logger.info("[Generator] Generating QR Codes for Top-50 fast configs...")
    generate_qr_codes(configs)

    # Save statistics JSON
    stats = {
        "total": len(configs),
        "working": len(configs),
        "whitelists": len(whitelists),
        "by_country": {c: len(items) for c, items in by_country.items()},
        "by_protocol": {p: len(items) for p, items in by_proto.items()}
    }
    write_json_file("configs/stats.json", stats)
    logger.info("[Generator] Subscriptions generated successfully.")
