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


#code tiré exemple principalement vue en classe
def main():
    """
    Méthodes pour commencer le programme
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

