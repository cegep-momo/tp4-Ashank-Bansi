from datetime import datetime
from model.modele import Modele
from model.mesure import Mesure
from view.platine import Platine
from view.view import view
from time import sleep

class Controler:
    def __init__(self):
        self.platine = Platine()
        self.vue = view()
        self.modele = Modele("donnees.json")
        self.en_marche = False
        
    def demarrer_programme(self):
        self.en_marche = True
        self.vue.afficher("System en", "marche")

    def arreter_programme(self):
        self.en_marche = False
        self.vue.afficher("Systeme", "fermé")
        sleep(1.5)
        self.vue.effacer()

    def boucle(self):
        while True:
            if self.platine.buttons["Bouton1"].is_pressed:
                if not self.en_marche:
                    self.demarrer_programme()
                else:
                    self.arreter_programme()
                sleep(0.5)  

            if self.en_marche:
                distance = self.platine.lecture_distance()
                self.vue.afficher("Distance:", f"{distance:.1f} cm")
                sleep(5)

                if self.platine.buttons["Bouton2"].is_pressed:
                    self.enregistrer_donnees_mesure(distance)
                    sleep(0.5)

    def enregistrer_donnees_mesure(self, distance):
        now = datetime.now()
        mesure = Mesure(now.strftime('%Y-%m-%d %H:%M:%S'), [distance])
        self.modele.enregistrer_donnees(now, [distance])
        self.vue.afficher("Mesure prise:", f"{distance:.1f} cm")
        print(mesure)

    def fin_programme(self):
        self.platine.fin()
        self.vue.effacer()
        print("Fin du programme.")
