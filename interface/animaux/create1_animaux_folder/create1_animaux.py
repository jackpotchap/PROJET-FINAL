####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe Create1Animaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
import inventaire
from interface.animaux.create1_animaux_folder import create1_animaux_interface
from interface.animaux.create2_animaux_folder import create2_animaux
from interface.animaux.quitter_sans_terminer_animaux_crea_folder import quitter_sans_terminer_animaux_crea
from animaux import animal
from animaux import reptile, poisson, oiseau, animal


def cacher_lables_erreure(window):
    """
    Fonction pour cacher les labels erreure du parametre window
    : window: la fenettre a chacher les labels erreure de...
    """
    window.label_existant_erreure_id_crea1_animaux.setVisible(False)
    window.label_format_erreure_id_crea1_enclos.setVisible(False)



class Create1Animaux(QtWidgets.QDialog, create1_animaux_interface.Ui_Dialog):
    """
    Classe : Create1Animaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self, p_animal = None,parent=None):
        """Constructeur"""

        super(Create1Animaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - 1er étape de la création d'un animaux")

        cacher_lables_erreure(self)

        #mettre toute les classe disponible dans la combo box
        for classe in inventaire.dict_classe_animaux:
            self.comboBox_classe_crea1_animaux.addItem(classe)

        #pour eviter le ette vous sure de vouloir quitter
        self.bruteForceClose = False

        #si l'animal est = a none cela veut dire que l'utilisateur shouaite en crée un
        #alors que si non il veut le modifier
        self.animal = p_animal

        if self.animal != None:
            print(type(self.animal))

            self.comboBox_classe_crea1_animaux.setCurrentText(inventaire.dict_translate_object_to_dict[type(self.animal)])
            self.lineEdit_id_crea1_animaux.setText(self.animal.Id_animal)

    @pyqtSlot()
    def on_pushButton_suivant_crea1_animaux_clicked(self):
        """
                fonction pour ouvrire la 2e fenêtre de création d'animaux
                et également commencer la création de l'animal et les premiere vérification
        """
        #pour que les erreure ayant été corriger disparaisse apres chaque essaie
        cacher_lables_erreure(self)


        #Vérifier si l'id existe déja
        id_animal = self.lineEdit_id_crea1_animaux.text()
        self.classe = self.comboBox_classe_crea1_animaux.currentText()
        trouver = False
        for a in inventaire.ls_animaux:

            if a.Id_animal == id_animal:
                if a != self.animal:
                    trouver = True

        if trouver:
            self.label_existant_erreure_id_crea1_animaux.setVisible(True)
        else:
            #vérifier si l'id est du bon format en l'attribuant a l'animal
            # Vas grasse a la classe préalablement selectionner crée automatiquement un animal vide
            if inventaire.dict_translate_object_to_dict[type(self.animal)] != self.classe:
                if self.animal == None:

                    self.animal = inventaire.dict_classe_animaux[self.classe]()
                else:
                    animal_t = inventaire.dict_classe_animaux[self.classe]()
                    animal_t.Nom_animal = self.animal.Nom_animal
                    animal_t.Poid_animal = self.animal.Poid_animal
                    animal_t.Espece = self.animal.Espece
                    self.animal = animal_t

            self.animal.Id_animal = id_animal
            if self.animal.Id_animal == "":
                self.label_format_erreure_id_crea1_enclos.setVisible(True)
            else:
                print(self.animal.Nom_animal)
                print("AA")
                crea2_A_form = create2_animaux.Create2Animaux(p_caller = self)


                crea2_A_form.show()
                crea2_A_form.exec()

                if self.bruteForceClose:
                    self.close()

    @pyqtSlot()
    def on_pushButton_annulez_crea1_animaux_clicked(self):
        """
            fonction pour fermer la fenetre mais demander a l'utilisateur si il veut vraiment quitter la fenetre
        """


        self.close()

    @pyqtSlot()
    def show_caller(self):
        self.show()

    #code proveneant de la documentation officiel PyQt5 https://pythonpyqt.com/pyqt-message-box/
    def closeEvent(self, event):

        #j'ai tenter de le traduire sans resulta le mieux que j'ai trouver pour une solution de pyqt3.5
        if not self.bruteForceClose:
            reply = QMessageBox.question(self, "Quit", "Tous changement effectuez seras perdu.",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()