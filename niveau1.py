"""
Module pour le niveau 1 du jeu, abordant les variables et les types de données.
"""

def niveau1():
    """
    Fonction pour le niveau 1 du jeu.
    Ce niveau couvre les variables et les types de données à travers des exercices.
    """

    print("Niveau 1 : Variables et Types de Données")

    # Exercice 1 : Addition simple
    a = 5
    b = 10
    print(f"Quel est le résultat de {a} + {b} ?")
    reponse = input("Ta réponse : ")

    try:
        if int(reponse) == (a + b):
            print("Bonne réponse !")
        else:
            print(f"Mauvaise réponse. La bonne réponse était {a + b}.")
    except ValueError:
        print("Ce n'est pas un nombre valide. Veuillez entrer un nombre entier.")

    # Exercice 2 : Types de données
    nombre = input("Entre un nombre entier : ")
    texte = input("Entre une chaîne de caractères : ")

    print(f"Tu as entré le nombre {nombre} et le texte '{texte}'.")
    print(f"Le type de {nombre} est {type(nombre).__name__}.")
    print(f"Le type de {texte} est {type(texte).__name__}.")

# Lancer le niveau 1
niveau1()
