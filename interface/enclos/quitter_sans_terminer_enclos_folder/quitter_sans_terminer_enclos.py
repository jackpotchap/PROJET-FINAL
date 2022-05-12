####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DeserialisationAnimaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from interface.animaux.deserialisation_animaux_folder import deserialisation_animaux_interface

class DeserialisationAnimaux(QtWidgets.QDialog, deserialisation_animaux_interface.Ui_Dialog):
    """
    Classe : DetailAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(DeserialisationAnimaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Deserialisation d'un animaux")

    @pyqtSlot()
    def on_pushButton_quitter_deserialisation_animaux_clicked(self):
        self.close()
    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):

        reply = QMessageBox.question(self, "Quit", "La désérialisation en cours seras annulez.",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()