from colorama import Fore, Style, init
from selected import selected
from preview import preview
import selection as s
init(convert=True)
import clear as c
import time
import os

def fonts(text):
    print("Font list:" + Fore.MAGENTA)
    os.system('pyfiglet --list_fonts')
    print(Style.RESET_ALL)
    
    font = input(str("Enter the font: "))

    print("[0] - Preview\n[1] - Select\n[99] - Go Back")
    option = input(str("Option: "))

    if option == '0':
        preview(text, font)
    elif option == '1':
        selected(text, font)
    elif option == '99':
        s.selection()
    else:
        print(Fore.RED + "Command not recognized" + Style.RESET_ALL)
        time.sleep(2)
        c.clear()
        fonts(text)
