from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity
from pyrogram.errors import ChatWriteForbidden
from config import app, prefixs
from functions.func import connect_db, connect_db2, create_table_ky

photo_url = None
text_cp = None

@app.on_message(filters.command("edit_photo", prefixes=prefixs))
async def edit_photo(client, message):
    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para enviar mensajes.")
        return
    
    global photo_url

    phoyo = get_photo_and_text()
    phoyo1 = phoyo[0]
    phoyo_1 = phoyo1[0]

    await message.reply_text(f"""Link de la foto pasada: `{phoyo_1}`""")

    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para editar la foto.")
        return
    TEXT = message.text.split()
    pht_url = " ".join(TEXT[1:]).split(",")
    if len(pht_url) < 1:
        await message.reply_text("Debes ingresar los datos correctamente.")
        return
    
    photo_url = pht_url[0].strip()
    update_photo(photo_url)
    await message.reply_text("Foto editada con éxito.")

@app.on_message(filters.command("edit_cp", prefixes=prefixs))
async def edit_caption(client, message):
    if message.from_user.id not in [6706374638, 6364510923]:
        await message.reply("No tienes permiso para editar el caption.")
        return

    global text_cp
    create_table_ky()
    
    # Captura todo el mensaje, excluyendo el comando
    text_cp = message.text.split(None, 1)[1]  # Captura todo el texto después del comando

    cp_past = get_cp()
    cp_past1 = cp_past[0]

    await message.reply_text(f"Caption anterior: {cp_past1}")
    await message.reply_text(f"Nuevo caption: {text_cp}")
    
    update_caption(text_cp)
    await message.reply_text("Caption editado con éxito.")


def update_photo(new_photo):
    try:
        conn = connect_db2()
        cursor = conn.cursor()
        cursor.execute("UPDATE ConfigBotonera SET img_link = ?;", (new_photo,))
        conn.commit()
        print(f"Foto actualizada a: {new_photo}")
        cursor.execute("SELECT img_link FROM ConfigBotonera;")
        photos = cursor.fetchall()
        print(f"Fotos en la base de datos: {photos}")
    except Exception as e:
        print(f"Error al actualizar la foto: {e}")
    finally:
        conn.close()

def update_caption(new_caption):
    try:
        conn = connect_db2()
        cursor = conn.cursor()
        cursor.execute("UPDATE ConfigBotonera SET caption = ?;", (new_caption,))
        conn.commit()
        print(f"Caption actualizada a: {new_caption}")
        cursor.execute("SELECT caption FROM ConfigBotonera;")
        captions = cursor.fetchall()
        print(f"Captions en la base de datos: {captions}")
    except Exception as e:
        print(f"Error al actualizar el caption: {e}")
    finally:
        conn.close()


# Función para obtener los links y captions desde la base de datos
def get_links_and_captions_from_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT caption, link_channel FROM UsersBotonera;")
    return cursor.fetchall()

def get_photo_and_text():
    create_table_ky()
    conx = connect_db2() 
    cursor = conx.cursor()
    cursor.execute("SELECT img_link, caption FROM ConfigBotonera;")
    return cursor.fetchall()

def get_cp():
    create_table_ky()
    conx = connect_db2() 
    cursor = conx.cursor()
    cursor.execute("SELECT caption FROM ConfigBotonera;")
    return cursor.fetchall()

# Función para crear los botones y enviar el mensaje
async def send_links_with_captions(client, chat_id, message):
    global photo_url
    global text_cp
    rows = get_links_and_captions_from_db()
    rows2 = get_photo_and_text()
    buttons = []

    for row2 in rows2:
        photo_url = row2[0]
        text_cp = row2[1]

    permanent_button = InlineKeyboardButton("🔗 AÑADE TU CANAL AQUI", url="https://t.me/LionsButtonsBot")
    buttons.append([permanent_button])

    for row in rows:
        caption = row[0]
        link_channel = row[1]
        button = InlineKeyboardButton(text=caption, url=link_channel)
        buttons.append([button])

    if photo_url is None:
        photo_url = "imgs/lion_1.jpg"

    keyboard = InlineKeyboardMarkup(buttons)
    
    try:
        await app.send_photo(
            chat_id=chat_id,
            photo=photo_url,
            caption=text_cp,
            reply_markup=keyboard
        )
    except ChatWriteForbidden:
        await app.send_message(6364510923, f"Error: No tienes permisos para enviar mensajes en el chat `{chat_id}`.")
        await message.reply_text(f"No tengo permisos para enviar mensajes en este canal. \n**ID:** `{chat_id}`")

# Función manejadora del comando
def handle_links(client, message):
    send_links_with_captions(client, message.chat.id)

@app.on_message(filters.command("prev-see", prefixes=prefixs))
async def previsualizacion(client, message):
    if message.from_user.id != 6706374638 and message.from_user.id != 6364510923:
        await message.reply("No tienes permiso para enviar mensajes.")
        return
    await send_links_with_captions(client, message.chat.id, message)
    await message.reply_text("Aqui esta la botonera bb, disfrutala 💕🥵.")
    return