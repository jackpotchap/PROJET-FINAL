# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/enclos/quitter_sans_terminer_enclos_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(366, 161)
        self.label_message_veut_Q_pop_up_enclos = QtWidgets.QLabel(Dialog)
        self.label_message_veut_Q_pop_up_enclos.setGeometry(QtCore.QRect(20, 10, 351, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_message_veut_Q_pop_up_enclos.setFont(font)
        self.label_message_veut_Q_pop_up_enclos.setObjectName("label_message_veut_Q_pop_up_enclos")
        self.pushButton_veut_Q_pop_up_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_veut_Q_pop_up_enclos.setGeometry(QtCore.QRect(190, 130, 71, 21))
        self.pushButton_veut_Q_pop_up_enclos.setObjectName("pushButton_veut_Q_pop_up_enclos")
        self.pushButton_veut_pas_Q_pop_up_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_veut_pas_Q_pop_up_enclos.setGeometry(QtCore.QRect(270, 130, 71, 21))
        self.pushButton_veut_pas_Q_pop_up_enclos.setObjectName("pushButton_veut_pas_Q_pop_up_enclos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_message_veut_Q_pop_up_enclos.setText(_translate("Dialog", "<html><head/><body><p>La procédure de deserialisation </p><p>n\'est pas completement terminer. </p><p>Êtte vous sure de vouloire quitter?</p></body></html>"))
        self.pushButton_veut_Q_pop_up_enclos.setText(_translate("Dialog", "Valider"))
        self.pushButton_veut_pas_Q_pop_up_enclos.setText(_translate("Dialog", "Annulez"))
