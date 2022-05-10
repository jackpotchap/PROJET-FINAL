####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: le fichier a executer pour commencer l'aplication
###################################################################################

import sys
from animaux import animal
import enclos
from inventaire import ls_animaux, ls_enclos
from PyQt5 import QtWidgets
from interface.fenetre_principale_folder import fenetre_principale


def deserialiser_enclos(p_fichier):
    """
    Fonction qui permet de deserialier un enclo et l'integraliter des animaux qu'il contenait
    : p_fichier: le nom du fichier contenant l'enclo
    """
    enclo = enclos.Enclos()
    ls_animaux_t = enclo.deserialiser(p_fichier, [])
    for a in ls_animaux_t:
        a_t = animal.Animal(enclo, a["_Animal__poid_animal"], a["_Animal__nom_animal"], a["_Animal__espece_animal"], a["_Animal__id_animal"])
        ls_animaux.append(a_t)
    return enclo



def main():
    """
    Méthodes pour commence le programme
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetre_principale.FenetrePrincipale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()


if __name__ == "__main__":
    main()

