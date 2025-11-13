menu=["1 afficher liste",
        "2 afficher mot prefixe",
        "3 afficher la def dun mot",
        "4 ajouter un nouveau mot et sa def",
        "5 modifier la def dun mot",
        "6 sup un mot de la liste",
        "7 quitter"]
mots=["mot1","mot2"]
definitions=["def du mot1","def du mot2"]



bombo =True
while bombo==True:
    print("=== MENU ===")
    for element in menu:
        print(element)    
    
    choix=str(input("ecris un numero pour selectioner"))
    
    if choix=="1":
        for i in range(len(mots)):
            print(mots[i])

    
    elif choix == "2":
        prefixe = input("Donne une lettre : ")
        trouve = False
        for mot in mots:
            if mot[0] == prefixe:  
                print(mot)
                trouve = True
        if not trouve:
            print(f"Y a pas de mot qui commence par {prefixe}")
    
    elif choix == "3":
        mot = input("Donne le mot dont tu veux la définition : ")
        if mot in mots:
            index = mots.index(mot)   
            print(definitions[index])        
        else:
            print(f"Le mot '{mot}' n'est pas dans la liste.")
    elif choix =="4":
        mot=str(input("donne moi le mot que tu veux rajouter"))        
        definition=str(input("donne moi la def que tu veux rajouter"))
        mots.append(mot)
        definitions.append(definition)
    elif choix =="5":
        mot = input("Donne le mot dont tu veux modif la définition : ")
        if mot in mots:
            index = mots.index(mot)
            print(f"la definition que tu va modif est {definitions[index]}")
            nouveau=str(input("donne la nouvel def"))
            definitions[index]=nouveau
            print(f"La définition du mot '{mot}' a été mise à jour. sest maintenant {nouveau}")
        else:   
            print(f"Le mot '{mot}' n'est pas dans la liste.")
    elif choix =="6":        
        enlever = input("Donne le mot a enlever stp : ")
        if enlever in mots:
            index = mots.index(enlever)
            mots.pop(index)
            definitions.pop(index)
            
        

