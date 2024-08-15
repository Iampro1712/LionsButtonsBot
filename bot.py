from config import app
from cmds import start, help, add, remove, list, send, edit
import requests, sys, time as tm
from moduls import utils, banner

if __name__ == '__main__':
    utils.clear_terminal()

    banner.banner()

    utils.animINFO("Revisando si hay una conexion a internet....")
    internet = False

    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            utils.animDONE("Conexion encontrada, Procediendo a iniciar el bot.")
            internet = True
        else:
            utils.animERROR("No tienes una conexion a internet.")
            internet = False
    except requests.ConnectionError:
        utils.animERROR("No tienes una conexion a internet estable o no esta conectada a ninguna, Favor conectarse a una para proseguir...")

    if not internet:
        utils.animINFO("Saliendo...")
        sys.exit()

    utils.animINFO("Iniciando bot...")
    tm.sleep(2)
    utils.animDONE("Bot iniciado con exito.")
    utils.anim("\nCREADOR:\n        Telegram @MasterBinn3r")
    app.run()