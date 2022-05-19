####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DeserialisationEnclos
###################################################################################
import json
import pathlib

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot
import copy
import enclos
import inventaire
from interface.enclos.deserialisation_enclos_folder import deserialisation_enclos_interface

def colorier_en_rouge(text : str) -> str:
    """
    Vas colorier le texte en rouge
    : text: le text a colorié
    return: le text en rouge
    """
    return f"<html><head/><body><p><span style=\" color:#ff0000;\">{text}</span></p><p><br/></p></body></html>"

def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_importation_erreure_deserialisation_enclos.setText(
        colorier_en_rouge("*Une erreure ces produit durant l\'importation"))
    window.label_importation_erreure_deserialisation_enclos.setVisible(False)
    window.label_selection_erreure_deserialisation_enclos.setVisible(False)


# code trouver sur https://stackoverflow.com/questions/38746002/pyqt-qfiledialog-directly-browse-to-a-folder
# pour montrer un interafce pouvant aller recuperer des fichier
def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    options |= QFileDialog.DontUseCustomDirectoryIcons
    dialog = QFileDialog()
    dialog.setOptions(options)

    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

    # ARE WE TALKING ABOUT FILES OR FOLDERS
    if isFolder:
        dialog.setFileMode(QFileDialog.DirectoryOnly)
    else:
        dialog.setFileMode(QFileDialog.AnyFile)
    # OPENING OR SAVING
    dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

    # SET FORMAT, IF SPECIFIED
    if fmt != '' and isFolder is False:
        dialog.setDefaultSuffix(fmt)
        dialog.setNameFilters([f'{fmt} (*.{fmt})'])

    # SET THE STARTING DIRECTORY
    if directory != '':
        dialog.setDirectory(str(directory))
    else:
        dialog.setDirectory(str(pathlib.Path().resolve()))


    if dialog.exec_() == QDialog.Accepted:
        path = dialog.selectedFiles()[0]  # returns a list
        return path
    else:
        return ''


class DeserialisationEnclos(QtWidgets.QDialog, deserialisation_enclos_interface.Ui_Dialog):
    """
    Classe : DeserialisationEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(DeserialisationEnclos, self).__init__(parent)
        self.setupUi(self)
        # variable qui si mis a true, permet de quitter sans demande a l'utilisateur si il veut quitter
        self.bruteForceClose = False
        self.dict = ""
        self.Filepath = ""
        self.importer_animaux = True

        cacher_lables_erreure(self)
        self.setWindowTitle("Gestion de Zoo - Deserialisation d'un enclos")

    @pyqtSlot()
    def on_pushButton_recherche_deserialisation_enclo_clicked(self):
        """
        fonction qui vas ouvrire un interface permetant d'aller choisire le path désiré.
        """
        # code trouver sur https://stackoverflow.com/questions/38746002/pyqt-qfiledialog-directly-browse-to-a-folder
        # pour montrer un interafce pouvant aller recuperer des fichier
        self.Filepath = FileDialog(forOpen=True)
        cacher_lables_erreure(self)
        try:
            with open(self.Filepath, "r") as fichier:
                self.dict = json.load(fichier)
                self.textBrowser_deserialisation_enclos.setText(str(self.dict))
        except:
            self.label_selection_erreure_deserialisation_enclos.setVisible(True)


    @pyqtSlot()
    def on_pushButton_importer_animaux_deserialisation_enclos_clicked(self):
        """
            Function qui vas servire de switch on/off pour activer ou désactiver l'importation animaux
        """
        if self.importer_animaux == True:
            self.importer_animaux = False
            self.pushButton_importer_animaux_deserialisation_enclos.setText("non")
        else:
            self.importer_animaux = True
            self.pushButton_importer_animaux_deserialisation_enclos.setText("oui")


    @pyqtSlot()
    def on_pushButton_ajouter_deserialisation_enclos_clicked(self):
        cacher_lables_erreure(self)

        # pour faire sure que le fichier a deja été ouvert et est valide
        if self.dict != "":

            enclos_t = enclos.Enclos()
            enclos_t.deserialiser(self.Filepath, inventaire.ls_animaux, self.importer_animaux)

            # faire sure si l'encloss existe déjà
            trouver = False
            for e in inventaire.ls_enclos:
                if e.Id_enclos == enclos_t.Id_enclos:
                    trouver = True

            if trouver:
                self.label_importation_erreure_deserialisation_enclos.setVisible(True)
                self.label_importation_erreure_deserialisation_enclos.setText(
                    colorier_en_rouge("*un enclos ayant un id identique existe déjà"))
            else:
                #ajouter l'enclos a la liste et y importer ses animaux si cocher
                inventaire.ls_enclos.append(enclos_t)
                if self.importer_animaux:
                    ls_animaux_enclos_t = []
                    for a in enclos_t.Ls_animaux_enclos:
                        #si jamais l'animal existe déjà
                        if type(a) == type({}):
                            animal_t = inventaire.dict_classe_animaux[a["_Animal__type"]]()
                            animal_t.deserialiser(a, inventaire.ls_enclos, enclos_t.Id_enclos)
                        else:
                            animal_t = a

                        #faire sure que un animal étant déjà dans le systeme sois importer 2 fois
                        trouver = False
                        for animal in inventaire.ls_animaux:
                            if animal.Id_animal == animal_t.Id_animal:
                                trouver = True
                                ls_animaux_enclos_t.append(animal)
                                animal.Enclos_animal = enclos_t

                        if trouver is False:
                            inventaire.ls_animaux.append(animal_t)
                            ls_animaux_enclos_t.append(animal_t)


                    enclos_t.Ls_animaux_enclos = ls_animaux_enclos_t

                self.bruteForceClose = True
                self.close()
        else:
            self.label_importation_erreure_deserialisation_enclos.setVisible(True)

    @pyqtSlot()
    def on_pushButton_quitter_deserialisation_enclos_clicked(self):
        self.close()


    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):

        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "La désérialisation en cours seras annulez.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()