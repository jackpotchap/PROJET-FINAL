# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/animaux/quitter_sans_terminer_animaux_deserialiser_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 142)
        self.label_message_veut_Q_pop_up_animaux = QtWidgets.QLabel(Dialog)
        self.label_message_veut_Q_pop_up_animaux.setGeometry(QtCore.QRect(0, -10, 351, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_message_veut_Q_pop_up_animaux.setFont(font)
        self.label_message_veut_Q_pop_up_animaux.setObjectName("label_message_veut_Q_pop_up_animaux")
        self.pushButton_veut_pas_Q_pop_up_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_veut_pas_Q_pop_up_animaux.setGeometry(QtCore.QRect(260, 90, 71, 21))
        self.pushButton_veut_pas_Q_pop_up_animaux.setObjectName("pushButton_veut_pas_Q_pop_up_animaux")
        self.pushButton_veut_Q_pop_up_animaux = QtWidgets.QPushButton(Dialog)
        self.pushButton_veut_Q_pop_up_animaux.setGeometry(QtCore.QRect(180, 90, 71, 21))
        self.pushButton_veut_Q_pop_up_animaux.setObjectName("pushButton_veut_Q_pop_up_animaux")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_message_veut_Q_pop_up_animaux.setText(_translate("Dialog", "<html><head/><body><p>Tous changement effectuez seras perdu.</p><p>Êtte-vous sure de vouloire quitter?</p></body></html>"))
        self.pushButton_veut_pas_Q_pop_up_animaux.setText(_translate("Dialog", "Annulez"))
        self.pushButton_veut_Q_pop_up_animaux.setText(_translate("Dialog", "Valider"))