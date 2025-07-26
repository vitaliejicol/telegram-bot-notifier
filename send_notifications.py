import sys
import asyncio
from bot.utils import send_notification

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_notification.py 'your message'")
        sys.exit(1)

    msg = sys.argv[1]
    asyncio.run(send_notification(msg))
