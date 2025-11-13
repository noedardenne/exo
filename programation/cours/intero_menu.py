# sest le menu
menu=["0 quitter",
        "1 ajouter",
        "2 retirer",
        "3 afficher la liste"]
#sest la liste utilisateur
utilisateur=[]
#condition pour la boucle
bombo =True
while bombo==True:
# affichage du menu 
    print("=== MENU ===")
    for element in menu:
        print(element)
    choix=str(input("ecris un numero pour selectioner"))
# premier choix pour quitter 
    if choix=="0":
        bombo=False
        print("merci d'utiliser notre programe")
#deuxieme choix pour ajouter des nom au user
    elif choix=="1":
        ajout=str(input("ecrit un nouveau truc"))
        for i in utilisateur:
            if ajout==i:
                print("le nom d'utilisateur est pris")
            
        else :
              print("votre nom d'utilisateur a bien été ajouter")
              utilisateur.append(ajout)
# troisieme choix pour enlever des user  
    elif choix=="2":    
        enlever = input("Écris le texte exact à enlever : ")
        if enlever in utilisateur:
            utilisateur.remove(enlever)
            print(f"'{enlever}' retiré.")
            
        else:
            print(" Cet élément n'existe pas.")
#dernier choix pour afficher la liste
    elif choix=="3":
        indice=0
        for j in utilisateur:
            
            indice+=1
            print(f"[{indice}] {j}")
            
