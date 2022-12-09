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
from pyrogram.types import Message 

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
