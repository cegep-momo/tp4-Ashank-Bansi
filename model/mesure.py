from datetime import datetime

class Mesure:
    def __init__(self, dateHeureMesure, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure

    def __repr__(self):
        return f"{self.dateHeureMesure} - {self.dataMesure}"

    def afficherMesure(self):
        return f"Date : {self.dateHeureMesure}\nDonnées : {self.dataMesure}"
