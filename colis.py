import random

class Colis:

    _dernier_id_num = 0
    
    def __init__(self, id_colis=None, priorite=1, poids=1.0, ordre_arrivee=0, destination=""):

        if id_colis is None:
            Colis._dernier_id_num += 1
            self.id = f"COLIS_{Colis._dernier_id_num:03d}"
        else:
            self.id = id_colis
        
        self.priorite = priorite
        self.poids = poids
        self.ordre_arrivee = ordre_arrivee
        self.destination = destination
    
    def __str__(self):
        dest = f" - {self.destination}" if self.destination else ""
        return (f"ID: {self.id} | Priorité: {self.priorite}/5 "
                f"| Poids: {self.poids:.1f}kg | Arrivée: {self.ordre_arrivee}{dest}")
    
    # def __repr__(self):
    #     return f"Colis({self.id}, p={self.priorite}, {self.poids}kg, arr={self.ordre_arrivee})


def generer_colis_aleatoire(ordre_arrivee, destinations=None):

    if destinations is None:
        destinations = ["Nktt", "Rosso", "Aleg", "Boghe", "Kaedi", "Selibabi", "NDB"]
    
    priorite = random.randint(1, 5) 
    poids = round(random.uniform(0.5, 25.0), 1)
    destination = random.choice(destinations)
    
    return Colis(priorite=priorite, poids=poids, ordre_arrivee=ordre_arrivee, destination=destination)


c1 = Colis(id_colis="TEST001", priorite=3, poids=12.5, ordre_arrivee=1, destination="Paris")
c2 = Colis(priorite=2, poids=5.0, ordre_arrivee=2)

