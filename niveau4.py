"""
Module pour le niveau 4 du jeu, abordant les fonctions.
"""

import re


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


def est_nom_valide(nom):
    """
    Vérifie si le nom est valide.
    :param nom: Le nom à vérifier.
    :return: True si le nom est valide, sinon False.
    """
    return bool(re.match(r'^[A-Za-zàâçéèêëîïôûùüÿñæœ\- ]+$', nom))


def est_age_valide(age):
    """
    Vérifie si l'âge est valide.
    :param age: L'âge à vérifier.
    :return: True si l'âge est valide, sinon False.
    """
    return 0 <= age <= 120


def niveau4():
    """
    Fonction pour le niveau 4 du jeu.
    Ce niveau couvre les fonctions en utilisant des opérations simples et
    des messages personnalisés.
    """

    print("Niveau 4 : Fonctions")

    # Vérification des entrées pour l'addition
    try:
        a = int(input("Entrez le premier nombre pour additionner : "))
        b = int(input("Entrez le deuxième nombre pour additionner : "))
    except ValueError:
        print("Veuillez entrer des nombres entiers.")
        return  # Arrête la fonction si l'entrée est invalide

    resultat = addition(a, b)
    print(f"Le résultat de {a} + {b} est {resultat}.")

    # Vérification des entrées pour le message personnalisé
    try:
        nom = input("Quel est ton nom ? ").strip()

        if not est_nom_valide(nom):
            print("Veuillez entrer un nom valide"
                  "(lettres, espaces, tirets seulement).")
            return

        age = int(input("Quel est ton âge ? "))

        if not est_age_valide(age):
            print("Veuillez entrer un âge valide (entre 0 et 120).")
            return
    except ValueError:
        print("Veuillez entrer un nombre entier pour l'âge.")
        return  # Arrête la fonction si l'entrée est invalide

    print(message_personnalise(nom, age))


if __name__ == "__main__":
    niveau4()
