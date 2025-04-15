from gpiozero import DistanceSensor, Button
from time import sleep
import LCD1602

class platine:
    def __init__(self):  
        self.buttons = {
            "Bouton1": Button(19),
            "Bouton2": Button(13)            
            }
        
        self.capteur = DistanceSensor(echo=12, trigger=17, max_distance=1.0)
    
        LCD1602.init(0x27, 1)
        
    def afficher_lcd(self, ligne1, ligne2=""):
        LCD1602.write(0, 0, ligne1.ljust(16))
        LCD1602.write(0, 1, ligne2.ljust(16))

    def effacer_lcd(self):
        LCD1602.clear()
        sleep(0.2)
        
     
