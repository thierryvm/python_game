"""
Module pour le niveau 5 du jeu, abordant les listes et les structures de données.
"""

def niveau5():
    """
    Fonction pour le niveau 5 du jeu.
    Ce niveau couvre les listes et les structures de données en demandant des nombres à l'utilisateur,
    en effectuant des opérations sur ces nombres, et en manipulant une liste de chaînes de caractères.
    """

    print("Niveau 5 : Listes et Structures de Données")

    # Demande à l'utilisateur d'entrer plusieurs nombres
    try:
        nombres = [int(x) for x in input("Entrez plusieurs nombres séparés par des espaces : ").split()]
        if not nombres:
            raise ValueError("Aucun nombre n'a été entré.")
    except ValueError as e:
        print(f"Erreur : {e}. Veuillez entrer des nombres entiers séparés par des espaces.")
        return  # Arrête la fonction si l'entrée est invalide

    print(f"Les nombres que tu as entrés sont : {nombres}")
    print(f"La somme des nombres est : {sum(nombres)}")
    print(f"Le nombre maximum est : {max(nombres)}")
    print(f"Le nombre minimum est : {min(nombres)}")

    # Manipulation d'une liste de chaînes
    fruits = ["pomme", "banane", "cerise"]
    print("Liste des fruits :")
    for fruit in fruits:
        print(fruit)

# Lancer le niveau 5
niveau5()
