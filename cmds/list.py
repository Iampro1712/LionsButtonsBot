from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import prefixs
from functions.func import get_info_db
from config import app

@app.on_message(filters.command("list", prefixes=prefixs))
async def listch(client, message):
    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para enviar mensajes.")
        return

    await message.reply_text("𝙻𝚒𝚜𝚝𝚊 𝚍𝚎 𝚌𝚊𝚗𝚊𝚕𝚎𝚜 𝚛𝚎𝚐𝚒𝚜𝚝𝚛𝚊𝚍𝚘𝚜 𝚎𝚗 𝐋𝐢𝐨𝐧𝐬 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐨𝐭")
    list = get_info_db()
    for lista in list:
        await message.reply_text(f"""
[- - - - - - - - - - - - - - - - - - - - - - - - -](https://t.me/LionsButtonsBot)
Owner ID: `{lista[0]}`
Channel ID: `{lista[1]}`
Link: `{lista[2]}`
Canal: `**{lista[3]}**`
Caption: `{lista[4]}`
Subs: `{lista[5]}`
Fecha: `{lista[6]}`
[- - - - - - - - - - - - - - - - - - - - - - - - -](https://t.me/LionsButtonsBot)""")