# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/enclos/deserialisation_enclos_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(713, 475)
        self.pushButton_recherche_deserialisation_enclo = QtWidgets.QPushButton(Dialog)
        self.pushButton_recherche_deserialisation_enclo.setGeometry(QtCore.QRect(10, 20, 691, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_recherche_deserialisation_enclo.setFont(font)
        self.pushButton_recherche_deserialisation_enclo.setObjectName("pushButton_recherche_deserialisation_enclo")
        self.textBrowser_deserialisation_enclos = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_deserialisation_enclos.setGeometry(QtCore.QRect(10, 150, 391, 301))
        self.textBrowser_deserialisation_enclos.setObjectName("textBrowser_deserialisation_enclos")
        self.label_selection_erreure_deserialisation_enclos = QtWidgets.QLabel(Dialog)
        self.label_selection_erreure_deserialisation_enclos.setGeometry(QtCore.QRect(20, 80, 411, 41))
        self.label_selection_erreure_deserialisation_enclos.setObjectName("label_selection_erreure_deserialisation_enclos")
        self.label_fichier_titre_deserialisation_enclo = QtWidgets.QLabel(Dialog)
        self.label_fichier_titre_deserialisation_enclo.setGeometry(QtCore.QRect(20, 110, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_fichier_titre_deserialisation_enclo.setFont(font)
        self.label_fichier_titre_deserialisation_enclo.setObjectName("label_fichier_titre_deserialisation_enclo")
        self.label_importer_animaux_deserialisation_enclos = QtWidgets.QLabel(Dialog)
        self.label_importer_animaux_deserialisation_enclos.setGeometry(QtCore.QRect(490, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_importer_animaux_deserialisation_enclos.setFont(font)
        self.label_importer_animaux_deserialisation_enclos.setObjectName("label_importer_animaux_deserialisation_enclos")
        self.pushButton_importer_animaux_deserialisation_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_importer_animaux_deserialisation_enclos.setGeometry(QtCore.QRect(490, 170, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_importer_animaux_deserialisation_enclos.setFont(font)
        self.pushButton_importer_animaux_deserialisation_enclos.setObjectName("pushButton_importer_animaux_deserialisation_enclos")
        self.pushButton_ajouter_deserialisation_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_deserialisation_enclos.setGeometry(QtCore.QRect(490, 250, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_deserialisation_enclos.setFont(font)
        self.pushButton_ajouter_deserialisation_enclos.setObjectName("pushButton_ajouter_deserialisation_enclos")
        self.label_importation_erreure_deserialisation_enclos = QtWidgets.QLabel(Dialog)
        self.label_importation_erreure_deserialisation_enclos.setGeometry(QtCore.QRect(490, 300, 411, 41))
        self.label_importation_erreure_deserialisation_enclos.setObjectName("label_importation_erreure_deserialisation_enclos")
        self.pushButton_quitter_deserialisation_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_deserialisation_enclos.setGeometry(QtCore.QRect(490, 400, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_deserialisation_enclos.setFont(font)
        self.pushButton_quitter_deserialisation_enclos.setObjectName("pushButton_quitter_deserialisation_enclos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_recherche_deserialisation_enclo.setText(_translate("Dialog", "Chercher..."))
        self.label_selection_erreure_deserialisation_enclos.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">*le fichier n\'est pas du bon format</span></p><p><br/></p></body></html>"))
        self.label_fichier_titre_deserialisation_enclo.setText(_translate("Dialog", "Contenue du fichier:"))
        self.label_importer_animaux_deserialisation_enclos.setText(_translate("Dialog", "Importer les animaux :"))
        self.pushButton_importer_animaux_deserialisation_enclos.setText(_translate("Dialog", "Oui"))
        self.pushButton_ajouter_deserialisation_enclos.setText(_translate("Dialog", "Ajouter"))
        self.label_importation_erreure_deserialisation_enclos.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">*Une erreure ces produit durant l\'importation</span><br/></p></body></html>"))
        self.pushButton_quitter_deserialisation_enclos.setText(_translate("Dialog", "Quitter"))
