####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe GestionEnclos
###################################################################################
import pathlib
from datetime import date

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QEvent
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import enclos
from interface.enclos.gestion_enclos_folder import gestion_enclos_interface
from interface.enclos.create_enclos_folder import create_enclos
from interface.enclos.detail_enclos_folder import detail_enclos
from interface.enclos.deserialisation_enclos_folder import deserialisation_enclos
import inventaire
from interface.succes_pop_up_interface_folder import succes_pop_up


def refresh_list_view(window, list_enclos):
    """
    Méthodes qui vas rafraichir tous les valeur de la list_view .
    :param window: la fenetre qui contient la list view.
    : param list_enclos: list qui seras mis dans la list_view.
    """
    #code inspirer d'information vue en classe
    #création de la list view
    model = QStandardItemModel()
    window.listView_recherche_gestion_enclos.setModel(model)
    for e in list_enclos:

        item = QStandardItem(e.Id_enclos + " - " + e.Ecosysteme_enclos + " - " + e.Dernier_netoyage_enclos)
        model.appendRow(item)

    #pusique le systeme de selection fonctionne avec les row la list et la list view doivent etre identique
    inventaire.ls_enclos_filtrer = list_enclos
def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window.
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_selection_erreure_gestion_enclos.setVisible(False)
    window.label_format_erreure_id_recherche_gestion_enclos.setVisible(False)

def filtre(window,nouvelle_entree):
    """
    Fonction qui va retourner une liste qui a été filtrer selons la valeur et le type de la combobox.
    : param window: la fenetre qui contient les information pour filtrer.
    : param nouvelle_entree: donc, la touche qui a réscament été utiliser dans le lineedit .
    return: la list filtré
    """
    list_filtrer = []


    for e in inventaire.ls_enclos:

        toute_trouver = True
        #Si la noouvelle entrée est un supprimée retirer la dernière valeur.
        if nouvelle_entree == "\x08":
            text = window.lineEdit_recherche_id_gestion_enclos.text()[0:-1]

        else:
            text = window.lineEdit_recherche_id_gestion_enclos.text() + nouvelle_entree

        #Si les enclos contiennent tous les lettres contenue dans text, ils sont bon pour être affiché.
        for lettre in text:

            if e.Id_enclos.lower().find(lettre.lower()) != -1:
                pass
            else:
                toute_trouver = False

        # si jamais il a été trouver, est-ce que son genre écosystème est celui désirer si oui afficher
        # si le genre d'écosysteme est None tous afficher seux qui sont bon
        if toute_trouver:
            if window.comboBox_recherche_ecosysteme_gestion_enclos.currentText() == \
                    e.Ecosysteme_enclos \
                    or window.comboBox_recherche_ecosysteme_gestion_enclos.currentText() == "None":
                list_filtrer.append(e)

    return list_filtrer
class GestionEnclos(QtWidgets.QDialog, gestion_enclos_interface.Ui_Dialog):
    """
    Classe : GestionEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self, p_caller,parent=None):
        """Constructeur"""

        super(GestionEnclos, self).__init__(parent)
        self.setupUi(self)
        refresh_list_view(self, inventaire.ls_enclos)
        cacher_lables_erreure(self)
        self.setWindowTitle("Gestion de Zoo - Gestion enclos")

        # code qui permet de rafraichire la list view lorsque l'utilisateur écrit dans le line edit recherch id
        # code trouver sur https://stackoverflow.com/questions/46505769/pyqt-keypress-event-in-lineedit
        # j'associe l'evenementeventFilter
        self.lineEdit_recherche_id_gestion_enclos.installEventFilter(self)

        self.caller = p_caller

        #Initialisation des choix disponible dans la combo box.
        environement = list(inventaire.ls_type_enclos)
        environement.append("None")
        for e in environement:
            self.comboBox_recherche_ecosysteme_gestion_enclos.addItem(e)

        self.comboBox_recherche_ecosysteme_gestion_enclos.setCurrentIndex(len(environement) - 1)
        # code qui permet de mettre un event lorsque la combobox changeras de selection
        # code trouver sur https://stackoverflow.com/questions/44707794/pyqt-combo-box-change-value-of-a-label
        self.comboBox_recherche_ecosysteme_gestion_enclos.currentTextChanged.connect(
            self.on_comboBox_recherche_ecosysteme_gestion_enclos_changed)

    # code qui permet de rafraichire la list view lorsque l'utilisateur écrit dans le line edit recherch id
    # code trouver sur https://stackoverflow.com/questions/46505769/pyqt-keypress-event-in-lineedit
    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
                source is self.lineEdit_recherche_id_gestion_enclos):
            refresh_list_view(self, filtre(self, event.text()))
        return super(GestionEnclos, self).eventFilter(source, event)

    # code qui permet de mettre un event lorsque la combobox changeras de selection
    # code trouver sur https://stackoverflow.com/questions/44707794/pyqt-combo-box-change-value-of-a-label
    @pyqtSlot()
    def on_comboBox_recherche_ecosysteme_gestion_enclos_changed(self):
        """
        Fonction qui vas rafraichir la list avec le nouvelle filtre qui vient d'être slectionné.
        """
        refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_cree_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'enclos
        """
        cacher_lables_erreure(self)
        crea_A_form = create_enclos.CreateEnclos()

        crea_A_form.show()
        crea_A_form.exec()

        refresh_list_view(self,filtre(self,""))

    @pyqtSlot()
    def on_pushButton_modif_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de création d'enclos puisque ses la meme que modification
        """
        cacher_lables_erreure(self)

        #cependant un enclos de la list_view doit etre selectionner
        #code provenant de la documentation officiel pyqt5
        if self.listView_recherche_gestion_enclos.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_enclos.setVisible(True)

        else:
            crea_A_form = create_enclos.CreateEnclos(p_enclos=inventaire.ls_enclos_filtrer[self.listView_recherche_gestion_enclos.currentIndex().row()])

            crea_A_form.show()
            crea_A_form.exec()

            refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_sup_gestion_enclo_clicked(self):
        """
        Fonction pour supprimer un enclos
        """
        cacher_lables_erreure(self)
        # Cependant un enclos de la list_view doit etre selectionner.
        # Code provenant de la documentation officiel pyqt5
        if self.listView_recherche_gestion_enclos.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_enclos.setVisible(True)
        else:
            #En plus de retirer l'enclos de la list, je retirer en plus la référence des animaux à l'enclos
            for a in inventaire.ls_enclos_filtrer[self.listView_recherche_gestion_enclos.currentIndex().row()].Ls_animaux_enclos:

                a.Enclos_animal = enclos.Enclos()
            inventaire.ls_enclos.remove(
                inventaire.ls_enclos_filtrer[self.listView_recherche_gestion_enclos.currentIndex().row()])
            refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_netoyer_gestion_enclo_clicked(self):
        """
        Fonction pour nettoyer et mettre a jour la date du dernier nettoyer a l'enclos.

        """
        cacher_lables_erreure(self)
        # Cependant un enclos de la list_view doit etre selectionner.
        # Code provenant de la documentation officiel pyqt5
        if self.listView_recherche_gestion_enclos.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_enclos.setVisible(True)
        else:
            # code trouver sur
            # https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/#:~:text=In%20Python%2C%20in%20order%20to,class%20to%20fetch%20todays%20date.
            aujourdui = date.today()
            inventaire.ls_enclos_filtrer[self.listView_recherche_gestion_enclos.currentIndex().row()].Dernier_netoyage_enclos\
            = f"{aujourdui.year}-{aujourdui.month}-{aujourdui.day}"
            refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_detail_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'enclos
        """
        cacher_lables_erreure(self)
        # Cependant un enclos de la list_view doit etre selectionner.
        # Code provenant de la documentation officiel pyqt5
        if self.listView_recherche_gestion_enclos.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_enclos.setVisible(True)
        else:
            detail_E_form = detail_enclos.DetailEnclos(inventaire.ls_enclos_filtrer[self.listView_recherche_gestion_enclos.currentIndex().row()])

            detail_E_form.show()
            detail_E_form.exec()

    @pyqtSlot()
    def on_pushButton_serialiser_gestion_enclo_clicked(self):
        """
                fonction pour sérialiser un enclos
        """
        cacher_lables_erreure(self)
        # Cependant un enclos de la list_view doit etre selectionner.
        # Code provenant de la documentation officiel pyqt5
        if self.listView_recherche_gestion_enclos.currentIndex().row() == -1:
            self.label_selection_erreure_gestion_enclos.setVisible(True)
        else:
            #si jamais le resulta = 1, cela voudras dire que une erreure est survenue
            resulta = 0
            try:
                #formatage du nom du fichier a sérialiser acec son path (chemin accès).
                enclos_t = inventaire.ls_enclos_filtrer[self.listView_recherche_gestion_enclos.currentIndex().row()]
                nom_du_fichier = enclos_t.Id_enclos + "_" + enclos_t.Ecosysteme_enclos + "_" + enclos_t.Dernier_netoyage_enclos
                path = str(pathlib.Path().resolve()) + "\\Serialiser\\" + nom_du_fichier
                # code trouver sur https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
                # pour avoir seulement le directory dans lequel on travail.
                enclos_t.serialiser(path)
            except:
                resulta = 1

            #Faire apparaitre le message de confiramtion en fonction du niveau de réussite 1 = échec, 0 = réussite
            Sucess_A_form = succes_pop_up.SuccesPopUpInterface(resulta)
            Sucess_A_form.show()
            Sucess_A_form.exec()
            refresh_list_view(self, filtre(self, ""))

    @pyqtSlot()
    def on_pushButton_deserialiser_gestion_enclo_clicked(self):
        """
                fonction pour ouvrire la fenêtre de detail d'enclos
        """

        Deser_E_form = deserialisation_enclos.DeserialisationEnclos()

        Deser_E_form.show()
        Deser_E_form.exec()

        refresh_list_view(self, filtre(self, ""))
    @pyqtSlot()
    def on_pushButton_menu_principale_gestion_enclos_clicked(self):
        """
            fonction pour fermer la fenêtre de gestion enclos et remontrer le menu principale
        """
        self.caller.show()
        self.hide()