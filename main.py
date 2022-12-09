# RiZoeL 2022 © Coder-Bot 

""" Imports """
import os
import sys
import pip
import asyncio
import base64
import urllib.parse

print("""
     --------------------------
             starting...
     --------------------------
""")

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

if os.path.exists(".env"):
    load_dotenv(".env")

print("Bot - [INFO]: Cheking Variables....")
API_ID = int(os.getenv("API_ID", ""))
if not API_ID:
    print("Bot - [INFO]: Fill API_ID!")
    sys.exit()

API_HASH = os.getenv("API_HASH", "")
if not API_HASH:
    print("Bot - [INFO]: Fill API_HASH!")
    sys.exit()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    print("Bot - [INFO]: Fill BOT_TOKEN!")
    sys.exit()

print("Bot - [INFO]: Got all variables ✓")
   
RiZoeL = Client('Coder-Bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
print("Bot - [INFO]: Got Client!")



""" Functions """

source_code_button = [[
                     InlineKeyboardButton("• Source Code •", url="https://github.com/MrRizoel/Coder-Bot"),
                     ], ]

def _filter(cmd: str):
   return filters.private & filters.incoming & filters.command(cmd)

async def coder_(RiZoeL, message, type):
    args = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)
    if args:
       code = str(args[0])
    else:
       await message.reply_text("Gime code text!")
       return

    if type == "url":
       try:
          new_link = urllib.parse.quote_plus(code)
          google_url =  "https://www.google.com/url?q=" + url
          final_text = f"""
**Your URL Encoded**

New url: `{new_link}`
Google test: [Click Here.](google_url)
"""
       except Exception as error:
          await message.reply(f"oops error! {error}")
          return
    elif type == "encode":
       try:
          encode = base64.b64encode(code)
          final_text = f"""
**Encoded ✓**

Encode: `{encode}`
"""
       except Exception as error:
          await message.reply(f"oops error! {error}")
          return
    elif type == "decode":
       try:
          decode = base64.b64decode(code)
          final_text = f"""
**Decoded ✓**

Decode: `{decode}`
"""
       except Exception as error:
          await message.reply(f"oops error! {error}")
          return
    await RiZoeL.send_message(message.chat.id, final_text, reply_markup=InlineKeyboardMarkup(source_code_button))


@RiZoeL.on_message(_filter("start"))
async def start_(_, message: Message):
    user = message.from_user
    await message.reply(
               f"**Hello! {user.mention}**, I'm Pyrogram based Encode/Decode bot!",
               reply_markup=InlineKeyboardMarkup(source_code_button))

@RiZoeL.on_message(_filter(["ping", "speed"]))
async def ping_(_, message: Message):
    start = datetime.datetime.now()
    ping_txt = await message.reply("**Pong!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    await ping_txt.edit_text(f"🤖 **P O N G**: `{ms}`ms")

@RiZoeL.on_message(_filter(["url", "urlencode"]))
async def url_(_, message: Message):
    await coder_(RiZoeL, message, "url")
    print(f"Bot - [INFO]: {message.from_user.first_name} encode url!")
    return

@RiZoeL.on_message(filters.private & filters.web_page)
async def direct_(_, message: Message):
    try:
       new_link = urllib.parse.quote_plus(code)
       google_url =  "https://www.google.com/url?q=" + url
       final_text = f"""
**Your URL Encoded**

New url: `{new_link}`
Google test: [Click Here.](google_url)
"""
    except Exception as error:
       await message.reply(f"oops error! {error}")
       return
    await message.reply(final_text)
    print(f"Bot - [INFO]: {message.from_user.first_name} encode url!")
    
@RiZoeL.on_message(_filter(["en", "encode"]))
async def encode_(_, message: Message):
    await coder_(RiZoeL, message, "encode")
    print(f"Bot - [INFO]: {message.from_user.first_name} encode text!")
    return

@RiZoeL.on_message(_filter(["de", "decode"]))
async def decode_(_, message: Message):
    await coder_(RiZoeL, message, "decode")
    print(f"Bot - [INFO]: {message.from_user.first_name} decode text!")
    return

@RiZoeL.on_message(_filter("help"))
async def help_(_, message: Message):
    help_text = """
**Commands available**

• /ping - to check ping/speed.
• /url (url) - to encode url.
• /encode (text) - to encode text.
• /encode (text? - to decide text.
"""
    await message.reply(help_text)


if __name__ == "__main__:
    RiZoeL.start()
