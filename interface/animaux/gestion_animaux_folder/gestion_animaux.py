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
from interface.succes_pop_up_interface_folder import succes_pop_up
import pathlib


def refresh_list_view(window, list_animaux):
    #code inspirer d'information vue en classe
    model = QStandardItemModel()
    window.listView_recherche_gestion_animaux.setModel(model)
    for a in list_animaux:
        print(list_animaux)
        item = QStandardItem(a.Id_animal + " - " + a.Nom_animal + " - " + inventaire.dict_translate_object_to_dict[type(a)])
        model.appendRow(item)

def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_selection_erreure_gestion_animaux.setVisible(False)
    window.label_format_erreure_id_recherche_gestion_animaux.setVisible(False)

def filtre(window,nouvelle_entree):
    list_filtrer = []

    print(len(window.lineEdit_recherche_id_gestion_animaux.text()))
    for a in inventaire.ls_animaux:

        toute_trouver = True
        if nouvelle_entree == "\x08":
            text = window.lineEdit_recherche_id_gestion_animaux.text()[0:-1]
            print(window.lineEdit_recherche_id_gestion_animaux.text()[0:-1])
        else:
            text = window.lineEdit_recherche_id_gestion_animaux.text() + nouvelle_entree
        for lettre in text:

            if a.Id_animal.lower().find(lettre.lower()) != -1:
                pass
            else:
                toute_trouver = False
        if toute_trouver:
            if window.comboBox_recherche_ecosysteme_gestion_animaux.currentText() == \
                    inventaire.dict_translate_object_to_dict[type(a)] \
                    or window.comboBox_recherche_ecosysteme_gestion_animaux.currentText() == "None":
                list_filtrer.append(a)
    return list_filtrer

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
        print(self.listView_recherche_gestion_animaux.currentIndex().row())
        classe = list(inventaire.dict_classe_animaux)
        classe.append("None")
        for c in classe:
            self.comboBox_recherche_ecosysteme_gestion_animaux.addItem(c)

        self.comboBox_recherche_ecosysteme_gestion_animaux.setCurrentIndex(len(classe)-1)
        #code qui permet de mettre un event lorsque la combobox changeras de selection
        #code trouver sur https://stackoverflow.com/questions/44707794/pyqt-combo-box-change-value-of-a-label
        self.comboBox_recherche_ecosysteme_gestion_animaux.currentTextChanged.connect(self.on_comboBox_recherche_ecosysteme_gestion_animaux_changed)



    #code qui permet de rafraichire la list view lorsque l'utilisateur écrit dans le line edit recherch id
    #code trouver sur https://stackoverflow.com/questions/46505769/pyqt-keypress-event-in-lineedit
    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
                source is self.lineEdit_recherche_id_gestion_animaux):

            refresh_list_view(self, filtre(self, event.text()))
        return super(GestionAnimaux, self).eventFilter(source, event)

    @pyqtSlot()
    def on_comboBox_recherche_ecosysteme_gestion_animaux_changed(self):
        refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_cree_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'animaux
        """

        cacher_lables_erreure(self)
        crea1_A_form = create1_animaux.Create1Animaux()

        crea1_A_form.show()
        crea1_A_form.exec()
        refresh_list_view(self, filtre(self, ""))


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
            refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_sup_gestion_animaux_clicked(self):
        cacher_lables_erreure(self)
        if self.listView_recherche_gestion_animaux.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_animaux.setVisible(True)
        else:
            inventaire.ls_animaux.remove(inventaire.ls_animaux[self.listView_recherche_gestion_animaux.currentIndex().row()])
            refresh_list_view(self, filtre(self, ""))


    @pyqtSlot()
    def on_pushButton_detail_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'animaux
        """

        if self.listView_recherche_gestion_animaux.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_animaux.setVisible(True)
        else:
            detail_A_form = detail_animaux.DetailAnimaux(inventaire.ls_animaux[self.listView_recherche_gestion_animaux.currentIndex().row()])

            detail_A_form.show()
            detail_A_form.exec()

    @pyqtSlot()
    def on_pushButton_serialiser_gestion_animaux_clicked(self):
        """
                fonction pour sérialiser un animal
        """
        if self.listView_recherche_gestion_animaux.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_animaux.setVisible(True)
        else:
            resulta = 0
            try:
                animal_t = inventaire.ls_animaux[self.listView_recherche_gestion_animaux.currentIndex().row()]
                nom_du_fichier = animal_t.Nom_animal +"_"+ animal_t.Id_animal +"_"+ animal_t.Espece
                path = str(pathlib.Path().resolve()) +"\\Serialiser\\" + nom_du_fichier
                #code trouver sur https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
                #pour avoir seulement le directory dans le quelle on travail
                animal_t.serialiser(path)
            except:
                resulta = 1

            Sucess_A_form = succes_pop_up.SuccesPopUpInterface(resulta)
            Sucess_A_form.show()
            Sucess_A_form.exec()
            refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_deserialiser_gestion_animaux_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'animaux
        """

        Deser_A_form = deserialisation_animaux.DeserialisationAnimaux()

        Deser_A_form.show()
        Deser_A_form.exec()
        refresh_list_view(self, filtre(self, ""))

    def on_pushButton_menu_principale_gestion_animaux_clicked(self):
        """
            fonction pour fermer la fenêtre de gestion animaux et remontrer le menu principale
        """
        self.caller.show()
        self.hide()