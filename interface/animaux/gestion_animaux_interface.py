# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/animaux/gestion_animaux_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 574)
        self.pushButton_cree_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_cree_gestion_animaux.setGeometry(QtCore.QRect(490, 50, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cree_gestion_animaux.setFont(font)
        self.pushButton_cree_gestion_animaux.setObjectName("pushButton_cree_gestion_animaux")
        self.label_recherche_ecosysteme_gestion_animaux = QtWidgets.QLabel(Dialog)
        self.label_recherche_ecosysteme_gestion_animaux.setGeometry(QtCore.QRect(10, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_recherche_ecosysteme_gestion_animaux.setFont(font)
        self.label_recherche_ecosysteme_gestion_animaux.setObjectName("label_recherche_ecosysteme_gestion_animaux")
        self.pushButton_netoyer_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_netoyer_gestion_animaux.setGeometry(QtCore.QRect(490, 230, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_netoyer_gestion_animaux.setFont(font)
        self.pushButton_netoyer_gestion_animaux.setObjectName("pushButton_netoyer_gestion_animaux")
        self.pushButton_serialiser_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_serialiser_gestion_animaux.setGeometry(QtCore.QRect(490, 290, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_serialiser_gestion_animaux.setFont(font)
        self.pushButton_serialiser_gestion_animaux.setObjectName("pushButton_serialiser_gestion_animaux")
        self.lineEdit_recherche_id_gestion_animaux = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_recherche_id_gestion_animaux.setGeometry(QtCore.QRect(10, 90, 151, 31))
        self.lineEdit_recherche_id_gestion_animaux.setObjectName("lineEdit_recherche_id_gestion_animaux")
        self.comboBox_recherche_ecosysteme_gestion_animaux = QtWidgets.QComboBox(Dialog)
        self.comboBox_recherche_ecosysteme_gestion_animaux.setGeometry(QtCore.QRect(10, 210, 181, 31))
        self.comboBox_recherche_ecosysteme_gestion_animaux.setObjectName("comboBox_recherche_ecosysteme_gestion_animaux")
        self.pushButton_modif_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_modif_gestion_animaux.setGeometry(QtCore.QRect(490, 110, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modif_gestion_animaux.setFont(font)
        self.pushButton_modif_gestion_animaux.setObjectName("pushButton_modif_gestion_animaux")
        self.label_recherche_gestion_animaux = QtWidgets.QLabel(Dialog)
        self.label_recherche_gestion_animaux.setGeometry(QtCore.QRect(10, -10, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_recherche_gestion_animaux.setFont(font)
        self.label_recherche_gestion_animaux.setObjectName("label_recherche_gestion_animaux")
        self.label_selection_erreure_gestion_animaux = QtWidgets.QLabel(Dialog)
        self.label_selection_erreure_gestion_animaux.setGeometry(QtCore.QRect(490, 20, 411, 41))
        self.label_selection_erreure_gestion_animaux.setObjectName("label_selection_erreure_gestion_animaux")
        self.listView_recherche_gestion_animaux = QtWidgets.QListView(Dialog)
        self.listView_recherche_gestion_animaux.setGeometry(QtCore.QRect(10, 260, 401, 291))
        self.listView_recherche_gestion_animaux.setObjectName("listView_recherche_gestion_animaux")
        self.label_id_crea_animaux = QtWidgets.QLabel(Dialog)
        self.label_id_crea_animaux.setGeometry(QtCore.QRect(10, 70, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_id_crea_animaux.setFont(font)
        self.label_id_crea_animaux.setObjectName("label_id_crea_animaux")
        self.label_format_erreure_id_recherche_gestion_animaux = QtWidgets.QLabel(Dialog)
        self.label_format_erreure_id_recherche_gestion_animaux.setGeometry(QtCore.QRect(10, 130, 411, 41))
        self.label_format_erreure_id_recherche_gestion_animaux.setObjectName("label_format_erreure_id_recherche_gestion_animaux")
        self.pushButton_sup_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_sup_gestion_animaux.setGeometry(QtCore.QRect(490, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sup_gestion_animaux.setFont(font)
        self.pushButton_sup_gestion_animaux.setObjectName("pushButton_sup_gestion_animaux")
        self.pushButton_deserialiser_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_deserialiser_gestion_animaux.setGeometry(QtCore.QRect(490, 350, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_deserialiser_gestion_animaux.setFont(font)
        self.pushButton_deserialiser_gestion_animaux.setObjectName("pushButton_deserialiser_gestion_animaux")
        self.pushButton_menu_principale_gestion_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_menu_principale_gestion_animaux.setGeometry(QtCore.QRect(490, 510, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_menu_principale_gestion_animaux.setFont(font)
        self.pushButton_menu_principale_gestion_animaux.setObjectName("pushButton_menu_principale_gestion_animaux")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_cree_gestion_animaux.setText(_translate("Dialog", "Crée un nouvelle animal"))
        self.label_recherche_ecosysteme_gestion_animaux.setText(_translate("Dialog", "Classe :"))
        self.pushButton_netoyer_gestion_animaux.setText(_translate("Dialog", "Détail"))
        self.pushButton_serialiser_gestion_animaux.setText(_translate("Dialog", "Sérialiser"))
        self.pushButton_modif_gestion_animaux.setText(_translate("Dialog", "modifié un animal"))
        self.label_recherche_gestion_animaux.setText(_translate("Dialog", "Recherche et Gestion Animaux"))
        self.label_selection_erreure_gestion_animaux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">*Un animal doit être sélectioner au préalable</span></p><p><br/></p></body></html>"))
        self.label_id_crea_animaux.setText(_translate("Dialog", "id de l\'animal:"))
        self.label_format_erreure_id_recherche_gestion_animaux.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">*L\'id doit commencer par &lt;&lt; A &gt;&gt; et être suivit de 5 chiffres</span></p><p><span style=\" color:#ff0000;\">Ex: A12345</span></p><p><br/></p></body></html>"))
        self.pushButton_sup_gestion_animaux.setText(_translate("Dialog", "Supprimé un animal"))
        self.pushButton_deserialiser_gestion_animaux.setText(_translate("Dialog", "Désérialiser"))
        self.pushButton_menu_principale_gestion_animaux.setText(_translate("Dialog", "Menu principale"))
