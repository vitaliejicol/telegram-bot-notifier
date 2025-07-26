import os
import asyncio
from bot.utils import send_notification
from bot.config import CHAT_ID

message = os.getenv("INPUT_MESSAGE")  # GitHub Actions passes inputs as INPUT_<name>
chat_id = os.getenv("CHAT_ID")

if message and chat_id:
    asyncio.run(send_notification(message))
else:
    print("❌ Missing message or chat ID")
