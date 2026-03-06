import re
import os
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_group = os.getenv("SOURCE_GROUP")
target_group = os.getenv("TARGET_GROUP")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    text = event.message.text

    if not text:
        return

    match = re.search(r"Lost\s*=\s*(\d+)", text)

    if match:
        lost_value = int(match.group(1))

        if lost_value != 0:
            message = f" Packet Loss Detected!\n\n{text}"
            await client.send_message(target_group, message)

client.start()
client.run_until_disconnected()
