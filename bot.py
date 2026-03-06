import re
import asyncio
from telethon import TelegramClient, events
import os

api_id = int(os.getenv("35743821"))
api_hash = os.getenv("9ff4cf53160b1f1a6189198955c7b3e1")

source_group = os.getenv("https://t.me/+kzQWdOJvDzZmMGQ0")
target_group = os.getenv("https://t.me/+OBUXN8C8Jhk3Nzc0")

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
            message = f"Packet Loss Detected!\n\n{text}"
            await client.send_message(target_group, message)


async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()


asyncio.run(main())