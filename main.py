"""
Jeu éducatif pour apprendre les bases de la programmation.

Ce script sert de point d'entrée pour le jeu éducatif. Il affiche un menu
principal permettant à l'utilisateur de sélectionner différents niveaux
d'apprentissage en programmation. Chaque niveau est implémenté dans
des modules séparés (niveau1, niveau2, niveau3, niveau4, niveau5) et couvre
des concepts fondamentaux tels que les variables, les conditions, les boucles,
les fonctions et les listes.

Le script importe les modules nécessaires pour chaque niveau et appelle
la fonction `menu` pour afficher les options disponibles et gérer
les sélections de l'utilisateur.
La boucle continue jusqu'à ce que l'utilisateur choisisse de quitter le jeu.

Modules importés :
- sys : Pour gérer la sortie du programme.
- niveau1 : Contient les exercices pour le niveau 1.
- niveau2 : Contient les exercices pour le niveau 2.
- niveau3 : Contient les exercices pour le niveau 3.
- niveau4 : Contient les exercices pour le niveau 4.
- niveau5 : Contient les exercices pour le niveau 5.

Fonctions :
- menu() : Affiche le menu principal et gère la sélection des niveaux de jeu.
"""

import sys
import niveau1
import niveau2
import niveau3
import niveau4
import niveau5


def menu():
    """
    Affiche le menu principal et gère la sélection des niveaux de jeu.
    """
    while True:
        print("\nMenu du Jeu de Programmation")
        print("1. Niveau 1 : Variables et Types de Données")
        print("2. Niveau 2 : Conditions")
        print("3. Niveau 3 : Boucles")
        print("4. Niveau 4 : Fonctions")
        print("5. Niveau 5 : Listes et Structures de Données")
        print("6. Quitter")

        choix = input("Choisis un niveau (1-6) : ")

        if choix == '1':
            niveau1.niveau1()
        elif choix == '2':
            niveau2.niveau2()
        elif choix == '3':
            niveau3.niveau3()
        elif choix == '4':
            niveau4.niveau4()
        elif choix == '5':
            niveau5.niveau5()
        elif choix == '6':
            print("Merci d'avoir joué !")
            sys.exit()
        else:
            print("Choix invalide. Essaie encore.")


if __name__ == "__main__":
    menu()
