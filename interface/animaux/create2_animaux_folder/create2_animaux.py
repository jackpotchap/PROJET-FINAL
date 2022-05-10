####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe Create2Animaux
###################################################################################
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from interface.animaux.create2_animaux_folder import create2_animaux_interface
from PyQt5.QtWidgets import QMessageBox
import time
class Create2Animaux(QtWidgets.QDialog, create2_animaux_interface.Ui_Dialog):
    """
    Classe : Create2Animaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,p_caller,parent=None):
        """Constructeur
        : p_caller: la fenetre qui la appeler"""

        super(Create2Animaux, self).__init__(parent)
        self.setupUi(self)
        self.caller = p_caller
        self.bruteForceClose = False

        self.setWindowTitle("Gestion de Zoo - 2e étape de la création d'un animaux")

        self.setWindowModality(Qt.ApplicationModal)

    @pyqtSlot()
    def on_pushButton_retour_crea2_animaux_clicked(self):

        #pour eviter que lorsque l<utilisateur veut revenir en arrirer il recoit le message avertissement
        self.bruteForceClose = True

        self.close()


    def closeEvent(self, event):
        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "Tous changement effectuez seras perdu.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.caller.bruteForceClose = True

                event.accept()
            else:
                event.ignore()
