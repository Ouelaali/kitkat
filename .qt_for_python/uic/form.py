# Form implementation generated from reading ui file '/Users/linasmati/Documents/GitHub/kitkat/form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(466, 275)
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 30, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(320, 80, 111, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 160, 111, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView = QtWidgets.QListView(Widget)
        self.listView.setGeometry(QtCore.QRect(20, 70, 256, 192))
        self.listView.setObjectName("listView")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.lineEdit.setText(_translate("Widget", "Chaine de caractere"))
        self.pushButton.setText(_translate("Widget", "Hashed file"))
        self.pushButton_2.setText(_translate("Widget", "Hash"))
