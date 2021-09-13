
import os
import logging
import random
import time
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vimeo_downloader import Vimeo
from sample_config import Config
from pyromod.helpers import ikb



LOCATION = "./downloades"

START_BTN = ikb(
    [
        [
            ("💬 Updates Channel", "t.me/damiensoukara", "url"),
            ("🗣 Support Group", "t.me/damienhelp", "url"),
        ],
        [
            ("👾 About", "about"),
            ("📚 Help", "help"),
            ("❌", "close"),
        ],
        [
            (
                "🔗 Source Code",
                "https://github.com/AmineSoukara/PyLyricsBot/fork",
                "url",
            ),
            ("👨‍💻 Developer", "https://bio.link/aminesoukara", "url"),
        ],
    ]
)

HELP_BTN = ikb(
    [
        [
            ("💬 Updates Channel", "t.me/damiensoukara", "url"),
            ("🗣 Support Group", "t.me/damienhelp", "url"),
        ],
        [
            ("👾 About", "about"),
            ("📚 Help", "help"),
            ("❌", "close"),
        ],
    ]
)

STARTPIC = "https://telegra.ph/file/3f46a4a1ffecf0a641a02.jpg"

START_TEXT ="Hey, I'm Vimeo downloader bot 😜 \n\nI can download vimeo video links and upload to Telegram 🥰 \n\nSend me a vimeo video link to start download 😎"

HELP_TEXT ="Hey,"

HELPPIC = "https://telegra.ph/file/5db9ed27322137240ee4b.jpg"
# logging

bot = Client(
   "Vimeo",
   api_id=Config.API_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

# start message


@bot.on_callback_query()
async def cdata(c, q):

    data = q.data
    # userid = q.from_user.id
    pwait = "hi"
    if data == "help":
        await q.answer(pwait)
        await q.reply_photo(
        photo=HELPPIC,
        caption=HELP_TEXT,
        reply_markup=HELP_BTN,
    )
    elif data == "close":
        await q.message.delete(True)
        try:
            await q.message.reply_to_message.delete(True)

@bot.on_message(filters.private & filters.command(["start"]))
async def start(c, m):
    await m.reply_photo(
        photo=STARTPIC,
        caption=START_TEXT,
        reply_markup=START_BTN,
    )


bot.start()
idle()
