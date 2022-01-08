import random                 
import string                   

from mots import mots           
from pendu_diagramme import vies_dictionnaire_visuel            


def obtenir_mot(mots):
    mot = random.choice(mots)  

    
    while '-' in mot or ' ' in mot:
        mot = random.choice(mots)

    return mot.upper()


def pendu():

    print("=======================================")
    print(" ¡Bienvenue au jeu du Pendu! ")
    print("=======================================")

    
    mot = obtenir_mot(mots)
    lettres_a_trouves = set(mot)  
    alphabet = set(string.ascii_uppercase)
    lettres_trouves = set()  

    vies = 7           



    while len(lettres_a_trouves) > 0 and vies > 0:

        
        print(f"il te reste {vies} vies et tu as utilisé ; ces lettres: {' '.join(lettres_trouves)}")

        mot_liste = [lettre if lettre in lettres_trouves else '-' for lettre in mot]
        print(vies_dictionnaire_visuel[vies]) 
        print(f"mot: {' '.join(mot_liste)}")

       
        mot_utilisateur = input('choisie une lettre: ').upper()

       

        if mot_utilisateur in alphabet - lettres_trouves:
            lettres_trouves.add(mot_utilisateur)
            
            if mot_utilisateur in lettres_a_trouves:
                lettres_a_trouves.remove(mot_utilisateur)
                print('')
            
            else:
                vies = vies - 1
                print(f"\nLa lettre {mot_utilisateur} n es pas dans ce mot.")
       
        elif mot_utilisateur in lettres_trouves:
            print("\nTa deja choisit ce mot , choisit une autre.")
        else:
            print("\ncet lettre n est pas valide.")

    
    if vies == 0:
        print(vies_dictionnaire_visuel [vies])
        print(f"¡PENDU! Tu as perdu. Le mot etait: {mot}")
    else:
        print(f'¡Bravo! ¡Le mot etait bien {mot}!')


if __name__ == '__main__':
    pendu()
