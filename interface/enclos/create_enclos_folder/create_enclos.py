####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe CreateEnclos
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot

import enclos
from interface.enclos.create_enclos_folder import create_enclos_interface
import inventaire
from datetime import date

def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_existant_erreure_id_crea_enclos.setVisible(False)
    window.label_format_erreure_id_crea_enclos.setVisible(False)
class CreateEnclos(QtWidgets.QDialog, create_enclos_interface.Ui_Dialog):
    """
    Classe : CreateEnclos
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,p_enclos = None,parent=None):
        """Constructeur"""

        super(CreateEnclos, self).__init__(parent)
        self.setupUi(self)

        cacher_lables_erreure(self)

        self.setWindowTitle("Gestion de Zoo - Create enclos")
        self.bruteForceClose = False
        environement = list(inventaire.ls_type_enclos)

        for e in environement:
            self.comboBox_ecosysteme_crea_enclos.addItem(e)

        # pour eviter le probème ou on change la classe et
        # donc l'enclos n'est plus le meme object et donc sont id est déjà occupé par lui meme

        self.adminId = None

        # si l'enclos est = a none cela veut dire que l'utilisateur shouaite en crée un
        # alors que si non il veut le modifier
        self.enclos = p_enclos
        if self.enclos != None:

            self.adminId = self.enclos.Id_enclos
            self.comboBox_ecosysteme_crea_enclos.setCurrentText(self.enclos.Ecosysteme_enclos)
            self.lineEdit_id_crea_enclo.setText(self.enclos.Id_enclos)
    @pyqtSlot()
    def on_pushButton_annulez_crea_enclos_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pushButton_valider_crea_enclos_clicked(self):

        id_enclos = self.lineEdit_id_crea_enclo.text()
        environnement = self.comboBox_ecosysteme_crea_enclos.currentText()
        trouver = False
        bon_format = True
        for e in inventaire.ls_enclos:

            if e.Id_enclos == id_enclos:
                if e != self.enclos:
                    if self.adminId != e.Id_enclos:
                        trouver = True


        if trouver:
            self.label_existant_erreure_id_crea_enclos.setVisible(True)
        else:
            # vérifier si l'id est du bon format en l'attribuant a l'animal
            # Vas grasse a la classe préalablement selectionner crée automatiquement un animal vide
            if self.enclos == None:
                #code trouver sur
                #https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/#:~:text=In%20Python%2C%20in%20order%20to,class%20to%20fetch%20todays%20date.
                #pour aller chercher de l'information

                aujourdui = date.today()
                self.enclos = enclos.Enclos(p_dernier_netoyage=f"{aujourdui.year}-{aujourdui.month}-{aujourdui.day}")
            else:
                pass

            self.enclos.Id_enclos = id_enclos
            if self.enclos.Id_enclos == "":
                self.label_format_erreure_id_crea_enclos.setVisible(True)
                bon_format = False

            self.enclos.Ecosysteme_enclos = environnement

            if bon_format:
                #pour modifier les caratere de l'animal si jamais il exist e déja
                for e in inventaire.ls_enclos:
                    if e.Id_enclos == self.enclos.Id_enclos  :
                        inventaire.ls_enclos.remove(e)
                inventaire.ls_enclos.append(self.enclos)
                self.bruteForceClose = True
                self.close()





    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):

        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "Tous changement effectuez seras perdu.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()