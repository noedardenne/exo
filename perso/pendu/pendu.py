import menu as m
import jeux

jeu =True
while jeu==True:
    m.menu()
    choix=str(input("ecris un numero pour selectioner"))
    if choix=="1":
        jeux.jouer()
    elif choix=="2":
        m.regle()
    elif choix=="3":
        jeu=False        