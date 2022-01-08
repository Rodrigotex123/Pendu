import random                   #on importe le module random
import string                   #on importe le module string ; pour avoir des chaine des caracteres , qui contient tous les lettres en mayuscule

from mots import mots           #on importe la liste des mots de la variable mots qui se trouve dans mots.py
from pendu_diagramme import vies_dictionnaire_visuel            #on importe le diagramme du pendu qui se trouve dans la variable vies_dictionnaire_visuel


def obtenir_mot(mots):
    mot = random.choice(mots)  # seleccioner un mot au hazard de la liste

    # Si le mot contient un - ou un ' ',
    # on choisit un autre mot au hazard.
    while '-' in mot or ' ' in mot:
        mot = random.choice(mots)

    return mot.upper()


def pendu():

    print("=======================================")
    print(" ¡Bienvenue au jeu du Pendu! ")
    print("=======================================")

    #pour ne pas repeter les mots
    mot = obtenir_mot(mots)
    lettres_a_trouves = set(mot)  # set est un ensemble de clefs
    alphabet = set(string.ascii_uppercase)
    lettres_trouves = set()  # lettres qu on a trouves

    vies = 7            #vies totale



    while len(lettres_a_trouves) > 0 and vies > 0:

        # ' '.join(['a', 'b', 'c']) --> 'a b c'
        print(f"il te reste {vies} vies et tu as utilisé ; ces lettres: {' '.join(lettres_trouves)}")

        # Etat du mot a trouve  (par exemple:  H - L A)
        mot_liste = [lettre if lettre in lettres_trouves else '-' for lettre in mot]
        print(vies_dictionnaire_visuel[vies]) # montrer l etat du pendu
        print(f"mot: {' '.join(mot_liste)}")

        # l utilisateur choisie une lettre
        mot_utilisateur = input('choisie une lettre: ').upper()

        #si la lettre choisit par l utilisateur est dans la variable alphabet et n es pas dans
        #la variable lettres_trouves on place cet lettre ; dans la variable lettres_trouves

        if mot_utilisateur in alphabet - lettres_trouves:
            lettres_trouves.add(mot_utilisateur)
            # Si la lettre est dans le mot qu il faut trouver ;
            # ceci enleve cet lettre de la variable lettre_a_trouves
            if mot_utilisateur in lettres_a_trouves:
                lettres_a_trouves.remove(mot_utilisateur)
                print('')
            # Si la letrtre n es pas dans le mot ; ceci enleve une vie.
            else:
                vies = vies - 1
                print(f"\nLa lettre {mot_utilisateur} n es pas dans ce mot.")
        # si la lettre choisit a deja etait utilise.
        elif mot_utilisateur in lettres_trouves:
            print("\nTa deja choisit ce mot , choisit une autre.")
        else:
            print("\ncet lettre n est pas valide.")

    # On arrive ici quand on a plus de vie ou
    # quand on a trouve tous les lettres du mot.
    if vies == 0:
        print(vies_dictionnaire_visuel [vies])
        print(f"¡PENDU! Tu as perdu. Le mot etait: {mot}")
    else:
        print(f'¡Bravo! ¡Le mot etait bien {mot}!')


if __name__ == '__main__':
    pendu()
