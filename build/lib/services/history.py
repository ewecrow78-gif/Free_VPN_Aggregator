import json
import os
import time
from typing import Dict, Any
from src.config import DATA_DIR
from src.utils import logger

HISTORY_FILE = DATA_DIR / "history.json"

class HistoryManager:
    def __init__(self):
        self.history: Dict[str, Dict[str, Any]] = {}
        self.load()

    def load(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    self.history = json.load(f)
                logger.info(f"[History] Loaded {len(self.history)} records from history.")
            except Exception as e:
                logger.error(f"[History] Failed to load history: {e}")

    def save(self):
        os.makedirs(HISTORY_FILE.parent, exist_ok=True)
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=2)
            logger.info(f"[History] Saved {len(self.history)} records to history.")
        except Exception as e:
            logger.error(f"[History] Failed to save history: {e}")

    def get_record(self, fingerprint: str) -> dict:
        return self.history.get(fingerprint, {
            "total_successes": 0,
            "total_failures": 0,
            "consecutive_failures": 0,
            "availability_ema": 0.5,
            "last_failure_reason": None,
            "blocked_until": 0,
            "recent_results": [],
            "ema_latency": None,
            "ema_jitter": None,
            "last_latency": None
        })

    def update_record(self, fingerprint: str, success: bool, latency: float = None, jitter: float = None, failure_reason: str = None):
        rec = self.get_record(fingerprint)
        alpha = 0.25
        sample = 1.0 if success else 0.0
        old_availability = rec.get("availability_ema", 0.5)
        rec["availability_ema"] = alpha * sample + (1 - alpha) * old_availability
        
        # update recent results
        recent = rec.get("recent_results", [])
        recent.append(success)
        rec["recent_results"] = recent[-4:]
        
        if success:
            rec["total_successes"] = rec.get("total_successes", 0) + 1
            rec["consecutive_failures"] = 0
            rec["last_success"] = time.time()
            rec["blocked_until"] = 0
            
            l_alpha = 0.3
            if latency is not None:
                rec["last_latency"] = latency
                old_lat = rec.get("ema_latency")
                rec["ema_latency"] = latency if old_lat is None else l_alpha * latency + (1 - l_alpha) * old_lat
            
            if jitter is not None:
                old_jit = rec.get("ema_jitter")
                rec["ema_jitter"] = jitter if old_jit is None else l_alpha * jitter + (1 - l_alpha) * old_jit
        else:
            rec["total_failures"] = rec.get("total_failures", 0) + 1
            rec["consecutive_failures"] = rec.get("consecutive_failures", 0) + 1
            rec["last_failure_reason"] = failure_reason
            
            fails = rec["consecutive_failures"]
            if fails == 2:
                rec["blocked_until"] = time.time() + 2 * 3600
            elif fails == 3:
                rec["blocked_until"] = time.time() + 6 * 3600
            elif fails == 4:
                rec["blocked_until"] = time.time() + 12 * 3600
            elif fails >= 5:
                rec["blocked_until"] = time.time() + 24 * 3600

        self.history[fingerprint] = rec

    def is_quarantined(self, fingerprint: str) -> bool:
        rec = self.history.get(fingerprint, {})
        return rec.get("blocked_until", 0) > time.time()

    def clean_dead_records(self, max_fails: int = 3):
        pass

    def get_stability_score(self, fingerprint: str) -> float:
        """Returns a stability score from 0.0 to 1.0 based on history EMA."""
        rec = self.history.get(fingerprint)
        if not rec:
            return 0.5  # Neutral for new configs
        return float(rec.get("availability_ema", 0.5))
