from pyrogram import Client
#Poner sus credenciales, las api puedes obtenerla desde my.telegram.org
API_ID = "API ID" 
API_HASH = "API HASH"
BOT_TOKEN = "BOT TOKEN"
prefixs = ['/', '!', '.']
path_db = "db/info.db"
path_db_ky = "db/info_ky.db"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
