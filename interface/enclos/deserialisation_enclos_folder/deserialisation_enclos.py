####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DeserialisationEnclos
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from interface.enclos.deserialisation_enclos_folder import deserialisation_enclos_interface

class DeserialisationEnclos(QtWidgets.QDialog, deserialisation_enclos_interface.Ui_Dialog):
    """
    Classe : DeserialisationEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(DeserialisationEnclos, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Deserialisation d'un enclos")

    @pyqtSlot()
    def on_pushButton_quitter_deserialisation_enclos_clicked(self):
        self.close()
    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):

        reply = QMessageBox.question(self, "Quit", "La désérialisation en cours seras annulez.",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()