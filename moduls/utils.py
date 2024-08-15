import sys, time, os
from moduls import colors
# --- ANIMATION
def animINFO(s):
    """An function for animate INFO DATA in the console
* s: The text that will be animated"""
    s = f"{colors.BLUE}[{colors.WHITE}INFO{colors.BLUE}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def animDONE(s):
    """An function for animate SUCCESS DATA in the console
* s: The text that will be animated"""
    s = f"{colors.GREEN}[{colors.WHITE}DONE{colors.GREEN}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)


def animERROR(s):
    """An function for animate ERROR DATA in the console
* s: The text that will be animated"""
    s = f"{colors.RED}[{colors.WHITE}ERROR{colors.RED}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def anim(s):
    """An function for animate text in the console
* s: The text that will be animated"""
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

async def loading_message(message, sticker_id=0):
    """Stickers pack for the loading effect
* 0: Loading focus -> default
* 1: Whell
* 2: Cloud uploading
* 3: Files
* 4: Cocodrile
* 5: Linear"""
    LISTA_STICKERS = [
        "CAACAgUAAxkBAAIH6GTnnz50bOkZeI6bg0-Y31I1behoAAKcAAPIlGQUc48AAfPaxYX8MAQ",
        "CAACAgUAAxkBAAEK7VNlc6q3USwPWTu3e6V4JJliYesHzQACmgADyJRkFCxl4eFc7yVqMwQ",
        "CAACAgUAAxkBAAEK7VVlc6uex00WmBRBkOwatwjCOuG-VAACpQADyJRkFHhDhV4BRbZGMwQ",
        "CAACAgUAAxkBAAEK7Vdlc6vebcbOXztVGwyVtPG8rOFjZwACpwADyJRkFGCmdrVn5RydMwQ", 
        "CAACAgIAAxkBAAN2ZdKS5UetFdo704o6sHi5_daCDGQAAjgLAAJO5JlLMrFH0tlPjNAeBA",
        "CAACAgUAAxkBAAPfZdKvwArlZE4TkkymoGmuQ9lK3wQAAqEAA8iUZBTlOvHR3aRelx4E"
    ]
    message_f = await message.reply_sticker(LISTA_STICKERS[sticker_id])
    return message_f