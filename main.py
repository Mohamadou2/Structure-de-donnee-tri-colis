from colis import Colis, generer_colis_aleatoire
from structures import FileAttente, PileChargement
from tris import tri_insertion_file, tri_selection_file, tri_insertion_pile, tri_selection_pile
import sys


class CentreTri:
    def __init__(self):

        self.file_attente = FileAttente()
        self.pile_chargement = PileChargement()
        self.ordre_arrivee_counter = 1 
        self.ids_existants = set()
        self.destinations = ["Nktt", "Rosso", "Aleg", "Boghe", "Kaedi", "Selibabi", "NDB"]
    
    
    def ajouter_colis_manuel(self):
        print("\n=== Ajout manuel d'un colis ===")
        while True:
            id_colis = input("ID du colis (laisser vide pour auto-généré): ").strip()
            if not id_colis:
                id_colis = f"COLIS_{Colis._dernier_id_num + 1:03d}"
                print(f"ID généré: {id_colis}")
                break
            
            if id_colis in self.ids_existants:
                print("Cet ID existe deja! Veuillez en choisir un autre.")
            else:
                break

        while True:
            try:
                priorite = int(input("Priorité (1-5, 5=urgent): "))
                if 1 <= priorite <= 5:
                    break
                else:
                    print("La priorité doit être entre 1 et 5")
            except ValueError:
                print("Veuillez entrer un nombre")

        while True:
            try:
                poids = float(input("Poids (kg): "))
                if poids > 0:
                    break
                else:
                    print("Le poids doit être positif")
            except ValueError:
                print("Veuillez entrer un nombre")

        destination = input("Destination (optionnel): ").strip()

        colis = Colis(
            id_colis=id_colis,
            priorite=priorite,
            poids=poids,
            ordre_arrivee=self.ordre_arrivee_counter,
            destination=destination
        )
        
        self.file_attente.ajouter(colis)
        self.ids_existants.add(id_colis)
        self.ordre_arrivee_counter += 1
        
        print(f"Colis {id_colis} ajouté à la file d'attente!")
    
    def ajouter_colis_aleatoire(self, nombre=1):
        """Ajoute un ou plusieurs colis alatoires"""
        print(f"\n=== Ajout de {nombre} colis aléatoire(s) ===")
        
        for i in range(nombre):
            colis = generer_colis_aleatoire(
                ordre_arrivee=self.ordre_arrivee_counter,
                destinations=self.destinations
            )
            
            self.file_attente.ajouter(colis)
            self.ids_existants.add(colis.id)
            self.ordre_arrivee_counter += 1
            
            print(f"  {colis}")
        
        print(f"{nombre} colis aléatoires ajoutés!")
    
    def traiter_colis(self):
        """Transfère un colis de la file vers la pile"""
        if self.file_attente.est_vide():
            print("La file d'attente est vide!")
            return
        
        try:
            colis = self.file_attente.retirer()
            self.pile_chargement.empiler(colis)
            print(f" Colis {colis.id} transféré vers la pile de chargement")
        except IndexError:
            print("Erreur lors du traitement du colis")
    
    def decharger_camion(self):
        """Décharge un colis de la pile vers le camion"""
        if self.pile_chargement.est_vide():
            print("La pile de chargement est vide!")
            return
        
        try:
            colis = self.pile_chargement.depiler()
            print(f" Colis {colis.id} chargé dans le camion!")
            print(f"   Détails: {colis}")
        except IndexError:
            print("Erreur lors du déchargement")
    
    def trier_file(self):
        """Menu pour choisir l'algorithme de tri de la file"""
        if self.file_attente.est_vide():
            print(" La file d'attente est vide!")
            return
        
        print("\n=== Tri de la file d'attente ===")
        print("1. Tri par insertion (stable)")
        print("2. Tri par sélection (non stable)")
        print("0. Annuler")
        
        choix = input("\nChoix: ").strip()
        
        if choix == "1":
            print("\nTri par insertion en cours...")
            tri_insertion_file(self.file_attente)
        elif choix == "2":
            print("\nTri par sélection en cours...")
            tri_selection_file(self.file_attente)
        elif choix == "0":
            print("Annulation")
        else:
            print(" Choix invalide")
    
    def trier_pile(self):
        """Menu pour choisir l'algorithme de tri de la pile"""
        if self.pile_chargement.est_vide():
            print(" La pile de chargement est vide!")
            return
        
        print("\n=== Tri de la pile de chargement ===")
        print("1. Tri par insertion (croissant)")
        print("2. Tri par insertion (décroissant)")
        print("3. Tri par sélection (croissant)")
        print("4. Tri par sélection (décroissant)")
        print("0. Annuler")
        
        choix = input("\nChoix: ").strip()
        
        if choix == "1":
            print("\nTri par insertion (croissant) en cours...")
            tri_insertion_pile(self.pile_chargement, croissant=True)
        elif choix == "2":
            print("\nTri par insertion (décroissant) en cours...")
            tri_insertion_pile(self.pile_chargement, croissant=False)
        elif choix == "3":
            print("\nTri par sélection (croissant) en cours...")
            tri_selection_pile(self.pile_chargement, croissant=True)
        elif choix == "4":
            print("\nTri par sélection (décroissant) en cours...")
            tri_selection_pile(self.pile_chargement, croissant=False)
        elif choix == "0":
            print("Annulation")
        else:
            print(" Choix invalide")
    
    def afficher_menu(self):
        """Affiche le menu principal"""
        print("\n" + "="*50)
        print("CENTRE DE TRI DES COLIS")
        print("="*50)
        print(f"File d'attente: {self.file_attente.taille()} colis")
        print(f"Pile de chargement: {self.pile_chargement.taille()} colis")
        print("-"*50)
        print("1. Ajouter un colis (manuel)")
        print("2. Ajouter des colis aléatoires")
        print("3. Traiter un colis (File → Pile)")
        print("4. Décharger camion (Pile → Camion)")
        print("5. Afficher la file d'attente")
        print("6. Afficher la pile de chargement")
        print("7. Trier la file par priorité")
        print("8. Trier la pile par poids")
        print("9. Comparer les algorithmes de tri")
        print("0. Quitter")
        print("-"*50)
    
    def comparer_tris(self):
        """Compare les performances des algorithmes de tri"""
        print("\n=== Comparaison des algorithmes de tri ===")
        
        if self.file_attente.est_vide():
            print(" La file d'attente est vide!")
            return
        
        # Créer des copies pour la comparaison
        import copy
        file_originale = copy.deepcopy(self.file_attente)
        
        print("\n1. Tri de la file par priorité:")
        print("-" * 40)
        
        # Test tri par insertion
        file_insertion = copy.deepcopy(file_originale)
        print("Tri par insertion en cours...")
        tri_insertion_file(file_insertion)
        
        # Test tri par sélection
        file_selection = copy.deepcopy(file_originale)
        print("Tri par sélection en cours...")
        tri_selection_file(file_selection)
        
        print("\n" + "="*50)
        print("RÉSUMÉ DES CARACTÉRISTIQUES:")
        print("="*50)
        print("TRI PAR INSERTION:")
        print("- Complexité: O(n²) pire cas, O(n) meilleur cas")
        print("- Stable: OUI (conserve l'ordre d'arrivée pour même priorité)")
        print("- Efficace pour petites listes ou listes presque triées")
        
        print("\nTRI PAR SÉLECTION:")
        print("- Complexité: O(n²) dans tous les cas")
        print("- Stable: NON (peut inverser l'ordre d'arrivée pour même priorité)")
        print("- Simple à comprendre, fait peu d'échanges")
        
        print("\n" + "="*50)
        
        # Demander à l'utilisateur quel résultat appliquer
        choix = input("\nAppliquer quel tri à la file actuelle? (1=Insertion, 2=Sélection, 0=Aucun): ").strip()
        
        if choix == "1":
            self.file_attente = file_insertion
            print(" Tri par insertion appliqué!")
        elif choix == "2":
            self.file_attente = file_selection
            print(" Tri par sélection appliqué!")
        else:
            print("Aucun changement appliqué.")
    
    def executer(self):
        """Boucle principale du programme"""
        print("Bienvenue au Centre de Tri des Colis!")
        print("Chargement du système...")
        
        # Ajouter quelques colis de démonstration
        self.ajouter_colis_aleatoire(3)
        
        while True:
            self.afficher_menu()
            choix = input("\nVotre choix: ").strip()
            
            if choix == "1":
                self.ajouter_colis_manuel()
            elif choix == "2":
                try:
                    nombre = int(input("Nombre de colis à générer: "))
                    if nombre > 0:
                        self.ajouter_colis_aleatoire(nombre)
                    else:
                        print(" Le nombre doit être positif")
                except ValueError:
                    print(" Veuillez entrer un nombre valide")
            elif choix == "3":
                self.traiter_colis()
            elif choix == "4":
                self.decharger_camion()
            elif choix == "5":
                self.file_attente.afficher()
            elif choix == "6":
                self.pile_chargement.afficher()
            elif choix == "7":
                self.trier_file()
            elif choix == "8":
                self.trier_pile()
            elif choix == "9":
                self.comparer_tris()
            elif choix == "0":
                print("\nMerci d'avoir utilisé le Centre de Tri des Colis!")
                print("Au revoir!")
                break
            else:
                print(" Choix invalide! Veuillez réessayer.")
            
            input("\nAppuyez sur Entrée pour continuer...")


def main():
    """Point d'entrée du programme"""
    try:
        centre = CentreTri()
        centre.executer()
    except KeyboardInterrupt:
        print("\n\nProgramme interrompu par l'utilisateur")
        sys.exit(0)
    except Exception as e:
        print(f"\n Une erreur est survenue: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()