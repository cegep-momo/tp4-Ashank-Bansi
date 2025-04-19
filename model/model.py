import json, codecs

class Modele:
    
    def __init__(self, fichier):
        self.fichier = fichier
        
    def enregistrer_donnees(self, date, valeurs):
        
        nouvelles_donnees = {
            "date": date.strftime('%Y-%m-%d %H:%M:%S'),
            "valeurs": valeurs       
        }
        
        try:
            with codecs.open(self.fichier, "r", encoding="utf-8") as f:
                donnees = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            donnees=[]
            
        donnees.append(nouvelles_donnees)
        
        with codecs.open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        