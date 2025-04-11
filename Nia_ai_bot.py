import requests
import time

# Masukkan token dari BotFather di sini
TELEGRAM_BOT_TOKEN = 'ISI_TOKEN_KAMU_DI_SINI'

# URL dasar Telegram API
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

# Fungsi kirim pesan ke user
def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, data=payload)

# Fungsi balas otomatis (AI sederhana)
def get_ai_response(message):
    if "gambar" in message.lower():
        return "Saya belum bisa kirim gambar dari PythonAnywhere. Tapi nanti bisa kita tambahkan!"
    return f"Kamu bilang: {message}\n(Suatu saat saya akan pakai AI OpenAI!)"

# Loop utama
def main():
    print("Bot sedang berjalan...")
    offset = None
    while True:
        url = f"{BASE_URL}/getUpdates"
        params = {'timeout': 100, 'offset': offset}
        response = requests.get(url, params=params).json()

        for update in response.get("result", []):
            offset = update["update_id"] + 1
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")
                reply = get_ai_response(text)
                send_message(chat_id, reply)

        time.sleep(1)

# Jalankan bot
if __name__ == "__main__":
    main()