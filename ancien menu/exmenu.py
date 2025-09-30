liste=["1 ajouter",
        "2 retirer",
        "3 quitter"]
liste1=["mot1"]
bombo =True
while bombo==True:
    print("=== MENU ===")
    for element in liste:   
        print(element)
    print("=== MOTS ===") 
    for element1 in liste1:
        print(element1)    
    choix=str(input("ecris un numero pour selectioner"))
    if choix=="1":
        ajout=str(input("ecrit un nouveau truc"))
        liste1.append(ajout)
    elif choix=="2":
        enlever = input("Écris le texte exact à enlever : ")
        if enlever in liste1:
            liste1.remove(enlever)
            print(f"'{enlever}' retiré.")
            
        else:
            print(" Cet élément n'existe pas.")

    elif choix=="3":
        bombo=False      



