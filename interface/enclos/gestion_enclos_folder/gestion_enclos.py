####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe GestionEnclos
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.enclos.gestion_enclos_folder import gestion_enclos_interface

class GestionEnclos(QtWidgets.QDialog, gestion_enclos_interface.Ui_Dialog):
    """
    Classe : GestionEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self, parent=None):
        """Constructeur"""

        super(GestionEnclos, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Gestion enclos")