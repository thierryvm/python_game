"""
Module pour le niveau 2 du jeu, abordant les conditions.
"""

def niveau2():
    """
    Fonction pour le niveau 2 du jeu.
    Ce niveau couvre les conditions en demandant l'âge de l'utilisateur et en évaluant
    s'il est mineur, adulte, senior, jeune ou plus vieux.
    """

    print("Niveau 2 : Conditions")

    try:
        age = int(input("Quel est ton âge ? "))
    except ValueError:
        print("Veuillez entrer un nombre entier pour l'âge.")
        return  # Arrête la fonction si l'entrée est invalide

    if age < 18:
        print("Tu es mineur.")
    elif age < 60:
        print("Tu es adulte.")
    else:
        print("Tu es senior.")

    reponse = input("Voulez-vous savoir si vous êtes jeune ou vieux ? (oui/non) : ").strip().lower()

    if reponse == "oui":
        if age < 30:
            print("Tu es jeune.")
        else:
            print("Tu es plus vieux.")
    else:
        print("Merci d'avoir joué.")

# Lancer le niveau 2
niveau2()
