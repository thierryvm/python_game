"""
Module pour le niveau 5 du jeu, abordant les listes et
les structures de données.
"""


def obtenir_nombres():
    """
    Demande à l'utilisateur d'entrer plusieurs nombres entiers séparés par
    des espaces.

    :return: Une liste de nombres entiers.
    """
    while True:
        try:
            entree = input("Entrez plusieurs nombres séparés "
                           "par des espaces : ").strip()
            if not entree:
                raise ValueError("Aucune entrée détectée.")

            nombres = [int(x) for x in entree.split()]
            if not nombres:
                raise ValueError("Aucun nombre n'a été entré.")

            return nombres
        except ValueError as e:
            print(f"Erreur : {e}. \nVeuillez entrer des nombres entiers "
                  "séparés par des espaces.")


def niveau5():
    """
    Fonction pour le niveau 5 du jeu.
    Ce niveau couvre les listes et les structures de données en demandant
    des nombres à l'utilisateur, en effectuant des opérations sur ces nombres,
    et en manipulant une liste de chaînes de caractères.
    """

    print("Niveau 5 : Listes et Structures de Données")

    # Demande à l'utilisateur d'entrer plusieurs nombres
    nombres = obtenir_nombres()

    print(f"\nLes nombres que tu as entrés sont : {nombres}")
    print(f"La somme des nombres est : {sum(nombres)}")
    print(f"Le nombre maximum est : {max(nombres)}")
    print(f"Le nombre minimum est : {min(nombres)}")

    # Manipulation d'une liste de chaînes
    fruits = ["pomme", "banane", "cerise", "fraise"]

    print("\nListe des fruits :")
    for fruit in fruits:
        print(fruit)


if __name__ == "__main__":
    niveau5()
