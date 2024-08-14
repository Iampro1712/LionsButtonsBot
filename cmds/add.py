from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import prefixs
from functions.func import validacion_input, create_table, insert_user
from datetime import datetime
import sqlite3
from config import app
from  pyrogram.errors import *

@app.on_message(filters.command('add', prefixes=prefixs))
async def add_ch(client, message):
    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para enviar mensajes.")
        return
    
    TEXT = message.text.split()
    # Verificamos si se han proporcionado suficientes argumentos
    if len(TEXT) < 2:
        await message.reply_text("Debes ingresar los datos requeridos.")
        return
    
    vars_ = " ".join(TEXT[1:])
    vars_ = vars_.split(",")

    if len(vars_) < 4:
        await message.reply_text("Faltan datos en tu mensaje. Asegúrate de ingresar todos los datos requeridos.")
        return

    if len(vars_[0].strip()) < 10 or not vars_[0].strip().isdigit():
        await message.reply_text("El **OWNER ID** proporcionado no es válido.")
        return

    link = vars_[2].strip()
    if not link.startswith("https://t.me/"):
        await message.reply_text("El **Link** proporcionado no es válido.")
        return
    
    mensaje = vars_[3].strip()
    if not mensaje:
        await message.reply_text("Debes ingresar un **Mensaje**.")
        return
    
    try:
        chat_id = vars_[1]
        subs = await app.get_chat_members_count(chat_id)
        info_ch = await app.get_chat(chat_id)
        name_ch = info_ch.title
        now = datetime.now()
        fecha = now.strftime("%d-%m-%Y %H:%M:%S")
        create_table()
        
        # Verificación de duplicados
        if not validacion_input(chat_id, vars_[2], name_ch, vars_[3]):
            await message.reply_text("Este canal ya ha sido registrado previamente.")
            return
        
        insert_user(vars_[0], chat_id, link, name_ch, mensaje, subs, fecha)
        await message.reply_text(f"Canal registrado con éxito. Subs: `{subs}`, Nombre: {name_ch}")
    
    except sqlite3.DatabaseError as e:
        await message.reply_text(f"Error al registrar en la Base de Datos {e}.")
        print(e)
        return
    except PeerIdInvalid as e:
        await message.reply_text(f"El bot no esta en el canal `{chat_id}`.")
        print(e)
        return

    except ValueError as e:
        if "Peer id invalid" in str(e):
            await message.reply_text("El ID del peer no es válido")

    # except Exception as e:
    #     await message.reply_text(f"Error al registrar el canal, Excepción: {e}.")
    #     print(e)
    #     return