####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe CreateEnclos
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from interface.enclos.create_enclos_folder import create_enclos_interface

class CreateEnclos(QtWidgets.QDialog, create_enclos_interface.Ui_Dialog):
    """
    Classe : CreateEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(CreateEnclos, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Create enclos")
        self.bruteForceClose = False

    @pyqtSlot()
    def on_pushButton_annulez_crea_enclos_clicked(self):
        self.close()

    def on_pushButton_valider_crea_enclos_clicked(self):
        self.bruteForceClose = True
        self.close()

    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):

        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "Tous changement effectuez seras perdu.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()