import json
import os
import time
from typing import List, Dict, Any
import aiohttp
import asyncio
from src.config import DATA_DIR
from src.utils import logger

SOURCES_FILE = DATA_DIR / "sources.json"
HEALTH_FILE = DATA_DIR / "sources_health.json"

DEFAULT_SOURCES = [
    {
        "name": "barry-far All",
        "url": "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt",
        "type": "mixed",
        "priority": 80,
        "enabled": True,
        "trust_level": "medium"
    },
    {
        "name": "matryoshka whitelist",
        "url": "https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt",
        "type": "whitelist",
        "priority": 90,
        "enabled": True,
        "trust_level": "high"
    },
    {
        "name": "goida configs",
        "url": "https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/configs/alive.txt",
        "type": "mixed",
        "priority": 85,
        "enabled": True,
        "trust_level": "medium"
    },
    {
        "name": "kort0881 alive",
        "url": "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/output/alive.txt",
        "type": "mixed",
        "priority": 80,
        "enabled": True,
        "trust_level": "medium"
    }
]

class SourceManager:
    def __init__(self):
        self.sources = []
        self.health = {}
        self.load_sources()
        self.load_health()

    def load_sources(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(SOURCES_FILE):
            with open(SOURCES_FILE, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_SOURCES, f, indent=2)
            self.sources = DEFAULT_SOURCES
        else:
            try:
                with open(SOURCES_FILE, "r", encoding="utf-8") as f:
                    self.sources = json.load(f)
            except Exception as e:
                logger.error(f"[SourceManager] Failed to load sources.json: {e}")
                self.sources = DEFAULT_SOURCES

    def load_health(self):
        if os.path.exists(HEALTH_FILE):
            try:
                with open(HEALTH_FILE, "r", encoding="utf-8") as f:
                    self.health = json.load(f)
            except Exception as e:
                logger.error(f"[SourceManager] Failed to load sources_health.json: {e}")
                self.health = {}

    def save_health(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        try:
            with open(HEALTH_FILE, "w", encoding="utf-8") as f:
                json.dump(self.health, f, indent=2)
        except Exception as e:
            logger.error(f"[SourceManager] Failed to save sources_health.json: {e}")

    def init_health_record(self, name: str):
        if name not in self.health:
            self.health[name] = {
                "status": "ok",
                "downloaded_lines": 0,
                "parsed_configs": 0,
                "unique_configs": 0,
                "alive_configs": 0,
                "success_rate": 0.0,
                "last_success": ""
            }

    def update_health(self, name: str, downloaded: int, parsed: int):
        self.init_health_record(name)
        self.health[name]["downloaded_lines"] += downloaded
        self.health[name]["parsed_configs"] += parsed
        if parsed > 0:
            self.health[name]["status"] = "ok"
            self.health[name]["last_success"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        else:
            self.health[name]["status"] = "failed_parse"

    def update_alive(self, name: str, unique: int, alive: int):
        self.init_health_record(name)
        self.health[name]["unique_configs"] += unique
        self.health[name]["alive_configs"] += alive
        total_unique = self.health[name]["unique_configs"]
        total_alive = self.health[name]["alive_configs"]
        if total_unique > 0:
            self.health[name]["success_rate"] = total_alive / total_unique

    def get_enabled_sources(self):
        # Auto-disable bad sources (e.g., success_rate < 0.001 and high parsed count)
        for s in self.sources:
            name = s["name"]
            if name in self.health:
                h = self.health[name]
                if h["parsed_configs"] > 1000 and h["success_rate"] < 0.001:
                    logger.warning(f"[SourceManager] Disabling source '{name}' due to low success rate.")
                    s["enabled"] = False
                    
        return [s for s in self.sources if s.get("enabled", True)]

async def fetch_source(session: aiohttp.ClientSession, source: dict) -> str:
    url = source.get("url")
    if not url:
        return ""
    try:
        async with session.get(url, timeout=15.0) as resp:
            if resp.status == 200:
                return await resp.text()
    except Exception as e:
        logger.warning(f"[SourceManager] Fetch failed for {source['name']}: {e}")
    return ""

async def fetch_all_sources(manager: SourceManager) -> Dict[str, str]:
    sources = manager.get_enabled_sources()
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_source(session, s) for s in sources]
        responses = await asyncio.gather(*tasks)
        for i, s in enumerate(sources):
            results[s["name"]] = responses[i]
    return results
