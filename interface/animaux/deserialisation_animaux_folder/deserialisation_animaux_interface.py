# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/animaux/deserialisation_animaux_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(717, 450)
        self.pushButton_recherche_deserialisation_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_recherche_deserialisation_animaux.setGeometry(QtCore.QRect(10, 10, 691, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_recherche_deserialisation_animaux.setFont(font)
        self.pushButton_recherche_deserialisation_animaux.setObjectName("pushButton_recherche_deserialisation_animaux")
        self.pushButton_quitter_deserialisation_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter_deserialisation_animaux.setGeometry(QtCore.QRect(500, 220, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_deserialisation_animaux.setFont(font)
        self.pushButton_quitter_deserialisation_animaux.setObjectName("pushButton_quitter_deserialisation_animaux")
        self.textBrowser_deserialisation_animaux = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_deserialisation_animaux.setGeometry(QtCore.QRect(10, 140, 391, 301))
        self.textBrowser_deserialisation_animaux.setObjectName("textBrowser_deserialisation_animaux")
        self.pushButton_ajouter_deserialisation_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_deserialisation_animaux.setGeometry(QtCore.QRect(500, 120, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_deserialisation_animaux.setFont(font)
        self.pushButton_ajouter_deserialisation_animaux.setObjectName("pushButton_ajouter_deserialisation_animaux")
        self.label_importation_erreure_deserialisation_animaux = QtWidgets.QLabel(Dialog)
        self.label_importation_erreure_deserialisation_animaux.setGeometry(QtCore.QRect(500, 170, 411, 41))
        self.label_importation_erreure_deserialisation_animaux.setObjectName("label_importation_erreure_deserialisation_animaux")
        self.label_fichier_titre_deserialisation_animaux = QtWidgets.QLabel(Dialog)
        self.label_fichier_titre_deserialisation_animaux.setGeometry(QtCore.QRect(20, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_fichier_titre_deserialisation_animaux.setFont(font)
        self.label_fichier_titre_deserialisation_animaux.setObjectName("label_fichier_titre_deserialisation_animaux")
        self.label_selection_erreure_deserialisation_animaux = QtWidgets.QLabel(Dialog)
        self.label_selection_erreure_deserialisation_animaux.setGeometry(QtCore.QRect(20, 70, 411, 41))
        self.label_selection_erreure_deserialisation_animaux.setObjectName("label_selection_erreure_deserialisation_animaux")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_recherche_deserialisation_animaux.setText(_translate("Dialog", "Chercher..."))
        self.pushButton_quitter_deserialisation_animaux.setText(_translate("Dialog", "Quitter"))
        self.pushButton_ajouter_deserialisation_animaux.setText(_translate("Dialog", "Ajouter"))
        self.label_importation_erreure_deserialisation_animaux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">*Une erreure ces produit durant l\'importation</span><br/></p></body></html>"))
        self.label_fichier_titre_deserialisation_animaux.setText(_translate("Dialog", "Contenue du fichier:"))
        self.label_selection_erreure_deserialisation_animaux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">*le fichier n\'est pas du bon format</span></p><p><br/></p></body></html>"))
