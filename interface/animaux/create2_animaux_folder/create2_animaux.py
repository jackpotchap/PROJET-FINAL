####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe Create2Animaux
###################################################################################
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from interface.animaux.create2_animaux_folder import create2_animaux_interface
from PyQt5.QtWidgets import QMessageBox
import time
from animaux import reptile, poisson, oiseau, animal
import inventaire

def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_sup_de_0_erreure_poid_crea2_animaux.setVisible(False)
    window.label_alpha_only_erreure_nom_crea2_animaux.setVisible(False)
    window.label_alpha_only_erreure_espece_crea2_animaux.setVisible(False)
    window.label_erreure_cara1_crea2_animaux.setVisible(False)
    window.label_erreure_cara2_crea2_animaux.setVisible(False)

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


def colorier_en_rouge(text : str) -> str:
    """
    vas colorier le texte en rouge
    : text: le text a colorié
    return: le text en rouge
    """
    return f"<html><head/><body><p><span style=\" color:#ff0000;\">{text}</span></p><p><br/></p></body></html>"

class Create2Animaux(QtWidgets.QDialog, create2_animaux_interface.Ui_Dialog):
    """
    Classe : Create2Animaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,p_caller,parent=None):
        """Constructeur
        : p_caller: la fenetre qui la appeler"""

        super(Create2Animaux, self).__init__(parent)
        self.setupUi(self)
        self.caller = p_caller

        # pour eviter le "êtte vous sure de vouloir quitter"?
        self.bruteForceClose = False

        self.setWindowTitle("Gestion de Zoo - 2e étape de la création d'un animaux")

        # mettre toute les enclos disponible dans la combo box
        for e in inventaire.ls_enclos:

            self.comboBox_enclos_crea2_enclos.addItem(f"{e.Id_enclos} - {e.Ecosysteme_enclos}")


        self.setWindowModality(Qt.ApplicationModal)

        cacher_lables_erreure(self)


        self.animal = self.caller.animal



        #Pour afficher les propritété ayant déja été initialiser
        if self.animal != None:
            self.lineEdit_nom_crea2_animaux.setText(self.animal.Nom_animal)
            if self.animal.Poid_animal == -1:
                self.lineEdit_poid_crea2_animaux.setText("")
            else:
                self.lineEdit_poid_crea2_animaux.setText(str(self.animal.Poid_animal))
            #pour que la enlcos prédéfinis sois déjà selectionné

            for e in inventaire.ls_enclos:
                if e.Id_enclos == self.animal.Enclos_animal.Id_enclos:
                    self.comboBox_enclos_crea2_enclos.setCurrentIndex(inventaire.ls_enclos.index(e))

            self.lineEdit_espece_crea2_animaux.setText(self.animal.Espece)
            if str(self.animal.__dict__[list(self.animal.__dict__)[-1]]) == "-1":
                self.lineEdit_cara1_crea2_animaux.setText("")
            else:
                self.lineEdit_cara1_crea2_animaux.setText(str(self.animal.__dict__[list(self.animal.__dict__)[-1]]))

            if str(self.animal.__dict__[list(self.animal.__dict__)[-2]]) == "-1":
                self.lineEdit_cara2_crea2_animaux.setText("")
            else:
                self.lineEdit_cara2_crea2_animaux.setText(str(self.animal.__dict__[list(self.animal.__dict__)[-2]]))


        #permeteras afficher l'attribut peut import sa classe
        cara1 = formatage_dun_attribut(list(self.animal.__dict__)[-1], self.caller.classe)
        self.label_cara1_crea2_animaux.setText(cara1)

        cara2 = formatage_dun_attribut(list(self.animal.__dict__)[-2], self.caller.classe)
        self.label_cara2_crea2_animaux.setText(cara2)

    @pyqtSlot()
    def on_pushButton_retour_crea2_animaux_clicked(self):



        #pour eviter que lorsque l'utilisateur veut revenir en arrirèr il recoit le message avertissement.
        self.bruteForceClose = True

        self.close()

    @pyqtSlot()
    def on_pushButton_validez_crea2_animaux_clicked(self):

        cacher_lables_erreure(self)
        bon_format = True

        poid = self.lineEdit_poid_crea2_animaux.text()
        nom = self.lineEdit_nom_crea2_animaux.text()
        enclos = inventaire.ls_enclos[self.comboBox_enclos_crea2_enclos.currentIndex()]
        espece = self.lineEdit_espece_crea2_animaux.text()

        #Vérification des données

        #Vérification de poids
        try:
            float(poid)
        except:
            self.label_sup_de_0_erreure_poid_crea2_animaux.setVisible(True)
            bon_format = False
        else:
            self.animal.Poid_animal = float(poid)
            if self.animal.Poid_animal != float(poid) or self.animal.Poid_animal == -1:

                self.label_sup_de_0_erreure_poid_crea2_animaux.setVisible(True)
                bon_format = False

        #vérification pour le nom
        self.animal.Nom_animal = nom
        if self.animal.Nom_animal != nom or self.animal.Nom_animal == "":
            self.label_alpha_only_erreure_nom_crea2_animaux.setVisible(True)
            bon_format = False


        #vérification pour le nom de l'èspece
        self.animal.Espece = espece
        if self.animal.Espece != espece or self.animal.Espece == "":
            self.label_alpha_only_erreure_espece_crea2_animaux.setVisible(True)
            bon_format = False

        self.animal.Enclos_animal = enclos


        cara1 = self.lineEdit_cara1_crea2_animaux.text()
        cara2 = self.lineEdit_cara2_crea2_animaux.text()

        #vérifiecation des 2 caratere spéciphique pour chaque type
        if self.caller.classe == "Reptile":
            self.label_erreure_cara2_crea2_animaux.setText(colorier_en_rouge("*Doit uniquement contenir des lettres"))
            self.label_erreure_cara1_crea2_animaux.setText(colorier_en_rouge("*Doit être un nombre supérieur a 0"))
            try:
                float(cara1)
            except:
                self.label_erreure_cara1_crea2_animaux.setVisible(True)
                bon_format = False
            else:
                self.animal.Temperature = float(cara1)
                if self.animal.Temperature != float(cara1) or self.animal.Temperature == -1:
                    self.label_erreure_cara1_crea2_animaux.setVisible(True)
                    bon_format = False

            self.animal.Couleur_de_peau = cara2
            if self.animal.Couleur_de_peau != cara2 or cara2 == "":
                self.label_erreure_cara2_crea2_animaux.setVisible(True)
                bon_format = False
        elif self.caller.classe == "Poisson":
            self.label_erreure_cara2_crea2_animaux.setText(colorier_en_rouge("*Doit être un nombre supérieur a 0"))
            self.label_erreure_cara1_crea2_animaux.setText(colorier_en_rouge("*Doit être un nombre supérieur a 0"))

            try:
                float(cara1)
            except:
                self.label_erreure_cara1_crea2_animaux.setVisible(True)
                bon_format = False
            else:
                self.animal.Profondeur_moyenne = float(cara1)
                if self.animal.Profondeur_moyenne != float(cara1) or self.animal.Profondeur_moyenne == -1:
                    self.label_erreure_cara1_crea2_animaux.setVisible(True)
                    bon_format = False

            try:
                float(cara2)
            except:
                self.label_erreure_cara2_crea2_animaux.setVisible(True)
                bon_format = False

            else:
                self.animal.Longueur_des_nageoire = float(cara2)
                if self.animal.Longueur_des_nageoire != float(cara2) or self.animal.Longueur_des_nageoire == -1:
                    self.label_erreure_cara2_crea2_animaux.setVisible(True)
                    bon_format = False
        elif self.caller.classe == "Oiseau":
            self.label_erreure_cara2_crea2_animaux.setText(colorier_en_rouge("*Doit être un nombre supérieur a 0"))
            self.label_erreure_cara1_crea2_animaux.setText(colorier_en_rouge("*Doit être un nombre supérieur a 0"))

            try:
                float(cara1)
            except:
                self.label_erreure_cara1_crea2_animaux.setVisible(True)

                bon_format = False
            else:
                self.animal.Longeur_bec = float(cara1)
                print(float(cara1))
                print(self.animal.Longeur_bec)
                if self.animal.Longeur_bec != float(cara1) or self.animal.Longeur_bec == -1:
                    self.label_erreure_cara1_crea2_animaux.setVisible(True)

                    bon_format = False

            try:
                float(cara2)
            except:
                self.label_erreure_cara2_crea2_animaux.setVisible(True)
                bon_format = False
            else:
                self.animal.Longeur_des_ailes = float(cara2)
                if self.animal.Longeur_des_ailes != float(cara2) or self.animal.Longeur_bec == -1:
                    self.label_erreure_cara2_crea2_animaux.setVisible(True)
                    bon_format = False

        if bon_format:

            #si jamais l'animal a changer de type, pour éviter que deux animaux avec le meme id existe en même temps
            #on vas suprimée
            for a in inventaire.ls_animaux:
                if a.Id_animal == self.animal.Id_animal or a.Id_animal == self.caller.adminId:
                    inventaire.ls_animaux.remove(a)

            #pour éviter que le meme animaux se retrouve dans le meme enclos
            if self.caller.enclos != None:
                for a in self.caller.enclos.Ls_animaux_enclos:
                    if a.Id_animal == self.animal.Id_animal:
                        self.caller.enclos.Ls_animaux_enclos.remove(a)

            self.animal.Enclos_animal.Ls_animaux_enclos.append(self.animal)


            inventaire.ls_animaux.append(self.animal)

            self.bruteForceClose = True
            self.caller.bruteForceClose = True
            self.close()

    def closeEvent(self, event):
        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "Tous changement effectuez seras perdu.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.caller.bruteForceClose = True

                event.accept()
            else:
                event.ignore()
