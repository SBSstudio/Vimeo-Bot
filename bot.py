
import os
import logging
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vimeo_downloader import Vimeo
from sample_config import Config


LOCATION = "./downloades"

STARTPIC = "https://telegra.ph/file/3f46a4a1ffecf0a641a02.jpg"

START_TEXT ="Hey, I'm Vimeo downloader bot 😜 \n\nI can download vimeo video links and upload to Telegram 🥰 \n\nSend me a vimeo video link to start download 😎"
# logging
bot = Client(
   "Vimeo",
   api_id=Config.API_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

# start message
@bot.on_message(filters.private & filters.command(["start"]))
async def start(c, m):
    await m.reply_photo(
        photo=STARTPIC,
        caption=START_TEXT,
    )

# vimeo download
@bot.on_message(filters.regex(pattern="https://vimeo.com/") & filters.private)
async def vimeo(_, message):
    input = message.text
    user = message.from_user.mention
    msg = await message.reply_text("📥 `Downloading...`")
    try:
        v = Vimeo(input)
        stream = v.streams
        stream[-1].download(download_directory=LOCATION,
                        filename="dihanofficial-vimeo.mp4")
        file = "./dihanofficial-vimeo.mp4"
        await msg.edit("📤 `Uploading...`")
        cap = f" `Uploaded By :` {user} \n `Bot By:` @DihanOfficial"    
        await bot.send_video(message.chat.id, video=file, caption=cap)
        await msg.delete()
        os.remove(file)
    except Exception as e:
        print(str(e))
        await msg.edit("❌ `Error.`")
        return

bot.start()
idle()
