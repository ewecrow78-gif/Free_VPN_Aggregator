import asyncio
import os
import platform
import zipfile
import aiohttp
from pathlib import Path
from src.config import CORE_DIR, XRAY_VERSION
from src.utils import logger


def get_xray_binary_path() -> Path:
    ext = ".exe" if platform.system().lower() == "windows" else ""
    return CORE_DIR / f"xray{ext}"

async def download_xray():
    bin_path = get_xray_binary_path()
    if bin_path.exists():
        return

    os.makedirs(CORE_DIR, exist_ok=True)
    sys_os = platform.system().lower()
    
    if sys_os == "windows":
        archive_name = "Xray-windows-64.zip"
    elif sys_os == "linux":
        arch = platform.machine().lower()
        if "aarch64" in arch or "arm64" in arch:
            archive_name = "Xray-linux-arm64-v8a.zip"
        else:
            archive_name = "Xray-linux-64.zip"
    elif sys_os == "darwin":
        archive_name = "Xray-macos-64.zip"
    else:
        raise Exception(f"Unsupported OS for automatic Xray download: {sys_os}")

    url = f"https://github.com/XTLS/Xray-core/releases/download/v{XRAY_VERSION}/{archive_name}"
    zip_path = CORE_DIR / archive_name

    logger.info(f"[XrayManager] Downloading Xray-core {XRAY_VERSION} from {url}...")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise Exception(f"Failed to download Xray-core: HTTP {resp.status}")
            with open(zip_path, "wb") as f:
                f.write(await resp.read())

    logger.info("[XrayManager] Extracting Xray-core...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(CORE_DIR)
    
    zip_path.unlink()
    
    if sys_os != "windows":
        os.chmod(bin_path, 0o755)
        
    logger.info("[XrayManager] Xray-core is ready.")
