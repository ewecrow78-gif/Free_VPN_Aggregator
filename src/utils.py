import base64
import json
import logging
import socket
from pathlib import Path
from typing import Dict, Tuple

# Logger Setup
def setup_logger(name: str = "vpn_aggregator") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        fmt = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    return logger

logger = setup_logger()

def is_base64_data(data: str) -> bool:
    text = data.strip()
    if "\n" in text or " " in text or "\r" in text:
        return False
    try:
        base64.b64decode(text + "==", validate=True)
        return True
    except Exception:
        return False

def decode_maybe_base64(data: str) -> str:
    if is_base64_data(data):
        try:
            decoded = base64.b64decode(data + "==")
            return decoded.decode("utf-8", errors="ignore")
        except Exception:
            pass
    return data

def resolve_ip(host: str) -> str:
    import re
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host):
        return host
    try:
        return socket.gethostbyname(host)
    except:
        return ""

async def batch_geoip_lookup(configs, session):
    import os
    import maxminddb
    from src.models.base import ISO_TO_FLAG, COUNTRY_ISO_MAP
    
    db_path = "GeoLite2-Country.mmdb"
    db_url = "https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb"
    
    if not os.path.exists(db_path):
        logger.info("[GeoIP] Downloading offline GeoIP database...")
        try:
            async with session.get(db_url) as resp:
                if resp.status == 200:
                    with open(db_path, "wb") as f:
                        f.write(await resp.read())
        except Exception as e:
            logger.error(f"[GeoIP] Failed to download DB: {e}")
            
    # Extract unique IPs
    ip_to_configs = {}
    for cfg in configs:
        import socket
        try:
            ip = socket.gethostbyname(cfg.host)
        except:
            ip = cfg.host
        if ip not in ip_to_configs:
            ip_to_configs[ip] = []
        ip_to_configs[ip].append(cfg)
        
    if os.path.exists(db_path):
        try:
            with maxminddb.open_database(db_path) as reader:
                for ip, cfgs in ip_to_configs.items():
                    iso = "UN"
                    c_name = "unknown"
                    try:
                        res = reader.get(ip)
                        if res and 'country' in res and 'iso_code' in res['country']:
                            iso = res['country']['iso_code']
                            c_name = res['country'].get('names', {}).get('en', iso)
                    except:
                        pass
                        
                    for cfg in cfgs:
                        cfg.country_iso = iso
                        cfg.country_name = c_name
                        cfg.flag = ISO_TO_FLAG.get(iso, "🏳️")
        except Exception as e:
            logger.error(f"[GeoIP] maxminddb lookup error: {e}")
            
    # Ensure defaults
    for cfg in configs:
        if not hasattr(cfg, 'flag') or cfg.flag == "🏳️":
            cfg.flag = "🏳️"
