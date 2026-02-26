import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def postar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    requests.post(url, data=data)

def gerar_post():
    return (
        "🔥 *ACHADINHO IMPERDÍVEL*\n\n"
        "🛍️ Oferta do dia na Shopee\n"
        "💸 Preço especial\n"
        "👉 COLE AQUI SEU LINK DE AFILIADA\n\n"
        "⏰ Corre que acaba!"
    )

while True:
    postar(gerar_post())
    time.sleep(3600)  # posta a cada 1 hora
