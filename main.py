"""
Menu principal du jeu éducatif pour apprendre les bases de la programmation.
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

# Lancer le menu
menu()
