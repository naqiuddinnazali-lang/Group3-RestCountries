import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID")

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def send_telegram_notification(record: dict) -> bool:
    population    = record["data"]
    #record_id  = record["id"]
    created_at = record["created_at"]

    message = (
        f"<b>Highest Population Country Updated</b>\n"
        f"<b>Created at: {population["created_at"]}\n"
        f"{json.dumps(record, indent=2)}\n"
    )

    payload = {
        "chat_id":    TELEGRAM_CHAT_ID,
        "text":       message,
        "parse_mode": "HTML",
    }

    try:
        print("[TELEGRAM] Sending notification...")
        response = requests.post(TELEGRAM_API_URL, json=payload, timeout=10)
        response.raise_for_status()
        print(f"[TELEGRAM] Notification sent (chat_id: {TELEGRAM_CHAT_ID})")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"[TELEGRAM] HTTP error: {e} — Response: {response.text}")
        return False
    except Exception as e:
        print(f"[TELEGRAM] Failed to send notification: {e}")
        return False