####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe DeserialisationAnimaux
###################################################################################

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot
from interface.animaux.deserialisation_animaux_folder import deserialisation_animaux_interface
import pathlib
import json
import inventaire

def colorier_en_rouge(text : str) -> str:
    """
    vas colorier le texte en rouge
    : text: le text a colorié
    return: le text en rouge
    """
    return f"<html><head/><body><p><span style=\" color:#ff0000;\">{text}</span></p><p><br/></p></body></html>"
def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_importation_erreure_deserialisation_animaux.setText(
        colorier_en_rouge("*Une erreure ces produit durant l\'importation"))
    window.label_importation_erreure_deserialisation_animaux.setVisible(False)
    window.label_selection_erreure_deserialisation_animaux.setVisible(False)

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
class DeserialisationAnimaux(QtWidgets.QDialog, deserialisation_animaux_interface.Ui_Dialog):
    """
    Classe : DetailAnimaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(DeserialisationAnimaux, self).__init__(parent)
        self.setupUi(self)
        self.bruteForceClose = False
        self.dict = ""
        self.Filepath = ""
        cacher_lables_erreure(self)
        self.setWindowTitle("Gestion de Zoo - Deserialisation d'un animaux")


    @pyqtSlot()
    def on_pushButton_recherche_deserialisation_animaux_clicked(self):
        #code trouver sur https://stackoverflow.com/questions/38746002/pyqt-qfiledialog-directly-browse-to-a-folder
        #pour montrer un interafce pouvant aller recuperer des fichier
        self.Filepath = FileDialog(forOpen=True)
        cacher_lables_erreure(self)

        #tester si le fichier es t lissable et l'afficher dans un textbrower son contenue
        try:
            with open(self.Filepath, "r") as fichier:
                self.dict = json.load(fichier)
                self.textBrowser_deserialisation_animaux.setText(str(self.dict))
        except:
            self.label_selection_erreure_deserialisation_animaux.setVisible(True)

    @pyqtSlot()
    def on_pushButton_ajouter_deserialisation_animaux_clicked(self):
        cacher_lables_erreure(self)

        #pour faire sure que le fichier a déjà été ouvert
        if self.dict != "":

            animal_t = inventaire.dict_classe_animaux[self.dict["_Animal__type"]]()
            animal_t.deserialiser(self.Filepath, inventaire.ls_enclos)

            #faire sure si l'animal existe déjà
            trouver = False
            for a in inventaire.ls_animaux:
                if a.Id_animal == animal_t.Id_animal:
                    trouver = True

            if trouver:
                self.label_importation_erreure_deserialisation_animaux.setVisible(True)
                self.label_importation_erreure_deserialisation_animaux.setText(colorier_en_rouge("*un animal ayant un id identique existe déja"))
            else:

                inventaire.ls_animaux.append(animal_t)
                self.bruteForceClose = True
                self.close()
        else:
            self.label_importation_erreure_deserialisation_animaux.setVisible(True)

    @pyqtSlot()
    def on_pushButton_quitter_deserialisation_animaux_clicked(self):
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