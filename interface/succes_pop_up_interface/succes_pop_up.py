####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe FenetrePrincipale
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface import fenetre_principale_interface, animaux

class FenetrePrincipale(QtWidgets.QMainWindow, fenetre_principale_interface.Ui_MainWindow):
    """
    Classe : FenetrePrincipale
    Héritant de Qtwidgets et de Ui_MainWindow
    """

    def __init__(self, parent=None):
        """Constructeur"""
        super(FenetrePrincipale, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Menu principale")

    @pyqtSlot()
    def on_pushButton_animaux_clicked(self):
        """
        fonction pour ouvrire la fenêtre de la section animaux du zoo
        """

        self.close()