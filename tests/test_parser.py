from src.models.protocols import VlessConfig, TrojanConfig

def test_vless_parsing():
    url = "vless://00000000-0000-0000-0000-000000000000@192.168.1.1:443?type=tcp&security=tls#Free_VPN"
    config = VlessConfig.from_url(url)
    assert config is not None
    assert config.protocol == "vless"
    assert config.host == "192.168.1.1"
    assert config.port == 443
    assert config.uuid == "00000000-0000-0000-0000-000000000000"
    assert config.network == "tcp"
    assert config.security == "tls"
    assert config.name == "Free_VPN"

def test_trojan_parsing():
    url = "trojan://mypassword@example.com:8443?type=ws&sni=example.com#Trojan_VPN"
    config = TrojanConfig.from_url(url)
    assert config is not None
    assert config.protocol == "trojan"
    assert config.host == "example.com"
    assert config.port == 8443
    assert config.password == "mypassword"
    assert config.network == "ws"
    assert config.sni == "example.com"
    assert config.name == "Trojan_VPN"
