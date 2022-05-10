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
from interface.animaux.gestion_animaux_folder import gestion_animaux
from interface.enclos.gestion_enclos_folder import gestion_enclos

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

        gestion_A_form = gestion_animaux.GestionAnimaux(self)
        self.hide()
        gestion_A_form.show()
        gestion_A_form.exec()

    @pyqtSlot()
    def on_pushButton_enclos_clicked(self):
        """
        fonction pour ouvrire la fenêtre de la enclos du zoo
        """

        gestion_E_form = gestion_enclos.GestionEnclos()

        gestion_E_form.show()
        gestion_E_form.exec()

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        """
        fonction pour fermer le programe principale
        """

        self.close()