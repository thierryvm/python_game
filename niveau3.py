"""
Module pour le niveau 3 du jeu, abordant les boucles.
"""


def obtenir_nombre_entier(prompt, valeur_min=None):
    """
    Demande à l'utilisateur de saisir un nombre entier valide.

    :param prompt: Le message à afficher à l'utilisateur.
    :param valeur_min: La valeur minimale que le nombre doit avoir
    (si spécifié).
    :return: Le nombre entier saisi par l'utilisateur.
    """
    while True:
        try:
            nombre = int(input(prompt))
            if valeur_min is not None and nombre <= valeur_min:
                print(f"Veuillez entrer un nombre supérieur à {valeur_min}.")
            else:
                return nombre
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def niveau3():
    """
    Fonction pour le niveau 3 du jeu.
    Ce niveau couvre les boucles en demandant une série de nombres
    pour calculer
    leur somme et en affichant la table de multiplication d'un nombre positif.
    """

    print("Niveau 3 : Boucles")

    # Calcul de la somme des nombres
    somme = 0
    nombres = ["premier", "second", "troisième", "quatrième", "cinquième"]
    for i in range(5):
        prompt = f"Entrez le {nombres[i]} nombre de la série : "
        nombre = obtenir_nombre_entier(prompt)
        somme += nombre

    print(f"La somme de tes nombres est {somme}.")

    # Exercice avec boucle while
    prompt = "Entre un nombre positif pour voir sa table de multiplication : "
    nombre = obtenir_nombre_entier(prompt, valeur_min=0)

    print(f"Table de multiplication de {nombre} :")
    i = 1
    while i <= 10:
        print(f"{nombre} x {i} = {nombre * i}")
        i += 1


if __name__ == "__main__":
    niveau3()
