####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DetailEnclos
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from interface.enclos.detail_enclos_folder import detail_enclos_interface
from interface.enclos.list_selection_animaux_enclos_folder import list_selection_animaux_enclos
class DetailEnclos(QtWidgets.QDialog, detail_enclos_interface.Ui_Dialog):
    """
    Classe : DetailEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(DetailEnclos, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Detail d'un Enclos")

    @pyqtSlot()
    def on_pushButton_ajouter_animaux_detail_enclo_clicked(self):
        """Fonction pour ajouter un animal a l'enclos """
        ajoute_A_form = list_selection_animaux_enclos.SelectionAnimaux()

        ajoute_A_form.show()
        ajoute_A_form.exec()
