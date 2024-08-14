from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import prefixs
from config import app

@app.on_message(filters.command('help', prefixes=prefixs))
async def help(client, message):
    await message.reply_text("""
**Lista de comandos:**
    - /start: Inicia el bot.
                             
    - /help: Muestra este mensaje de ayuda.
                             
    - /add: Registra un canal para la botonera.
        Ejemplo de uso: /add owner_id, channel_id, link_channel, caption

    - /remove: Elimina un canal de la botonera.
        Ejemplo de uso: /remove channel_id

    - /list: Muestra los canales registrados.
    
    - /edit_cp_ch: Para editar el mensaje que se muestra en el boton.
        Ejemplo de uso: /edit_cp_ch channel_id, mensaje_nuevo.
                        
    - /send: Para enviar la botonera a los canales guardados.
                    
    - /edit_photo: Para editar la foto principal de la botonera.
                             
    - /edit_cp: Para editar el texto de inicio de la botonera
        Ejemplo de uso: /edit_cp texto_nuevo""")