import asyncio
import os
import re
import aiohttp
from typing import List, Set
from telethon import TelegramClient
from telethon.sessions import StringSession
from src.models import ROOT
from utils import logger, decode_maybe_base64

TG_CHANNELS_FILE = ROOT / "tg_channels.txt"
URLS_FILE = ROOT / "urls.txt"

API_ID = os.getenv("TG_API_ID")
API_HASH = os.getenv("TG_API_HASH")
SESSION_STR = os.getenv("TG_SESSION")

# Strict regex for parsing VPN config URLs
CONFIG_RE = re.compile(
    r"(vmess://[a-zA-Z0-9+/=_-]+|vless://[^\s#]+(?:#[^\s]*)?|trojan://[^\s#]+(?:#[^\s]*)?|ss://[^\s#]+(?:#[^\s]*)?)", 
    re.IGNORECASE
)

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

async def fetch_subscription_url(session: aiohttp.ClientSession, url: str) -> List[str]:
    configs = []
    logger.info(f"[Scraper] Fetching URL: {url}")
    try:
        async with session.get(url, timeout=12) as response:
            if response.status == 200:
                raw = await response.read()
                text = decode_maybe_base64(raw)
                matches = CONFIG_RE.findall(text)
                configs.extend([m.strip() for m in matches if m.strip()])
                logger.info(f"[Scraper] Found {len(matches)} configs from {url}")
            else:
                logger.warning(f"[Scraper] URL {url} returned HTTP {response.status}")
    except Exception as e:
        logger.error(f"[Scraper] Failed to fetch {url}: {e}")
    return configs

async def fetch_telegram_channels() -> List[str]:
    configs = []
    if not API_ID or not API_HASH or not SESSION_STR:
        logger.warning("[Scraper] Telegram credentials not configured. Skipping Telethon scraper.")
        return configs

    channels = load_sources(TG_CHANNELS_FILE)
    if not channels:
        logger.info("[Scraper] No Telegram channels listed in tg_channels.txt")
        return configs

    logger.info("[Scraper] Starting Telethon connection...")
    try:
        client = TelegramClient(StringSession(SESSION_STR), int(API_ID), API_HASH)
        await client.connect()
        if not await client.is_user_authorized():
            logger.error("[Scraper] Telethon session is unauthorized! Update TG_SESSION secret.")
            return configs

        for channel in channels:
            logger.info(f"[Scraper] Scraping channel: {channel}")
            try:
                # Scrape up to 150 messages for maximum coverage of configs
                async for message in client.iter_messages(channel, limit=150):
                    if message.message:
                        matches = CONFIG_RE.findall(message.message)
                        configs.extend([m.strip() for m in matches if m.strip()])
                    
                    if message.document and message.file and message.file.name and message.file.name.endswith('.txt'):
                        try:
                            file_bytes = await client.download_media(message.document, bytes)
                            if file_bytes:
                                text = decode_maybe_base64(file_bytes)
                                matches = CONFIG_RE.findall(text)
                                configs.extend([m.strip() for m in matches if m.strip()])
                                logger.info(f"[Scraper] Found {len(matches)} configs from {message.file.name} in {channel}")
                        except Exception as doc_err:
                            logger.error(f"[Scraper] Error processing document {message.file.name} in {channel}: {doc_err}")
            except Exception as channel_err:
                logger.error(f"[Scraper] Channel {channel} scrape failed: {channel_err}")
        
        await client.disconnect()
    except Exception as e:
        logger.error(f"[Scraper] Telegram scraper error: {e}")
    
    return configs

async def scrape_all_sources() -> List[str]:
    all_raw = []
    
    # 1. Fetch URLs
    urls = load_sources(URLS_FILE)
    if urls:
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_subscription_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            for res in results:
                all_raw.extend(res)

    # 2. Fetch Telegram Channels
    tg_raw = await fetch_telegram_channels()
    all_raw.extend(tg_raw)

    # Dedup raw strings
    unique = list(dict.fromkeys(all_raw))
    logger.info(f"[Scraper] Completed. Total unique raw configurations: {len(unique)}")
    return unique
