import base64
import json
import urllib.parse
from typing import Optional, List, Dict, Tuple
from src.models.base import BaseVPNConfig


def safe_b64decode(s: str) -> bytes:
    # Add padding if necessary
    s = s.strip()
    s += "=" * (-len(s) % 4)
    # Some configs use urlsafe, some use standard
    try:
        return base64.b64decode(s)
    except:
        return base64.urlsafe_b64decode(s)

class VmessConfig(BaseVPNConfig):
    uuid: str = ""
    alterId: int = 0
    cipher: str = ""
    network: str = ""
    tls: str = ""
    sni: str = ""
    path: str = ""
    host_header: str = ""
    
    @classmethod
    def from_url(cls, url: str):
        payload = url[len("vmess://"):]
        try:
            data = json.loads(safe_b64decode(payload).decode("utf-8"))
        except:
            return None
            
        net = str(data.get("net", "tcp") or "")
        if net == "raw" or not net:
            net = "tcp"
            
        return cls(
            raw_link=url,
            protocol="vmess",
            host=data.get("add", ""),
            port=int(data.get("port", 0)),
            name=data.get("ps", "Free_VPN"),
            uuid=data.get("id", ""),
            alterId=int(data.get("aid", 0)),
            cipher=str(data.get("scy", "auto") or ""),
            network=net,
            tls=str(data.get("tls", "") or ""),
            sni=str(data.get("sni", "") or ""),
            path=str(data.get("path", "") or ""),
            host_header=str(data.get("host", "") or "")
        )


    def generate_xray_outbound(self) -> dict:
        outbound = {
            "protocol": "vmess",
            "settings": {
                "vnext": [{
                    "address": self.host,
                    "port": self.port,
                    "users": [{"id": self.uuid, "alterId": self.alterId, "security": self.cipher}]
                }]
            },
            "streamSettings": {
                "network": self.network
            }
        }
        if self.network == "ws":
            outbound["streamSettings"]["wsSettings"] = {"path": self.path}
            if self.host_header:
                outbound["streamSettings"]["wsSettings"]["headers"] = {"Host": self.host_header}
        if self.tls in ["tls", "reality"]:
            outbound["streamSettings"]["security"] = "tls"
            outbound["streamSettings"]["tlsSettings"] = {
                "serverName": self.sni or self.host,
                "allowInsecure": True
            }
        return outbound

    def rename(self, new_name: str) -> None:
        self.name = new_name
        try:
            payload = self.raw_link[len("vmess://"):]
            data = json.loads(safe_b64decode(payload).decode("utf-8"))
            data["ps"] = new_name
            clean_keys = {"v", "ps", "add", "port", "id", "aid", "net", "type", "host", "path", "tls", "sni", "alpn", "scy"}
            data = {k: v for k, v in data.items() if k in clean_keys}
            new_json = json.dumps(data, separators=(",", ":")).encode("utf-8")
            self.raw_link = "vmess://" + base64.b64encode(new_json).decode("utf-8")
        except: pass

    def to_clash_proxy(self) -> dict:
        return {
            "name": self.name, "type": "vmess", "server": self.host, "port": self.port,
            "uuid": self.uuid, "alterId": self.alterId, "cipher": self.cipher,
            "network": self.network, "tls": (self.tls == "tls"),
            "servername": self.sni or self.host,
            "ws-opts": {"path": self.path, "headers": {"Host": self.host_header}} if self.network == "ws" else {}
        }
        
    def to_sing_box_outbound(self) -> dict:
        o = {
            "type": "vmess", "tag": self.name, "server": self.host, "server_port": self.port,
            "uuid": self.uuid, "security": self.cipher, "alter_id": self.alterId
        }
        if self.tls:
            o["tls"] = {"enabled": True, "server_name": self.sni or self.host, "insecure": True}
        if self.network == "ws":
            o["transport"] = {"type": "ws", "path": self.path}
        return o

class VlessConfig(BaseVPNConfig):
    uuid: str = ""
    network: str = ""
    security: str = ""
    sni: str = ""
    flow: str = ""
    pbk: str = ""
    sid: str = ""
    path: str = ""

    
    @classmethod
    def from_url(cls, url: str):
        try:
            parsed = urllib.parse.urlparse(url)
            host = parsed.hostname
            port = parsed.port
            uuid = parsed.username
            qs = urllib.parse.parse_qs(parsed.query)
            name = urllib.parse.unquote(parsed.fragment) if parsed.fragment else "Free_VPN"
            net = qs.get("type", ["tcp"])[0]
            if net == "raw" or not net:
                net = "tcp"
            return cls(
                raw_link=url, protocol="vless", host=host, port=port, name=name, uuid=uuid,
                network=net,
                security=qs.get("security", [""])[0],
                sni=qs.get("sni", [""])[0],
                flow=qs.get("flow", [""])[0],
                pbk=qs.get("pbk", [""])[0],
                sid=qs.get("sid", [""])[0],
                path=qs.get("path", [""])[0],
                allow_insecure=(qs.get("allowInsecure", ["0"])[0] in ["1", "true"])
            )
        except: return None

    def generate_xray_outbound(self) -> dict:
        outbound = {
            "protocol": "vless",
            "settings": {
                "vnext": [{
                    "address": self.host, "port": self.port,
                    "users": [{"id": self.uuid, "encryption": "none", "flow": self.flow}]
                }]
            },
            "streamSettings": {"network": self.network}
        }
        if self.network == "ws":
            outbound["streamSettings"]["wsSettings"] = {"path": self.path}
        if self.security == "tls":
            outbound["streamSettings"]["security"] = "tls"
            outbound["streamSettings"]["tlsSettings"] = {"serverName": self.sni or self.host, "allowInsecure": True}
        elif self.security == "reality":
            outbound["streamSettings"]["security"] = "reality"
            outbound["streamSettings"]["realitySettings"] = {
                "serverName": self.sni or self.host, "publicKey": self.pbk, "shortId": self.sid, "fingerprint": "chrome"
            }
        return outbound

    def rename(self, new_name: str) -> None:
        self.name = new_name
        base = self.raw_link.split("#")[0]
        self.raw_link = f"{base}#{urllib.parse.quote(new_name)}"

    def to_clash_proxy(self) -> dict:
        return {
            "name": self.name, "type": "vless", "server": self.host, "port": self.port,
            "uuid": self.uuid, "network": self.network, "tls": (self.security in ["tls", "reality"]),
            "servername": self.sni or self.host,
            "ws-opts": {"path": self.path} if self.network == "ws" else {},
            "reality-opts": {"public-key": self.pbk, "short-id": self.sid} if self.security == "reality" else {}
        }
        
    def to_sing_box_outbound(self) -> dict:
        o = {
            "type": "vless", "tag": self.name, "server": self.host, "server_port": self.port,
            "uuid": self.uuid, "flow": self.flow if self.flow else ""
        }
        if self.security:
            o["tls"] = {"enabled": True, "server_name": self.sni or self.host, "insecure": True}
            if self.security == "reality":
                o["tls"]["reality"] = {"enabled": True, "public_key": self.pbk, "short_id": self.sid}
        if self.network == "ws":
            o["transport"] = {"type": "ws", "path": self.path}
        return o

class TrojanConfig(BaseVPNConfig):
    password: str = ""
    network: str = ""
    sni: str = ""

    
    @classmethod
    def from_url(cls, url: str):
        try:
            parsed = urllib.parse.urlparse(url)
            host = parsed.hostname
            port = parsed.port
            password = parsed.username
            qs = urllib.parse.parse_qs(parsed.query)
            name = urllib.parse.unquote(parsed.fragment) if parsed.fragment else "Free_VPN"
            net = qs.get("type", ["tcp"])[0]
            if net == "raw" or not net:
                net = "tcp"
            return cls(
                raw_link=url, protocol="trojan", host=host, port=port, name=name, password=password,
                network=net,
                sni=qs.get("sni", [""])[0],
                allow_insecure=(qs.get("allowInsecure", ["0"])[0] in ["1", "true"])
            )
        except: return None

    def generate_xray_outbound(self) -> dict:
        return {
            "protocol": "trojan",
            "settings": {"servers": [{"address": self.host, "port": self.port, "password": self.password}]},
            "streamSettings": {
                "network": self.network, "security": "tls",
                "tlsSettings": {"serverName": self.sni or self.host, "allowInsecure": True}
            }
        }

    def rename(self, new_name: str) -> None:
        self.name = new_name
        base = self.raw_link.split("#")[0]
        self.raw_link = f"{base}#{urllib.parse.quote(new_name)}"

    def to_clash_proxy(self) -> dict:
        return {
            "name": self.name, "type": "trojan", "server": self.host, "port": self.port,
            "password": self.password, "sni": self.sni or self.host, "skip-cert-verify": True
        }
        
    def to_sing_box_outbound(self) -> dict:
        return {
            "type": "trojan", "tag": self.name, "server": self.host, "server_port": self.port,
            "password": self.password,
            "tls": {"enabled": True, "server_name": self.sni or self.host, "insecure": True}
        }

class SSConfig(BaseVPNConfig):
    method: str = ""
    password: str = ""

    
    @classmethod
    def from_url(cls, url: str):
        try:
            parsed = urllib.parse.urlparse(url)
            name = urllib.parse.unquote(parsed.fragment) if parsed.fragment else "Free_VPN"
            if "@" in parsed.netloc:
                cred, hostport = parsed.netloc.split("@")
                method_pass = safe_b64decode(cred).decode("utf-8")
                method, password = method_pass.split(":", 1)
                host, port = hostport.split(":")
                port = int(port)
            else:
                payload = safe_b64decode(parsed.netloc).decode("utf-8")
                method, pw_host_port = payload.split(":", 1)
                password, host_port = pw_host_port.split("@")
                host, port = host_port.split(":")
                port = int(port)
            return cls(
                raw_link=url, protocol="ss", host=host, port=port, name=name,
                method=method, password=password
            )
        except: return None

    def generate_xray_outbound(self) -> dict:
        return {
            "protocol": "shadowsocks",
            "settings": {"servers": [{"address": self.host, "port": self.port, "method": self.method, "password": self.password}]}
        }

    def rename(self, new_name: str) -> None:
        self.name = new_name
        base = self.raw_link.split("#")[0]
        self.raw_link = f"{base}#{urllib.parse.quote(new_name)}"

    def to_clash_proxy(self) -> dict:
        return {
            "name": self.name, "type": "ss", "server": self.host, "port": self.port,
            "cipher": self.method, "password": self.password
        }
        
    def to_sing_box_outbound(self) -> dict:
        return {
            "type": "shadowsocks", "tag": self.name, "server": self.host, "server_port": self.port,
            "method": self.method, "password": self.password
        }

def parse_link(link: str) -> Optional[BaseVPNConfig]:
    lower = link.lower().strip()
    if lower.startswith("vmess://"):
        return VmessConfig.from_url(link)
    elif lower.startswith("vless://"):
        return VlessConfig.from_url(link)
    elif lower.startswith("trojan://"):
        return TrojanConfig.from_url(link)
    elif lower.startswith("ss://"):
        return SSConfig.from_url(link)
    return None
