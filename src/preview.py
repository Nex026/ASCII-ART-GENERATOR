from pyfiglet import Figlet
import fonts as f
import clear as c
import time

def preview(text, font1):
    c.clear()
    global old_font
    old_font = font1
    try:
        print(Figlet(font=font1).renderText(text))
    except Exception:
        print("Invalid font")
    time.sleep(3)
    c.clear()
    f.fonts(text)