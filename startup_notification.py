import requests
import os
import socket

from backend.core.config import settings


BOT_TOKEN = settings.BOT_TOKEN
CHAT_ID = settings.CHAT_ID

def send_startup_message():
    computer_name = socket.gethostname()
    user_name = os.getenv('USERNAME', 'Unknown')
    
    message = f"🟢 Компьютер {computer_name} включен! Пользователь: {user_name}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, data=data, timeout=10)
        print(f"Message sent: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_startup_message()