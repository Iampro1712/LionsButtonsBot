# --------- LIBRERIAS ---------
from pyrogram import filters
from config import app, prefixs

# --------- FUNCION ---------
@app.on_message(filters.forwarded)
async def get_channel_id(client, message):
    # Verifica si el mensaje es de un canal reenviado
    if message.forward_from_chat:
        #DE AQUI SACAMOS EL ID DEL CANAL
        channel_id = message.forward_from_chat.id
        #Y POR ULTIMO LO MANDAMOS A LA PERSONA QUE LO SOLICITO
        await message.reply(f"El ID del canal es: `{channel_id}`")
    else:
        #Si no es un canal reenviado, se le manda un mensaje de error al usuario
        print("El mensaje no es de un canal reenviado")  # Si no es un canal reenviado
        await message.reply("Por favor, envía un mensaje reenviado de un canal para obtener su ID.")
