"""
Module pour le niveau 2 du jeu, abordant les conditions.
"""


def est_age_valide(age):
    """
    Vérifie si l'âge est un nombre entier valide et positif.

    :param age: L'âge à vérifier.
    :return: True si l'âge est un nombre entier positif, False sinon.
    """
    return isinstance(age, int) and age >= 0


def niveau2():
    """
    Fonction pour le niveau 2 du jeu.
    Ce niveau couvre les conditions en demandant l'âge de l'utilisateur et
    en évaluant s'il est mineur, adulte, senior, jeune ou plus vieux.
    """

    print("Niveau 2 : Conditions")

    while True:
        try:
            age = int(input("Quel est ton âge ? "))
            if est_age_valide(age):
                break
            else:
                print("Veuillez entrer un âge valide (nombre entier positif).")
        except ValueError:
            print("Veuillez entrer un nombre entier pour l'âge.")

    if age < 18:
        print("Tu es mineur.")
    elif age < 60:
        print("Tu es adulte.")
    else:
        print("Tu es senior.")

    while True:
        reponse = input(
            "Voulez-vous savoir avec quels personnages célèbres   "
            "vous vous comparez en fonction de votre âge ? (oui/non) : "
        ).strip().lower()

        if reponse == "oui":
            if age < 20:
                print(
                    "Tu es plus jeune que des célébrités comme Billie Eilish, "
                    "qui a révolutionné la musique à un jeune âge, "
                    "ou Finn Wolfhard, connu pour son rôle"
                    "dans 'Stranger Things'."
                )
            elif age < 30:
                print(
                    "Tu es dans la même tranche d'âge que des figures"
                    "influentes comme Zendaya, "
                    "une étoile montante dans le cinéma et la mode, "
                    "ou Timothée Chalamet, "
                    "un acteur acclamé."
                )
            elif age < 40:
                print(
                    "Tu partages ton âge avec des célébrités établies "
                    "comme Chris Hemsworth, "
                    "connu pour son rôle en tant que Thor, ou Rihanna, "
                    "une icône de la musique "
                    "et de la mode."
                )
            elif age < 50:
                print(
                    "Tu es dans la même tranche d'âge que des personnalités "
                    "influentes comme Elon Musk, "
                    "le visionnaire derrière Tesla et SpaceX, ou Oprah Winfrey"
                    ", une figure emblématique des médias."
                )
            elif age < 60:
                print(
                    "Tu es à peu près du même âge que des personnes  "
                    "influentes comme George Clooney, "
                    "un acteur et réalisateur respecté, ou Julia Roberts, "
                    "une star du cinéma mondialement "
                    "reconnue."
                )
            else:
                print(
                    "Tu partages ton âge avec des figures légendaires "
                    "comme Morgan Freeman, dont la "
                    "carrière impressionnante a marqué le cinéma, "
                    "ou Meryl Streep, considérée comme l'une "
                    "des plus grandes actrices de tous les temps."
                )
            break
        elif reponse == "non":
            print("Merci d'avoir joué. Passe une excellente journée !")
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")


if __name__ == "__main__":
    niveau2()
