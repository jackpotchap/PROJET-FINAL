####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe SelectionAnimaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from interface.enclos.list_selection_animaux_enclos_folder import list_selection_animaux_enclos_interface
from interface.animaux.detail_animaux_folder import detail_animaux
class SelectionAnimaux(QtWidgets.QDialog, list_selection_animaux_enclos_interface.Ui_Dialog):
    """
    Classe : DetailAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(SelectionAnimaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Selection d'un animal")

        self.bruteForceClose = False
    @pyqtSlot()
    def on_pushButton_ajouter_list_animaux_enclos_clicked(self):
        self.bruteForceClose = True
        self.close()

    @pyqtSlot()
    def on_pushButton_detail_list_animaux_enclos_clicked(self):
        detail_A_form = detail_animaux.DetailAnimaux()

        detail_A_form.show()
        detail_A_form.exec()

    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):
        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "L'ajouts d'animaux en cours seras annulez.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()