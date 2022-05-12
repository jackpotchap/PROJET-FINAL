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
from interface.enclos.create_enclos_folder import create_enclos
from interface.enclos.detail_enclos_folder import detail_enclos
from interface.enclos.deserialisation_enclos_folder import deserialisation_enclos

class GestionEnclos(QtWidgets.QDialog, gestion_enclos_interface.Ui_Dialog):
    """
    Classe : GestionEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self, p_caller,parent=None):
        """Constructeur"""

        super(GestionEnclos, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Gestion enclos")

        self.caller = p_caller
    @pyqtSlot()
    def on_pushButton_cree_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'enclos
        """

        crea_A_form = create_enclos.CreateEnclos()

        crea_A_form.show()
        crea_A_form.exec()

    @pyqtSlot()
    def on_pushButton_modif_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'enclos puisque ses la meme que modification
        """

        crea_A_form = create_enclos.CreateEnclos()

        crea_A_form.show()
        crea_A_form.exec()

    @pyqtSlot()
    def on_pushButton_detail_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'enclos
        """
        print("hit")
        detail_E_form = detail_enclos.DetailEnclos()

        detail_E_form.show()
        detail_E_form.exec()

    @pyqtSlot()
    def on_pushButton_deserialiser_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'enclos
        """
        print(1)
        Deser_E_form = deserialisation_enclos.DeserialisationEnclos()

        Deser_E_form.show()
        Deser_E_form.exec()

    @pyqtSlot()
    def on_pushButton_menu_principale_gestion_enclos_clicked(self):
        """
            fonction pour fermer la fenêtre de gestion enclos et remontrer le menu principale
        """
        self.caller.show()
        self.hide()