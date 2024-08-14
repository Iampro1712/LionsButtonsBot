from pyrogram import Client, filters

from config import app, prefixs
from functions.func import connect_db, mk_queries

@app.on_message(filters.command("edit_cp_ch", prefixes=prefixs))
async def editmsg(client, message):
    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para editar mensajes.")
        return
    
    TEXT = message.text.split()
    caption = " ".join(TEXT[1:]).split(",")

    # Verifica si hay al menos dos elementos en la lista `caption`
    if len(caption) < 2 or len(caption[1].strip()) < 1:
        await message.reply_text("Debes ingresar los datos correctamente.")
        return

    if len(caption[0].strip()) < 14:
        await message.reply_text("Debes ingresar el **ID del canal** que deseas editar.")
        return

    try:
        ch_id = int(caption[0].strip())
    except ValueError:
        await message.reply_text("El **ID DEL CANAL** debe ser un número válido.")
        return

    cap = mk_queries(f"SELECT * FROM UsersBotonera WHERE caption = '{caption[1]}'")
    owner_cap = mk_queries(f"SELECT name_channel FROM UsersBotonera WHERE caption = '{caption[1]}'")
    if cap:
        await message.reply_text(f"Ya existe un registro con este caption. \nCanal con el caption: {owner_cap[0][0]}")
        return False
    

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE UsersBotonera SET caption=? WHERE channel_id=?", (caption[1], ch_id))
    conn.commit()
    cursor.close()
    conn.close()
    await message.reply_text("Caption editado con éxito.")