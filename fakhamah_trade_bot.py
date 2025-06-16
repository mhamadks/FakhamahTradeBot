
from flask import Flask, request
import requests
import os

app = Flask(__name__)

# توكن البوت (تأكد أنه محفوظ بأمان في بيئة آمنة على السيرفر)
TELEGRAM_BOT_TOKEN = "8048449538:AAGMXSpY7y8QuJ5T_8bW9bm4qM25pb4LNCM"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"  # ضع هنا ID حسابك أو قناة التليجرام

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/')
def home():
    return 'Bot is running!'

@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json()
    message = data.get('message', '📡 إشعار من TradingView')
    send_telegram_message(message)
    return {'status': 'message sent'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
