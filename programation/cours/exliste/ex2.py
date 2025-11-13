from datetime import datetime

def afficher_menu_principal():
    print("\n=== Menu Principal ===")
    print("0. Quitter le menu")
    print("1. Créer une nouvelle tâche")
    print("2. Afficher la liste des tâches")
    print("3. Afficher les tâches actives")
    print("4. Afficher les tâches terminées")
    print("5. Afficher les tâches comprises entre deux dates (yyyy-mm-dd)")
    print("6. Modifier une tâche existante")
    print("7. Supprimer une tâche de la liste")

def afficher_sous_menu_modification():
    print("\n=== Sous-menu : Modifier une tâche ===")
    print("0. Quitter le sous-menu")
    print("1. Modifier la date")
    print("2. Modifier l'heure")
    print("3. Modifier le statut (actif / terminé)")
    print("4. Modifier le nom de la tâche")
    print("5. Modifier la description de la tâche")

taches = [
    ["Révisions maths", "Réviser contrôle chapitre 2", "2025-09-25", "18:00", "actif"],
    ["Boxe thaï", "Aller à l'entraînement", "2025-09-26", "19:30", "terminé"]
]
    

    
def afficher_toutes_les_taches(taches):
    if not taches:
        print("\nAucune tâche disponible.")
        return
    
    print("\n=== Liste des tâches ===")
    for i, t in enumerate(taches, start=1):
        print(f"\nTâche {i} : {t[0]}")  
        print(f"  Description : {t[1]}")
        print(f"  Date        : {t[2]}")
        print(f"  Heure       : {t[3]}")
        print(f"  Statut      : {t[4]}")


afficher_toutes_les_taches(taches)


