####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DetailEnclos
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from interface.enclos.detail_enclos_folder import detail_enclos_interface
from interface.enclos.list_selection_animaux_enclos_folder import list_selection_animaux_enclos
import inventaire

def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_selection_erreure_details_enclos.setVisible(False)


def refresh_list_view(window, ls_animaux):
    model = QStandardItemModel()
    window.listView_ls_animal_detail_enclos.setModel(model)
    print(ls_animaux)
    for a in ls_animaux:

        item = QStandardItem(
            a.Id_animal + " - " + a.Nom_animal + " - " + inventaire.dict_translate_object_to_dict[type(a)])
        model.appendRow(item)
class DetailEnclos(QtWidgets.QDialog, detail_enclos_interface.Ui_Dialog):
    """
    Classe : DetailEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,p_enclos = None,parent=None):
        """Constructeur"""

        super(DetailEnclos, self).__init__(parent)
        self.setupUi(self)
        self.enclos = p_enclos
        cacher_lables_erreure(self)


        ls_animaux = self.enclos.Ls_animaux_enclos.copy()
        print(ls_animaux)
        refresh_list_view(self,ls_animaux)

        self.label_id_information_detail_enclo.setText(self.enclos.Id_enclos)
        self.label_ecostysteme_information_detail_enclo.setText(self.enclos.Ecosysteme_enclos)
        self.label_nettoyage_information_detail_enclo.setText(self.enclos.Dernier_netoyage_enclos)


        self.setWindowTitle("Gestion de Zoo - Detail d'un Enclos")

