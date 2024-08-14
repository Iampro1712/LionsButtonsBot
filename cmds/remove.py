from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import prefixs
import sqlite3
from config import path_db
from config import app

@app.on_message(filters.command('remove', prefixes=prefixs))
async def rmv(client, message):
    TEXT = message.text.split()
    if len(TEXT) < 2:
        await message.reply_text("Debes ingresar el ID del canal que deseas eliminar.")
        return
    
    try:
        ch_id = int(TEXT[1])
    except ValueError:
        await message.reply_text("El **ID DEL CANAL** debe ser un número válido.")
        return
    
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM UsersBotonera WHERE channel_id=?", (ch_id,))
    conn.commit()
    conn.close()
    await message.reply_text("Canal eliminado con éxito.")