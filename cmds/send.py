from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from cmds.buttons import send_links_with_captions
from config import app, prefixs
from functions.func import connect_db

@app.on_message(filters.command("send", prefixes=prefixs))
async def send_message_to_all(client, message):
    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para enviar mensajes.")
        return
    
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT channel_id FROM UsersBotonera;")
    channels_ids = cursor.fetchall()
    cursor.execute("SELECT caption FROM UsersBotonera;")
    text = cursor.fetchone()
    text = text[0]

    for channel_id in channels_ids:
        channel = channel_id[0]
        try:
            await send_links_with_captions(app, channel, message)
            await message.reply_text(f"Mensaje enviado exitosamente a **`{channel}`**. Gracias **@MasterBinn3r**.")
        except Exception as e:
            print(f"Error sending message to {channel}: {e}")

    cursor.close()
    conn.close()