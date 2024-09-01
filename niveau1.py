"""
Niveau 1 : Variables et Types de Données

Ce niveau exerce les concepts de variables et types de données avec
des exercices interactifs en demandant à l'utilisateur de travailler
avec différents types de données, y compris les entiers,
les flottants, les booléens, et les chaînes de caractères.
"""

import random


def est_chaine_valide(valeur):
    """
    Vérifie si la valeur est une chaîne de caractères composée uniquement
    de lettres alphabétiques.

    :param valeur: La valeur à vérifier.
    :return: True si la valeur est une chaîne de caractères contenant
    uniquement des lettres, False sinon.
    # isalpha: Vérifie si tous les caractères dans valeur sont des lettres
    """
    return valeur.isalpha() and len(valeur) > 0


def est_boolean_valide(valeur):
    """
    Vérifie si la valeur est un booléen valide ('True' ou 'False').

    :param valeur: La valeur à vérifier.
    :return: True si la valeur est 'True' ou 'False' (en majuscule),
    False sinon.
    """
    return valeur in ['True', 'False']


def niveau1():
    """
    Exerce les concepts de variables et types de données avec
    des exercices interactifs.
    """
    print("Niveau 1 : Variables et Types de Données")

    # Exercice 1 : Addition aléatoire
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"Quel est le résultat de {a} + {b} ?")

    while True:
        try:
            reponse = int(input("Ta réponse : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    if reponse == (a + b):
        print("Bonne réponse !")
    else:
        print(f"Mauvaise réponse. La bonne réponse était {a + b}.")

    # Exercice 2 : Types de données
    while True:
        try:
            nombre_entier = int(input("Entre un nombre entier : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    while True:
        try:
            nombre_float = float(input("Entre un nombre flottant : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre flottant valide.")

    while True:
        texte = input(
            "Entre une chaîne de caractères (lettres seulement) : "
        )
        if est_chaine_valide(texte):
            break
        else:
            print(
                "Veuillez entrer une chaîne de caractères contenant "
                "uniquement des lettres."
            )

    while True:
        boolean_str = input("Entre un booléen (True ou False) : ").capitalize()
        if est_boolean_valide(boolean_str):
            boolean_val = boolean_str == 'True'
            break
        else:
            print("Veuillez entrer 'True' ou 'False'.")

    print(
        f"Tu as entré le nombre entier {nombre_entier},"
        f"le nombre flottant {nombre_float}, "
        f"le texte '{texte}', et le booléen {boolean_val}."
    )
    print(
        f"Le type de {nombre_entier} est {type(nombre_entier)}."
    )
    print(
        f"Le type de {nombre_float} est {type(nombre_float)}."
    )
    print(
        f"Le type de {texte} est {type(texte)}."
    )
    print(
        f"Le type de {boolean_val} est {type(boolean_val)}."
    )


if __name__ == "__main__":
    niveau1()
