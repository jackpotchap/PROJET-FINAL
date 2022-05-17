####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe GestionAnimaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QEvent
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import inventaire
from interface.animaux.gestion_animaux_folder import gestion_animaux_interface
from interface.animaux.create1_animaux_folder import create1_animaux
from interface.animaux.detail_animaux_folder import detail_animaux
from interface.animaux.deserialisation_animaux_folder import deserialisation_animaux

def refresh_list_view(window, list_animaux):
    #code inspirer d'information vue en classe
    model = QStandardItemModel()
    window.listView_recherche_gestion_animaux.setModel(model)
    for a in list_animaux:
        print(str(type(a)))
        item = QStandardItem(a.Id_animal + " - " + a.Nom_animal + " - " + inventaire.dict_translate_object_to_dict[type(a)])
        model.appendRow(item)

def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_selection_erreure_gestion_animaux.setVisible(False)
    window.label_format_erreure_id_recherche_gestion_animaux.setVisible(False)

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
        cacher_lables_erreure(self)
        self.lineEdit_recherche_id_gestion_animaux.installEventFilter(self)
        self.setWindowTitle("Gestion de Zoo - Gestion animaux")
        refresh_list_view(self, inventaire.ls_animaux)
        self.caller = p_caller

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
                source is self.lineEdit_recherche_id_gestion_animaux):
            refresh_list_view(self,)
        return super(GestionAnimaux, self).eventFilter(source, event)

    @pyqtSlot()
    def on_pushButton_cree_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'animaux
        """


        crea1_A_form = create1_animaux.Create1Animaux()

        crea1_A_form.show()
        crea1_A_form.exec()
        refresh_list_view(self, inventaire.ls_animaux)


    @pyqtSlot()
    def on_pushButton_modif_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de modification d'animaux
        """
        cacher_lables_erreure(self)
        if self.listView_recherche_gestion_animaux.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_animaux.setVisible(True)

        else:
            crea1_A_form = create1_animaux.Create1Animaux(p_animal=inventaire.ls_animaux[self.listView_recherche_gestion_animaux.currentIndex().row()])

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

        Deser_A_form = deserialisation_animaux.DeserialisationAnimaux()

        Deser_A_form.show()
        Deser_A_form.exec()

    def on_pushButton_menu_principale_gestion_animaux_clicked(self):
        """
            fonction pour fermer la fenêtre de gestion animaux et remontrer le menu principale
        """
        self.caller.show()
        self.hide()