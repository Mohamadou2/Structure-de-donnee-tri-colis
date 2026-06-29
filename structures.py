class FileAttente:
    def __init__(self):
        self._elements = []
    
    def est_vide(self):
        return len(self._elements) == 0
    
    def ajouter(self, colis):
        self._elements.append(colis)
    
    def retirer(self):
        if self.est_vide():
            print("La file est vide")
        return self._elements.pop(0)
    
    def premier(self):
        if self.est_vide():
            return None
        return self._elements[0]
    
    def taille(self):
        return len(self._elements)
    
    def afficher(self):
        if self.est_vide():
            print("File d'attente vide")
            return
        
        print(f"=== File d'attente ({self.taille()} colis) ===")
        for i, colis in enumerate(self._elements, 1):
            print(f"{i}. {colis}")
    
    def get_elements(self):
        return self._elements.copy()
    
    def set_elements(self, elements):
        self._elements = elements

class PileChargement:
    def __init__(self):
        self._elements = [] 
    
    def est_vide(self):
        return len(self._elements) == 0
    
    def empiler(self, colis):
        self._elements.append(colis) 
    
    def depiler(self):
        if self.est_vide():
            print("La pile est vide")
        return self._elements.pop()
    
    def sommet(self):
        if self.est_vide():
            return None
        return self._elements[-1]
    
    def taille(self):
        return len(self._elements)
    
    def afficher(self):
        if self.est_vide():
            print("Pile de chargement vide")
            return
        
        print(f"=== Pile de chargement ({self.taille()} colis) ===")
        for i in range(len(self._elements) - 1, -1, -1):
            position = len(self._elements) - i
            print(f"{position}. {self._elements[i]}")
    
    def get_elements(self):
        return self._elements.copy()
    
    def set_elements(self, elements):
        self._elements = elements