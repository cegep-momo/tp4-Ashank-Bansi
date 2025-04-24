from gpiozero import DistanceSensor, Button
import RPi.GPIO as GPIO
from time import sleep

class Platine:
    def __init__(self):  
        self.buttons = {
            "Bouton1": Button(19),
            "Bouton2": Button(13)            
            }
        
        self.capteur = DistanceSensor(echo=12, trigger=17, max_distance=1.0)
            
    def lecture_distance(self):
        return round(self.capteur.distance * 100, 1)
        
    
    def fin(self):
        GPIO.cleanup()
