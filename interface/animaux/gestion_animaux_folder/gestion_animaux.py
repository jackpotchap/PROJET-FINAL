####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe GestionAnimaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.animaux.gestion_animaux_folder import gestion_animaux_interface

class GestionAnimaux(QtWidgets.QDialog, gestion_animaux_interface.Ui_Dialog):
    """
    Classe : GestionAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self, parent=None):
        """Constructeur"""

        super(GestionAnimaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Gestion animaux")