####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe SuccesPopUpInterface
###################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from interface.succes_pop_up_interface_folder import succes_pop_up_interface

class SuccesPopUpInterface(QtWidgets.QDialog, succes_pop_up_interface.Ui_Dialog):
    """
    Classe : SuccesPopUpInterface
    Héritant de QDialog et de Ui_Dialog
    """

    def __init__(self,p_result ,parent=None):
        """Constructeur"""
        super(SuccesPopUpInterface, self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle("Gestion de Zoo - resulta")

        #si sa na pas fonctionner
        if p_result == 1:
            self.label_succes_serialisation_pop_up.setVisible(False)
        #si sa la fonctionner
        else:
            self.label_erreure_serialisation_pop_up.setVisible(False)
    @pyqtSlot()
    def on_pushButton_ok_serialisation_enclo_clicked(self):
        """
        fonction pour ouvrire la fenêtre de la section animaux du zoo
        """

        self.close()