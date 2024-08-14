"""
Module pour le niveau 4 du jeu, abordant les fonctions.
"""

def addition(a, b):
    """
    Additionne deux nombres.

    :param a: Le premier nombre.
    :param b: Le deuxième nombre.
    :return: La somme de a et b.
    """
    return a + b

def message_personnalise(nom, age):
    """
    Crée un message personnalisé avec le nom et l'âge.

    :param nom: Le nom de la personne.
    :param age: L'âge de la personne.
    :return: Un message de salutation personnalisé.
    """
    return f"Bonjour {nom}, tu as {age} ans."

def niveau4():
    """
    Fonction pour le niveau 4 du jeu.
    Ce niveau couvre les fonctions en utilisant des opérations simples et 
    des messages personnalisés.
    """

    print("Niveau 4 : Fonctions")

    try:
        a = int(input("Entrez le premier nombre pour additionner : "))
        b = int(input("Entrez le deuxième nombre pour additionner : "))
    except ValueError:
        print("Veuillez entrer des nombres entiers.")
        return  # Arrête la fonction si l'entrée est invalide

    resultat = addition(a, b)
    print(f"Le résultat de {a} + {b} est {resultat}.")

    try:
        nom = input("Quel est ton nom ? ").strip()
        age = int(input("Quel est ton âge ? "))
    except ValueError:
        print("Veuillez entrer un nombre entier pour l'âge.")
        return  # Arrête la fonction si l'entrée est invalide

    print(message_personnalise(nom, age))

# Lancer le niveau 4
niveau4()
