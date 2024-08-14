"""
Module pour le niveau 3 du jeu, abordant les boucles.
"""

def niveau3():
    """
    Fonction pour le niveau 3 du jeu.
    Ce niveau couvre les boucles en demandant une série de nombres pour calculer
    leur somme et en affichant la table de multiplication d'un nombre positif.
    """

    print("Niveau 3 : Boucles")

    # Calcul de la somme des nombres
    somme = 0
    for i in range(1, 6):
        try:
            nombre = int(input(f"Entrez le nombre {i} : "))
            somme += nombre
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
            return  # Arrête la fonction si l'entrée est invalide

    print(f"La somme de tes nombres est {somme}.")

    # Exercice avec boucle while
    try:
        nombre = int(input("Entre un nombre positif pour voir sa table de multiplication : "))
        if nombre <= 0:
            print("Veuillez entrer un nombre positif.")
            return  # Arrête la fonction si l'entrée est invalide
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return  # Arrête la fonction si l'entrée est invalide

    i = 1
    while i <= 10:
        print(f"{nombre} x {i} = {nombre * i}")
        i += 1

# Lancer le niveau 3
niveau3()
