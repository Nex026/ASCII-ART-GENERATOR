from colorama import Fore, Style
from pyfiglet import Figlet
import clipboard as clp
import selection as s
import clear as c
import time

def selected(text, font1):
    c.clear()

    try:
        r = Figlet(font=font1).renderText(text)
        print(r)
        clp.copy(r)
        print(Fore.GREEN + "Successfully Copied" + Style.RESET_ALL)
    except Exception:
        print("Invalid font")

    time.sleep(3)
    s.selection()