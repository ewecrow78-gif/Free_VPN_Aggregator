import os
import sys
import platform
import asyncio
import urllib.request
from src.utils import logger

HAPP_REPO = "amurcanov/happ-decrypt-universal"
HAPP_VERSION = "v1.0.0"

def get_binary_name():
    system = platform.system().lower()
    if system == "windows":
        return "windows-x64_x86.exe"
    elif system == "linux":
        return "linux-x64_x86"
    else:
        # Fallback or unhandled
        return None

async def download_happ_binary(dest_path: str):
    if os.path.exists(dest_path):
        return True

    bin_name = get_binary_name()
    if not bin_name:
        logger.warning("[Happ] Unsupported OS for happ-decrypt-universal")
        return False

    url = f"https://github.com/{HAPP_REPO}/releases/download/{HAPP_VERSION}/{bin_name}"
    logger.info(f"[Happ] Downloading {bin_name} from {url}")
    
    try:
        urllib.request.urlretrieve(url, dest_path)
        if platform.system().lower() != "windows":
            os.chmod(dest_path, 0o755)
        return True
    except Exception as e:
        logger.error(f"[Happ] Failed to download binary: {e}")
        return False

async def decrypt_happ(link: str) -> str:
    """
    Returns the decrypted string if successful, else None.
    """
    if not link.startswith("happ://"):
        return None

    bin_name = "happ.exe" if platform.system().lower() == "windows" else "happ"
    dest_path = os.path.join("core", bin_name)
    
    os.makedirs("core", exist_ok=True)
    if not await download_happ_binary(dest_path):
        return None

    try:
        proc = await asyncio.create_subprocess_exec(
            dest_path, link,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        out = stdout.decode("utf-8", errors="ignore")
        
        if proc.returncode == 0 and "Result" in out:
            # Parse output
            lines = out.split("\n")
            result_idx = -1
            for i, line in enumerate(lines):
                if line.strip() == "Result":
                    result_idx = i
                    break
            
            if result_idx != -1 and result_idx + 1 < len(lines):
                decrypted = lines[result_idx + 1].strip()
                return decrypted
        else:
            logger.debug(f"[Happ] Failed to decrypt {link}: {stderr.decode('utf-8', errors='ignore')}")
            
    except Exception as e:
        logger.error(f"[Happ] Decryption process error: {e}")

    return None
