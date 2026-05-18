salle = None

def initialiser_salle(nb_lig, nb_col):
    return [[0 for _ in range(nb_col)] for _ in range(nb_lig)]

def afficher(salle):
    print("\nPlan de la salle :")
    for i, ligne in enumerate(salle):
        print(i, end=" ")
        for place in ligne:
            print(place, end=" ")
        print()
    print("  " + " ".join(str(i) for i in range(len(salle[0]))))

def reserver_place(salle, lig, col):
    if salle[lig][col] == 0:
        salle[lig][col] = 1
        print(" Place réservée")
    else:
        print(" Place déjà prise")

def annuler_reservation(salle, lig, col):
    if salle[lig][col] == 1:
        salle[lig][col] = 0
        print(" Réservation annulée")
    else:
        print(" Cette place n'était pas réservée")

def verifier_place(salle, lig, col):
    if salle[lig][col] == 0:
        print(" Place libre")
    else:
        print(" Place occupée")

def compter_places(salle):
    libres = 0
    occupees = 0
    
    for ligne in salle:
        for place in ligne:
            if place == 0:
                libres += 1
            else:
                occupees += 1

    print(f"Places libres : {libres}")
    print(f"Places occupées : {occupees}")

def menu():
    print("\n--- MENU ---")
    print("0. Quitter le programme")
    print("1. Initialiser la salle")
    print("2. Afficher le plan de salle")
    print("3. Réserver une place")
    print("4. Annuler une réservation")
    print("5. Vérifier une place")
    print("6. Compter les places")

# PROGRAMME PRINCIPAL
mibombo = True

while mibombo:
    menu()
    choix = int(input("Donne un numéro stp: "))

    if choix == 0:
        mibombo = False

    elif choix == 1:
        if salle is not None:
            print(" Salle déjà initialisée")
        else:
            nb_lig = int(input("Nombre de lignes: "))
            nb_col = int(input("Nombre de colonnes: "))
            salle = initialiser_salle(nb_lig, nb_col)

    elif choix == 2:
        if salle is None:
            print(" Salle non initialisée")
        else:
            afficher(salle)

    elif choix == 3:
        if salle is None:
            print(" Initialise la salle d'abord")
        else:
            lig = int(input("Ligne: "))
            col = int(input("Colonne: "))
            reserver_place(salle, lig, col)

    elif choix == 4:
        if salle is None:
            print(" Initialise la salle d'abord")
        else:
            lig = int(input("Ligne: "))
            col = int(input("Colonne: "))
            annuler_reservation(salle, lig, col)

    elif choix == 5:
        if salle is None:
            print(" Initialise la salle d'abord")
        else:
            lig = int(input("Ligne: "))
            col = int(input("Colonne: "))
            verifier_place(salle, lig, col)

    elif choix == 6:
        if salle is None:
            print(" Initialise la salle d'abord")
        else:
            compter_places(salle)