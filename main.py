import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.environ.get("API_ID", 26468828))
API_HASH = os.environ.get("API_HASH", "4693513c08d1ac6af15f95b116c29478")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

bot = Client("so_to_py_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("<blockquote>Send a .so file to manage it.</blockquote>")

@bot.on_message(filters.document)
async def handle_so_file(client: Client, message: Message):
    doc = message.document

    if not doc.file_name.endswith(".so"):
        await message.reply("<blockquote>Please send a `.so` file only.</blockquote>")
        return

    # Download the .so file
    file_path = await message.download()

    # Acknowledge receipt and clarify the conversion limitation
    await message.reply("<blockquote>Received .so file. Note: Converting back to .py is not supported.</blockquote>")

    # Implement any additional handling of the .so file if needed

    # Clean up the downloaded file
    if os.path.exists(file_path):
        os.remove(file_path)

bot.run()
