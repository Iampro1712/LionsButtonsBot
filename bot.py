from config import app
from cmds import start, help, add, remove, list, send, edit

if __name__ == '__main__':
    print("Iniciando bot...")
    app.run()