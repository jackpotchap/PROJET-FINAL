####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DetailAnimaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import enclos
import inventaire
from interface.animaux.detail_animaux_folder import detail_animaux_interface
def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_sans_enclos_erreure_details_animaux.setVisible(False)

def formatage_dun_attribut(p_attribut:str, p_classe)->str:
    """
    Fonction qui retireras les _ et mettra la premiere lettre en parametres
    : p_attribut: le nom de l'attribut qui seras afficher
    : p_classe: le nom de la classe de l'animal
    return: l'attribut bien formater
    """

    output = p_attribut.replace("_", " ").replace(p_classe, "")

    while output[0] == " ":
        output = output[1:]

    output = output[0].upper() + output[1:]
    return output

def animal_en_list_de_string(animal):

    dict_a = animal.__stre__()
    print(dict_a)
    output = []
    output += f"Nom : {dict_a['_Animal__nom_animal']}",
    output += f"Espèce : {dict_a['_Animal__espece_animal']}",
    output += f"Id de L'Enclos : {dict_a['_Animal__enclos_animal']}",
    output += f"Poids : {dict_a['_Animal__poid_animal']} Kg",
    output += "",
    output += f"Caratéristique de classe: ",

    for a in list(dict_a)[-2:]:
        output += f"     {formatage_dun_attribut(a,inventaire.dict_translate_object_to_dict[type(animal)])} : {dict_a[a]}",

    return output
class DetailAnimaux(QtWidgets.QDialog, detail_animaux_interface.Ui_Dialog):
    """
    Classe : DetailAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,p_animal,parent=None):
        """Constructeur"""

        super(DetailAnimaux, self).__init__(parent)
        self.setupUi(self)
        self.animal = p_animal
        self.setWindowTitle("Gestion de Zoo - Details d'un animaux")
        cacher_lables_erreure(self)

        model = QStandardItemModel()
        self.listView_ls_animal_detail_animaux.setModel(model)
        for row in animal_en_list_de_string(self.animal):
            item = QStandardItem(row)
            model.appendRow(item)

        self.label_id_information_detail_animaux.setText(self.animal.__dict__["_Animal__id_animal"])
        self.label_classe_information_detail_animaux.setText(inventaire.dict_translate_object_to_dict[type(self.animal)])

        trouver = False
        for e in inventaire.ls_enclos:

            if e.Id_enclos == self.animal.Enclos_animal.Id_enclos:
                trouver = True


        if trouver is False:
            self.label_sans_enclos_erreure_details_animaux.setVisible(True)

