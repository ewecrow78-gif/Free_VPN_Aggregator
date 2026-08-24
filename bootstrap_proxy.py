import asyncio
import json
import os
import sys
from pathlib import Path

sys.path.append(str(Path.cwd()))
from src.models.protocols import parse_link
from src.services.validator import start_xray_batch
from src.services.xray_manager import download_xray

async def test_proxy(port):
    print(f"Testing proxy on port {port}...")
    try:
        proc = await asyncio.create_subprocess_shell(
            f"curl -s -x socks5h://127.0.0.1:{port} -m 10 https://api.telegram.org",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if b"ok" in stdout or b"error_code" in stdout or proc.returncode == 0:
            return True
        print(f"Test failed with returncode {proc.returncode}: {stderr.decode()}")
        return False
    except Exception as e:
        print(f"Test exception: {e}")
        return False

async def main():
    await download_xray()
    scored_file = Path("data/06_scored.jsonl")
    if not scored_file.exists():
        print("No scored configs found!")
        sys.exit(1)

    configs = []
    with open(scored_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                cfg = json.loads(line)
                if cfg.get("score", 0) > 0 and cfg.get("raw_link"):
                    configs.append(cfg.get("raw_link"))

    if not configs:
        print("No valid proxy found in scored configs.")
        sys.exit(1)

    for link in configs:
        proxy_obj = parse_link(link)
        if not proxy_obj:
            continue
            
        print(f"Trying config: {proxy_obj.name}")
        process, conf_path = await start_xray_batch([proxy_obj], 0)
        if not process:
            print("Failed to start Xray batch for this config.")
            continue
            
        await asyncio.sleep(2) # Wait for Xray to start
        
        # Check if process is still running
        if process.returncode is not None:
            print(f"Xray process died early with code {process.returncode}")
            continue

        is_working = await test_proxy(10000)
        if is_working:
            print(f"XRAY_PID={process.pid}")
            sys.exit(0)
        else:
            print(f"Proxy failed test. Killing Xray {process.pid}")
            try:
                process.kill()
            except ProcessLookupError:
                pass
            await process.wait()

    print("All scored configs failed.")
    sys.exit(1)
    
if __name__ == "__main__":
    asyncio.run(main())
