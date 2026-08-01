from src.utils import decode_maybe_base64, is_base64_data
import base64

def test_is_base64_data():
    valid = base64.b64encode(b"vless://abc").decode("utf-8")
    assert is_base64_data(valid) is True
    assert is_base64_data("not base64 data at all") is False

def test_decode_maybe_base64():
    valid = base64.b64encode(b"vless://abc").decode("utf-8")
    assert decode_maybe_base64(valid) == "vless://abc"
    assert decode_maybe_base64("vless://abc") == "vless://abc"
