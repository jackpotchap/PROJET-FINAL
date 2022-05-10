####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe QuitterSansTerminerAnimauxCrea
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.animaux.quitter_sans_terminer_animaux_crea_folder import quitter_sans_terminer_animaux_crea_interface

class QuitterSansTerminerAnimauxCrea(QtWidgets.QDialog, quitter_sans_terminer_animaux_crea_interface.Ui_Dialog):
    """
    Classe : QuitterSansTerminerAnimauxCrea
    Héritant de Qtwidgets et de Ui_Dialogue
    """

    def __init__(self,parent=None):
        """Constructeur"""

        super(QuitterSansTerminerAnimauxCrea, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - Attention")

    @pyqtSlot()
    def on_pushButton_veut_pas_Q_pop_up_animaux_clicked(self):
        self.close()
        return 0

    @pyqtSlot()
    def on_pushButton_veut_Q_pop_up_animaux_clicked(self):
        return self
        return 1