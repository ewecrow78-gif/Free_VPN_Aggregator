from typing import Optional
from pydantic import BaseModel, Field

# Geo mapping
FLAG_TO_ISO = {
    "🇷🇺": "RU", "🇺🇸": "US", "🇩🇪": "DE", "🇫🇷": "FR", "🇳🇱": "NL",
    "🇬🇧": "GB", "🇹🇷": "TR", "🇸🇬": "SG", "🇯🇵": "JP", "🇰🇷": "KR",
    "🇨🇳": "CN", "🇭🇰": "HK", "🇹🇼": "TW", "🇨🇦": "CA", "🇧🇷": "BR",
    "🇮🇳": "IN", "🇪🇸": "ES", "🇮🇹": "IT", "🇸🇪": "SE", "🇨🇭": "CH",
    "🇵🇱": "PL", "🇺🇦": "UA", "🇮🇷": "IR", "🇦🇪": "AE", "🇫🇮": "FI"
}
ISO_TO_FLAG = {v: k for k, v in FLAG_TO_ISO.items()}
COUNTRY_ISO_MAP = {
    "RU": "russia", "US": "usa", "DE": "germany", "FR": "france",
    "NL": "netherlands", "GB": "united-kingdom", "TR": "turkey", 
    "SG": "singapore", "JP": "japan", "KR": "south-korea",
    "CN": "china", "HK": "hong-kong", "TW": "taiwan", "CA": "canada",
    "BR": "brazil", "IN": "india", "ES": "spain", "IT": "italy",
    "SE": "sweden", "CH": "switzerland", "PL": "poland", "UA": "ukraine",
    "IR": "iran", "AE": "uae", "FI": "finland"
}

class BaseVPNConfig(BaseModel):
    raw_link: str
    protocol: str
    host: str
    port: int
    name: str = "Free_VPN"
    
    security: Optional[str] = None
    sni: Optional[str] = None
    exit_ip_verified: bool = False
    
    country_iso: str = "UN"
    country_name: str = "unknown"
    flag: str = "🏳️"
    
    latency_ms: Optional[float] = None
    jitter_std_ms: Optional[float] = None
    latency_p90_ms: Optional[float] = None
    proxy_latency_ms: Optional[float] = None
    
    # Whitelist verification
    whitelist_candidate: bool = False
    whitelist_verified: bool = False
    
    entry_latency_ms: Optional[float] = None
    entry_success_rate: float = 0.0
    
    whitelist_latency_ms: Optional[float] = None
    whitelist_p95_ms: Optional[float] = None
    whitelist_jitter_ms: Optional[float] = None
    whitelist_success_rate: float = 0.0
    
    # New validation fields
    tcp_rtt_ms: Optional[float] = None
    success_rate: float = 0.0
    download_speed_mbps: Optional[float] = None
    ru_reachable: bool = False
    dpi_bypassed: bool = False
    allow_insecure: bool = False
    
    # Stable pool history
    stability_score: float = 0.5
    ema_latency: Optional[float] = None
    ema_jitter: Optional[float] = None

    def get_fingerprint(self) -> str:
        """Returns a unique fingerprint for this config ignoring the #name part."""
        import hashlib
        core_link = self.raw_link.split("#")[0].strip().lower()
        return hashlib.sha256(core_link.encode("utf-8")).hexdigest()

    def get_score(self) -> float:
        # 0..100
        success = self.success_rate * 35.0
        stability = self.stability_score * 25.0

        p50 = self.ema_latency if self.ema_latency is not None else (self.latency_ms if self.latency_ms is not None else 2000.0)
        # экспоненциальный спад: 100ms≈20, 300ms≈10, 800ms≈2
        latency_pts = 20.0 * (0.5 ** (p50 / 300.0))

        p90 = getattr(self, "latency_p90_ms", None) or p50 * 1.5
        tail_penalty = min(10.0, max(0.0, (p90 - p50) / 50.0))

        jitter = self.ema_jitter if self.ema_jitter is not None else (self.jitter_std_ms if self.jitter_std_ms is not None else 300.0)
        jitter_penalty = min(10.0, jitter / 30.0)

        dpi_bonus = 5.0 if self.dpi_bypassed else 0.0
        speed = self.download_speed_mbps or 0.0
        speed_pts = min(10.0, speed * 2.0)  # 5 MB/s → 10

        score = success + stability + latency_pts + dpi_bonus + speed_pts
        score -= tail_penalty + jitter_penalty
        
        if self.allow_insecure:
            score -= 15.0
            
        return round(max(0.0, score), 2)

    def generate_xray_outbound(self) -> dict:
        """
        Must return a valid Xray-core outbound JSON dictionary for testing this config.
        """
        raise NotImplementedError

    def rename(self, new_name: str) -> None:
        """
        Modifies self.name and self.raw_link with the new name.
        """
        raise NotImplementedError

    def to_clash_proxy(self) -> dict:
        """
        Returns Clash YAML proxy object.
        """
        raise NotImplementedError
        
    def to_sing_box_outbound(self) -> dict:
        """
        Returns Sing-Box JSON outbound object.
        """
        raise NotImplementedError
