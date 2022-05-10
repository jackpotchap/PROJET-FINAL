####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe Create1Animaux
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.animaux.create1_animaux_folder import create1_animaux_interface
from interface.animaux.create2_animaux_folder import create2_animaux
from interface.animaux.quitter_sans_terminer_animaux_crea_folder import quitter_sans_terminer_animaux_crea
from animaux import animal

class Create1Animaux(QtWidgets.QDialog, create1_animaux_interface.Ui_Dialog):
    """
    Classe : Create1Animaux
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(Create1Animaux, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - 1er étape de la création d'un animaux")
        self.animaux = None

    @pyqtSlot()
    def on_pushButton_suivant_crea1_animaux_clicked(self):
        """
                fonction pour ouvrire la 2e fenêtre de création d'animaux
        """

        crea2_A_form = create2_animaux.Create2Animaux()

        crea2_A_form.show()
        crea2_A_form.exec()

    @pyqtSlot()
    def on_pushButton_annulez_crea1_animaux_clicked(self):
        """
            fonction pour fermer la fenetre mais demander a l'utilisateur si il veut vraiment quitter la fenetre
        """

        pop_up_quitter_A = quitter_sans_terminer_animaux_crea.QuitterSansTerminerAnimauxCrea()
        pop_up_quitter_A.show()
        answer = pop_up_quitter_A.exec_()
        print(answer)
        if answer == 1:
            self.close()