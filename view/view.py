from view.LCD1602 import CharLCD1602
from time import sleep


class view:
    def __init__(self):
        self.lcd = CharLCD1602()
        self.lcd.init_lcd(0x27, 1)

    def afficher(self, ligne1, ligne2=""):
        self.lcd.clear()
        self.lcd.write(0, 0, ligne1.ljust(16))
        self.lcd.write(0, 1, ligne2.ljust(16))

    def effacer(self):
        self.lcd.clear()
