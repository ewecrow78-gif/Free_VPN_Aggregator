import asyncio
import json
from pathlib import Path
import sys
import os

sys.path.append(str(Path.cwd()))
from src.models.protocols import parse_link
from src.services.validator import start_xray_batch

async def main():
    scored_file = Path("data/06_scored.jsonl")
    if not scored_file.exists():
        print("No scored configs found!")
        sys.exit(1)

    best_config_link = None
    with open(scored_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                cfg = json.loads(line)
                if cfg.get("score", 0) > 0 and cfg.get("raw_link"):
                    best_config_link = cfg.get("raw_link")
                    break

    if not best_config_link:
        print("No valid proxy found in scored configs.")
        sys.exit(1)

    # parse the link
    proxy_obj = parse_link(best_config_link)
    if not proxy_obj:
        print("Failed to parse best config.")
        sys.exit(1)
        
    process, conf_path = await start_xray_batch([proxy_obj], 999)
    if not process:
        print("Failed to start Xray batch.")
        sys.exit(1)
        
    print(f"XRAY_PID={process.pid}")
    
if __name__ == "__main__":
    asyncio.run(main())
