####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe Create1Animaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.animaux.create1_animaux_folder import create1_animaux_interface

class Create1Animaux(QtWidgets.QDialog, create1_animaux_interface.Ui_Dialog):
    """
    Classe : GestionAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(Create1Animaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - 1er étape de la création d'un animaux")


