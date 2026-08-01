import os
import qrcode
from PIL import Image
from src.config import ROOT_DIR
from src.utils import logger

def generate_qr_code(url: str, filename: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    full_path = ROOT_DIR / "configs" / "qr" / filename
    os.makedirs(full_path.parent, exist_ok=True)
    
    img.save(full_path)

def generate_all_qrs() -> None:
    logger.info("[QR] Generating QR codes for subscriptions...")
    base_url = "https://raw.githubusercontent.com/ewecrow78-gif/Free_VPN_Aggregator/output/base64/"
    
    subs = [
        ("recommended.txt", "recommended.png"),
        ("mobile.txt", "mobile.png"),
        ("top_fast.txt", "top_fast.png"),
        ("ru_mobile_whitelist.txt", "ru_mobile_whitelist.png"),
        ("whitelist_all.txt", "whitelist_all.png"),
        ("sni_cidr_bypass.txt", "sni_cidr_bypass.png"),
        ("top_150_mobile.txt", "top_150_mobile.png")
    ]
    
    for sub_file, qr_file in subs:
        url = base_url + sub_file
        try:
            generate_qr_code(url, qr_file)
        except Exception as e:
            logger.error(f"[QR] Failed to generate {qr_file}: {e}")
            
    logger.info("[QR] QR codes generated successfully.")
