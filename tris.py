def tri_insertion_file(file):
    elements = file.get_elements()
    n = len(elements)
    for i in range(1, n):
        colis_courant = elements[i]

        j = i - 1
        while j >= 0 and (
            elements[j].priorite < colis_courant.priorite or  
            (elements[j].priorite == colis_courant.priorite and elements[j].ordre_arrivee > colis_courant.ordre_arrivee)):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = colis_courant
    file.set_elements(elements)
    print("Tri par insertion terminé!")

def tri_selection_file(file):
    elements = file.get_elements()
    n = len(elements)
    for i in range(n - 1):
        index_max = i
        
        for j in range(i + 1, n):
            if elements[j].priorite > elements[index_max].priorite:
                index_max = j
            elif (elements[j].priorite == elements[index_max].priorite and
                  elements[j].ordre_arrivee < elements[index_max].ordre_arrivee):
                index_max = j
        if index_max != i:
            elements[i], elements[index_max] = elements[index_max], elements[i]
    
    file.set_elements(elements)
    print("Tri par sélection terminé!")

def tri_insertion_pile(pile, croissant=True):
    elements_temp = []
    while not pile.est_vide():
        elements_temp.append(pile.depiler())
    
    elements = list(reversed(elements_temp))
    n = len(elements)

    for i in range(1, n):
        colis_courant = elements[i]
        j = i - 1

        if croissant:
            while j >= 0 and elements[j].poids > colis_courant.poids:
                elements[j + 1] = elements[j]
                j -= 1
        else:
            while j >= 0 and elements[j].poids < colis_courant.poids:
                elements[j + 1] = elements[j]
                j -= 1
        elements[j + 1] = colis_courant
    for colis in elements:
        pile.empiler(colis)
    
    ordre = "croissant" if croissant else "décroissant"
    print(f"Tri par insertion (poids {ordre}) termine!")

def tri_selection_pile(pile, croissant=True):
    elements_temp = []
    while not pile.est_vide():
        elements_temp.append(pile.depiler())

    elements = list(reversed(elements_temp))
    n = len(elements)

    for i in range(n - 1):
        index_extremum = i 
        
        for j in range(i + 1, n):
            if croissant:
                if elements[j].poids < elements[index_extremum].poids:
                    index_extremum = j
            else:
                if elements[j].poids > elements[index_extremum].poids:
                    index_extremum = j

        if index_extremum != i:
            elements[i], elements[index_extremum] = elements[index_extremum], elements[i]

    for colis in elements:
        pile.empiler(colis)
    
    ordre = "croissant" if croissant else "décroissant"
    print(f"Tri par sélection (poids {ordre}) terminé!")
    


""" tri par """

