import asyncio
import aiohttp
from src.config import ANTIFILTER_URL, BLOCKLIST_FILE
from src.utils import logger


async def fetch_ru_blocklist() -> set:
    blocked_ips = set()
    logger.info("[Blocklist] Fetching Russian DPI blocklist (antifilter)...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(ANTIFILTER_URL, timeout=10) as resp:
                if resp.status == 200:
                    text = await resp.text()
                    for line in text.splitlines():
                        line = line.strip()
                        if line:
                            blocked_ips.add(line)
                    # Cache locally
                    with open(BLOCKLIST_FILE, "w", encoding="utf-8") as f:
                        f.write(text)
                else:
                    logger.warning("[Blocklist] Failed to fetch. Checking local cache...")
    except Exception as e:
        logger.error(f"[Blocklist] Fetch error: {e}")
        
    if not blocked_ips and BLOCKLIST_FILE.exists():
        with open(BLOCKLIST_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    blocked_ips.add(line)
                    
    logger.info(f"[Blocklist] Loaded {len(blocked_ips)} blocked IPs.")
    return blocked_ips

def is_whitelist_config(cfg_raw: str, cfg_host: str, cfg_port: int, ip: str, blocked_ips: set) -> bool:
    """
    Determines if a node is highly likely to bypass DPI (Whitelist).
    It must use modern DPI-bypass protocols (VLESS/Trojan with TLS/Reality) 
    and its IP must not be in the Antifilter blocklist.
    """
    if not ip or ip in blocked_ips:
        return False
        
    link_lower = cfg_raw.lower()
    
    # Must use modern protocols capable of DPI bypass
    if not ("vless://" in link_lower or "trojan://" in link_lower):
        return False
        
    # Must use TLS or Reality
    if not ("security=tls" in link_lower or "security=reality" in link_lower):
        return False
        
    return True
