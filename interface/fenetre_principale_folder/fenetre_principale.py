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
from interface.fenetre_principale_folder import fenetre_principale_interface
from interface.animaux import gestion_animaux_folder

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
        gestion_animaux_folder.gestion_animaux.
        self.close()