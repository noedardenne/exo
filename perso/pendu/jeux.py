def jouer():
    mot = str(input("Donne un mot : "))
    nblettre = len(mot)
    mot2 = "_" * nblettre
    print(mot2)
    essaie = 6
    
    while essaie > 0:
        lettre = str(input("Donne une lettre : "))
        mot2_modif = ""
        
        if lettre in mot:
            for i in range(nblettre):
                if mot[i] == lettre:
                    mot2_modif += lettre 
                else:
                    mot2_modif += mot2[i]
            mot2 = mot2_modif
            print(mot2)
        else:
            print("Ya pas la lettre")
            essaie -= 1
            print(f"Tu as {essaie} essais restants")

        # dessin du pendu selon le nombre d'essais restants
        if essaie == 6:
            print("""
  +---+
  |   |
      |
      |
      |
      |
=========
""")
        elif essaie == 5:
            print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""")
        elif essaie == 4:
            print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""")
        elif essaie == 3:
            print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""")
        elif essaie == 2:
            print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""")
        elif essaie == 1:
            print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""")
        elif essaie == 0:
            print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")

        
        if mot2 == mot:
            print("Tu as gagné")
            break
    
    else:  
        print(f" Tu as perdu... Le mot était : {mot}")
