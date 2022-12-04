from pyfiglet import Figlet
from colorama import Fore, Style
from fonts import fonts
import clear as c

def selection():
    c.clear()
    print(Fore.GREEN + Figlet(font='larry3d').renderText('ASCII ART') + Style.RESET_ALL)
    text = input(str("Enter the text to be transformed into ASCII ART: "))
    if text != ' ':
        fonts(text)