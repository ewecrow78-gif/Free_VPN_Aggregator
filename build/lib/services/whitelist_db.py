import os
import json
import ipaddress
import urllib.request
from typing import List, Set
from src.utils import logger
from src.config import DATA_DIR

CACHE_FILE = DATA_DIR / "whitelist_cidrs.json"
CACHE_AGE_HOURS = 24

CLOUDFLARE_V4_URL = "https://www.cloudflare.com/ips-v4"
FASTLY_URL = "https://api.fastly.com/public-ip-list"
GOOGLE_CLOUD_URL = "https://www.gstatic.com/ipranges/cloud.json"

_cached_networks: List[ipaddress.IPv4Network] = []

def fetch_cidrs() -> List[str]:
    cidrs = []
    
    # Cloudflare
    try:
        req = urllib.request.Request(CLOUDFLARE_V4_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            cf_text = response.read().decode('utf-8')
            for line in cf_text.splitlines():
                if line.strip() and not line.startswith('#'):
                    cidrs.append(line.strip())
    except Exception as e:
        logger.error(f"[WhitelistDB] Failed to fetch Cloudflare IPs: {e}")
        
    # Fastly
    try:
        req = urllib.request.Request(FASTLY_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            fastly_data = json.loads(response.read().decode('utf-8'))
            cidrs.extend(fastly_data.get('addresses', []))
    except Exception as e:
        logger.error(f"[WhitelistDB] Failed to fetch Fastly IPs: {e}")
        
    # Google Cloud
    try:
        req = urllib.request.Request(GOOGLE_CLOUD_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            gc_data = json.loads(response.read().decode('utf-8'))
            for prefix in gc_data.get('prefixes', []):
                if 'ipv4Prefix' in prefix:
                    cidrs.append(prefix['ipv4Prefix'])
    except Exception as e:
        logger.error(f"[WhitelistDB] Failed to fetch Google Cloud IPs: {e}")

    return list(set(cidrs))

def load_whitelist_cidrs():
    global _cached_networks
    if _cached_networks:
        return
        
    import time
    
    needs_update = True
    if CACHE_FILE.exists():
        age = time.time() - CACHE_FILE.stat().st_mtime
        if age < CACHE_AGE_HOURS * 3600:
            needs_update = False
            
    cidrs = []
    if needs_update:
        logger.info("[WhitelistDB] Fetching updated CIDRs for whitelists...")
        cidrs = fetch_cidrs()
        if cidrs:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cidrs, f, indent=2)
    
    if not cidrs and CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cidrs = json.load(f)
            
    for c in cidrs:
        try:
            _cached_networks.append(ipaddress.IPv4Network(c, strict=False))
        except ValueError:
            pass
            
    logger.info(f"[WhitelistDB] Loaded {len(_cached_networks)} IPv4 whitelist CIDR blocks.")

def is_ip_whitelisted(ip_str: str) -> bool:
    if not _cached_networks:
        load_whitelist_cidrs()
        
    try:
        addr = ipaddress.IPv4Address(ip_str)
        for net in _cached_networks:
            if addr in net:
                return True
    except ValueError:
        pass
        
    return False

_trusted_snis: Set[str] = set()

def load_trusted_snis():
    global _trusted_snis
    if _trusted_snis:
        return
        
    sni_file = DATA_DIR.parent / "sni.txt"
    if sni_file.exists():
        with open(sni_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    _trusted_snis.add(line.strip().lower())
    logger.info(f"[WhitelistDB] Loaded {len(_trusted_snis)} trusted SNIs.")

def is_sni_whitelisted(sni: str) -> bool:
    if not _trusted_snis:
        load_trusted_snis()
        
    if not sni:
        return False
        
    return sni.strip().lower() in _trusted_snis
