import asyncio
import random

# Danh sách 500 "Agent" ảo (Mỗi con là một thông điệp khác nhau để tránh bị Telegram quét)
AGENTS_MESSAGES = [
    f"New USDT Flash Tool 2026 leaked! Check here: https://github.com/npcanhthanh/USDT-Flash-TRC20-Tool-2026?v={i}"
    for i in range(500)
]

async def deploy_agent(agent_id, message):
    # Giả lập hành động rải link vào các ngách Crypto
    print(f"[Agent {agent_id}] Đang xâm nhập group mục tiêu...")
    await asyncio.sleep(random.uniform(0.1, 0.5)) # Tốc độ cực nhanh nhưng vẫn né được quét
    print(f"[Agent {agent_id}] Đã rải link: {message[:50]}...")

async def start_army():
    tasks = []
    for i, msg in enumerate(AGENTS_MESSAGES):
        tasks.append(deploy_agent(i, msg))
    
    # Kích hoạt 500 con cùng lúc
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("--- KHỞI ĐỘNG ĐỘI QUÂN 500 AGENT ---")
    asyncio.run(start_army())
    print("--- TẤT CẢ AGENT ĐÃ RA QUÂN. ĐỢI CÁ CẮN CÂU TRÊN TELEGRAM ---")
