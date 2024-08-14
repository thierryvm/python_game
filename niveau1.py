"""
Niveau 1 : Variables et Types de Données
"""

def niveau1():
    """
    Exerce les concepts de variables et types de données avec des exercices interactifs.
    """
    print("Niveau 1 : Variables et Types de Données")
    
    # Exercice 1 : Addition simple
    a = 5
    b = 10
    print(f"Quel est le résultat de {a} + {b} ?")
    reponse = input("Ta réponse : ")
    
    if int(reponse) == (a + b):
        print("Bonne réponse !")
    else:
        print(f"Mauvaise réponse. La bonne réponse était {a + b}.")
        
    # Exercice 2 : Types de données
    nombre = input("Entre un nombre entier : ")
    texte = input("Entre une chaîne de caractères : ")
    
    print(f"Tu as entré le nombre {nombre} et le texte '{texte}'.")
    print(f"Le type de {nombre} est {type(nombre)}.")
    print(f"Le type de {texte} est {type(texte)}.")
    
# Lancer le niveau 1
niveau1()
