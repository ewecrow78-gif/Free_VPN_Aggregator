import os
from pathlib import Path

# Project Roots
ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"
CONFIGS_DIR = ROOT_DIR / "configs"
CORE_DIR = ROOT_DIR / "core"
DATA_DIR = ROOT_DIR / "data"

# Files
TG_CHANNELS_FILE = ROOT_DIR / "tg_channels.txt"
TG_FORUMS_FILE = ROOT_DIR / "tg_forums.txt"
URLS_FILE = ROOT_DIR / "urls.txt"
STATS_FILE = CONFIGS_DIR / "stats.json"
README_TEMPLATE = ROOT_DIR / "README.template.md"
README_FILE = ROOT_DIR / "README.md"
BLOCKLIST_FILE = ROOT_DIR / "ru_blocklist.txt"

# Xray Settings
XRAY_VERSION = "1.8.24"
XRAY_URL_WIN = f"https://github.com/XTLS/Xray-core/releases/download/v{XRAY_VERSION}/Xray-windows-64.zip"
XRAY_URL_LINUX = f"https://github.com/XTLS/Xray-core/releases/download/v{XRAY_VERSION}/Xray-linux-64.zip"
XRAY_FALLBACK_PORT_START = 10000

# Telegram
TG_API_ID = os.getenv("TG_API_ID")
TG_API_HASH = os.getenv("TG_API_HASH")
TG_SESSION = os.getenv("TG_SESSION")

# Validation Settings
TEST_TIMEOUT = 5.0 # seconds for xray to connect and fetch
MAX_CONCURRENT_CHECKS = 100 # How many Xray instances to spawn simultaneously

# Ping validation
TEST_TIMEOUT = 5.0
PING_ATTEMPTS = 8
PING_WARMUP_ATTEMPTS = 1

# Validation Thresholds
MAX_LATENCY_HARD_MS = 1200.0
MAX_LATENCY_P50_MS = 450.0
MAX_LATENCY_P90_MS = 1800.0
MAX_JITTER_MS = 180.0
MIN_SUCCESS_RATE = 0.75
FAST_MAX_LATENCY_MS = 350.0
FAST_MAX_JITTER_MS = 80.0
FAST_MIN_SUCCESS_RATE = 0.90

PING_ENDPOINTS = [
    "https://cp.cloudflare.com/generate_204",
    "https://www.gstatic.com/generate_204",
    "https://www.google.com/generate_204",
]
TEST_URL = PING_ENDPOINTS[0]

# Antifilter
ANTIFILTER_URL = "https://antifilter.download/list/ip.txt"
