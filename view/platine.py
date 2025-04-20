from gpiozero import DistanceSensor, Button
from ADCDevice import *
import RPi.GPIO as GPIO
import math
from time import sleep

class Platine:
    def __init__(self):  
        self.buttons = {
            "Bouton1": Button(19),
            "Bouton2": Button(13)            
            }
        
        self.capteur = DistanceSensor(echo=12, trigger=17, max_distance=1.0)
        
        self.adc = ADCDevice()
        self.adc_detecte = False
        self.initialisation()
        
    def initialisation(self):
        if self.adc.detectI2C(0x48): 
            self.adc = ADS7830()
            self.adc_detecte = True
            print("Module ADC détecté.")
        else:
            print("Erreur : Aucun moduke ADC trouvée. Fin du programme")
            exit(-1)
            
    def lecture_distance(self):
        return round(self.capteur.distance * 100, 1)
    
    def lecture_volt(self):
        if self.adc_detecte:
            valeur = self.adc_analogRead(0)
            tension = valeur / 255.0 * 3.3
            return round(tension, 2)
        else:
            return 0.0

        
    def boucle(self):
        while True:
            distance = self.lecture_distance()
            temperature = self.lecture_volt()
            print("Distance : %.1f cm, Tension : %.2f V" % (distance, temperature))
            sleep(1)
    
    def fin(self):
        if self.adc_detecte:
            self.adc.close()
        GPIO.cleanup()
