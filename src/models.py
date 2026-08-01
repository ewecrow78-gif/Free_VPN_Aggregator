import base64
import json
import re
import urllib.parse
from pathlib import Path
from typing import Dict, Optional, Tuple
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent

# Country Mappings & Flags
COUNTRY_ISO_MAP = {
    "RU": "russia", "US": "usa", "DE": "germany", "FR": "france",
    "NL": "netherlands", "GB": "united-kingdom", "UK": "united-kingdom",
    "TR": "turkey", "SG": "singapore", "JP": "japan", "KR": "south-korea",
    "CN": "china", "HK": "hong-kong", "TW": "taiwan", "CA": "canada",
    "BR": "brazil", "IN": "india", "ES": "spain", "IT": "italy",
    "SE": "sweden", "CH": "switzerland", "PL": "poland", "UA": "ukraine",
    "IR": "iran", "AE": "uae", "FI": "finland"
}

FLAG_TO_ISO = {
    "🇷🇺": "RU", "🇺🇸": "US", "🇩🇪": "DE", "🇫🇷": "FR", "🇳🇱": "NL",
    "🇬🇧": "GB", "🇹🇷": "TR", "🇸🇬": "SG", "🇯🇵": "JP", "🇰🇷": "KR",
    "🇨🇳": "CN", "🇭🇰": "HK", "🇹🇼": "TW", "🇨🇦": "CA", "🇧🇷": "BR",
    "🇮🇳": "IN", "🇪🇸": "ES", "🇮🇹": "IT", "🇸🇪": "SE", "🇨🇭": "CH",
    "🇵🇱": "PL", "🇺🇦": "UA", "🇮🇷": "IR", "🇦🇪": "AE", "🇫🇮": "FI"
}

ISO_TO_FLAG = {v: k for k, v in FLAG_TO_ISO.items()}

class VPNConfig(BaseModel):
    protocol: str
    raw: str
    host: str
    port: int
    country_iso: str = "UN"
    country_name: str = "unknown"
    flag: str = "🏳️"
    name: str = "Free_VPN"
    latency_ms: Optional[float] = None
    is_whitelist: bool = False

    @classmethod
    def parse_raw_link(cls, link: str, geo_cache: Dict[str, Tuple[str, str]] = None) -> Optional["VPNConfig"]:
        link = link.strip()
        lower_link = link.lower()
        
        protocol = None
        for proto in ["vmess://", "vless://", "trojan://", "ss://"]:
            if lower_link.startswith(proto):
                protocol = proto[:-3]
                break
        
        if not protocol:
            return None

        # Extract host & port
        host, port = "", 0
        if protocol == "vmess":
            try:
                payload = link[len("vmess://"):]
                # Fix padding
                payload += "=" * (-len(payload) % 4)
                data = json.loads(base64.b64decode(payload).decode("utf-8"))
                host = data.get("add", "")
                port = int(data.get("port", 0))
            except Exception:
                return None
        else:
            try:
                parsed = urllib.parse.urlparse(link)
                host = parsed.hostname or ""
                port = parsed.port or 0
            except Exception:
                return None

        if not host or not port:
            return None

        # Determine Flag/Country ISO from raw name / fragment
        flag = "🏳️"
        iso = "UN"
        
        # Check if name contains flag
        raw_name = ""
        if protocol == "vmess":
            try:
                raw_name = data.get("ps", "")
            except: pass
        elif "#" in link:
            raw_name = urllib.parse.unquote(link.split("#")[-1])

        # Extract flag from name
        for f, i in FLAG_TO_ISO.items():
            if f in raw_name:
                flag = f
                iso = i
                break
        
        # Heuristic country names in fragment name
        if iso == "UN" and raw_name:
            low_name = raw_name.lower()
            if "russia" in low_name or " ru " in low_name or "_ru" in low_name:
                iso, flag = "RU", "🇷🇺"
            elif "germany" in low_name or "de" in low_name:
                iso, flag = "DE", "🇩🇪"
            elif "usa" in low_name or "us" in low_name:
                iso, flag = "US", "🇺🇸"

        # Lookup IP/GeoIP if country remains unknown
        if iso == "UN" and geo_cache is not None:
            # Resolving IP (done outside or here)
            try:
                ip = socket.gethostbyname(host) if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host) else host
                if ip in geo_cache:
                    iso, c_name = geo_cache[ip]
                else:
                    # Sync Lookup as fallback
                    url = f"http://ip-api.com/json/{ip}?fields=status,countryCode"
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=3) as resp:
                        res_data = json.loads(resp.read().decode("utf-8"))
                        if res_data.get("status") == "success":
                            iso = res_data.get("countryCode", "UN")
                    c_name = COUNTRY_ISO_MAP.get(iso, "unknown")
                    geo_cache[ip] = (iso, c_name)
                flag = ISO_TO_FLAG.get(iso, "🏳️")
            except:
                pass

        country_name = COUNTRY_ISO_MAP.get(iso, "unknown")

        return cls(
            protocol=protocol,
            raw=link,
            host=host,
            port=port,
            country_iso=iso,
            country_name=country_name,
            flag=flag
        )

    def rename_with_index(self, index: int) -> None:
        new_name = f"{self.flag} Free_VPN №{index}"
        self.name = new_name
        
        if self.protocol == "vmess":
            try:
                payload = self.raw[len("vmess://"):]
                payload += "=" * (-len(payload) % 4)
                obj = json.loads(base64.b64decode(payload).decode("utf-8"))
                obj["ps"] = new_name
                new_json = json.dumps(obj, separators=(",", ":")).encode("utf-8")
                self.raw = "vmess://" + base64.b64encode(new_json).decode("utf-8")
            except:
                pass
        else:
            try:
                base_part = self.raw.split("#")[0]
                self.raw = f"{base_part}#{urllib.parse.quote(new_name)}"
            except:
                pass
