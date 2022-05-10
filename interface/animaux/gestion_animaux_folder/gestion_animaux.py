####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe GestionAnimaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.animaux.gestion_animaux_folder import gestion_animaux_interface
from interface.animaux.create1_animaux_folder import create1_animaux
from interface.animaux.detail_animaux_folder import detail_animaux
from interface.animaux.deserialisation_animaux_folder import deserialisation_animaux



class GestionAnimaux(QtWidgets.QDialog, gestion_animaux_interface.Ui_Dialog):
    """
    Classe : GestionAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,p_caller,parent=None):
        """Constructeur
        : p_caller: permet de savoir de quelle fenetre il a été ouvert
        """

        super(GestionAnimaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Gestion animaux")

        self.caller = p_caller
    @pyqtSlot()
    def on_pushButton_cree_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'animaux
        """

        crea1_A_form = create1_animaux.Create1Animaux()

        crea1_A_form.show()
        crea1_A_form.exec()


    @pyqtSlot()
    def on_pushButton_modif_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de modification d'animaux
        """

        crea1_A_form = create1_animaux.Create1Animaux()

        crea1_A_form.show()
        crea1_A_form.exec()


    @pyqtSlot()
    def on_pushButton_detail_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'animaux
        """

        detail_A_form = detail_animaux.DetailAnimaux()

        detail_A_form.show()
        detail_A_form.exec()

    @pyqtSlot()
    def on_pushButton_deserialiser_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'animaux
        """
        print(1)
        Deser_A_form = deserialisation_animaux.DeserialisationAnimaux()

        Deser_A_form.show()
        Deser_A_form.exec()

    def on_pushButton_menu_principale_gestion_animaux_clicked(self):
        """
            fonction pour fermer la fenêtre de gestion animaux et remontrer le menu principale
        """
        self.caller.show()
        self.hide()