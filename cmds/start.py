from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import prefixs
from config import app

@app.on_message(filters.command('start', prefixes=prefixs))
async def strt(client, message):
    name = message.from_user.first_name
    await message.reply_text(f"Hola **{name}**, Bienvenido a **Lions Buttons Bot**.")