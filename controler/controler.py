from datetime import datetime
from model import Modele
from mesure import Mesure
from view.platine import Platine
from view.view import view
from time import sleep

class Controler:
    def __init__(self):
        self.platine = Platine()
        self.vue = view()
        self.modele = Modele("donnees.json")
        self.en_marche = False
        
    
