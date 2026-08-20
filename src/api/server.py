from fastapi import FastAPI, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
import json
from src.config import DATA_DIR
from src.models.config import Config
from src.utils import logger
import sqlite3

app = FastAPI(title="Free_VPN_Aggregator Tester API")

class TestResult(BaseModel):
    fingerprint: str
    success: bool
    latency_ms: Optional[float] = None
    jitter_ms: Optional[float] = None
    download_mbps: Optional[float] = None
    error: Optional[str] = None

class BatchResults(BaseModel):
    tester_id: str
    results: List[TestResult]

@app.get("/api/v1/tester/batch")
async def get_batch(limit: int = 20):
    """
    Returns a batch of whitelist candidates for the Android tester.
    Reads from the latest 04_handshake_ok.jsonl or 05_http_ok.jsonl
    """
    candidates = []
    file_path = DATA_DIR / "04_handshake_ok.jsonl"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="No candidates available yet")
        
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            cfg_dict = json.loads(line)
            # Only send those marked as whitelist_candidate
            if cfg_dict.get("whitelist_candidate", False):
                candidates.append(cfg_dict)
                if len(candidates) >= limit:
                    break
                    
    return {"batch": candidates}

@app.post("/api/v1/tester/results")
async def post_results(data: BatchResults, background_tasks: BackgroundTasks):
    """
    Receives test results from Android application and updates the SQLite DB.
    Also pushes to the GitHub Results repository.
    """
    logger.info(f"[API] Received {len(data.results)} results from tester {data.tester_id}")
    
    # We should update a SQLite DB or a JSON log for the main pipeline to consume
    results_file = DATA_DIR / "tester_results.jsonl"
    with open(results_file, "a", encoding="utf-8") as f:
        for r in data.results:
            row = r.model_dump()
            row["tester_id"] = data.tester_id
            f.write(json.dumps(row) + "\n")
            
    # Also write to the github repo and push
    import os
    import subprocess
    repo_dir = "/home/qbert/.gemini/antigravity/scratch/Free_VPN_Aggregator_Results"
    if os.path.exists(repo_dir):
        github_file = os.path.join(repo_dir, "android_tester_results.jsonl")
        with open(github_file, "a", encoding="utf-8") as f:
            for r in data.results:
                row = r.model_dump()
                row["tester_id"] = data.tester_id
                f.write(json.dumps(row) + "\n")
                
        def commit_and_push():
            try:
                subprocess.run(["git", "add", "android_tester_results.jsonl"], cwd=repo_dir, check=True)
                subprocess.run(["git", "commit", "-m", f"Automated test results from {data.tester_id}"], cwd=repo_dir, check=True)
                subprocess.run(["git", "push"], cwd=repo_dir, check=True)
                logger.info("[API] Successfully pushed results to GitHub")
            except Exception as e:
                logger.error(f"[API] Failed to push to GitHub: {e}")
                
        background_tasks.add_task(commit_and_push)
            
    return {"status": "ok", "processed": len(data.results)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
