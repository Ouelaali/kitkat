# Form implementation generated from reading ui file '/Users/linasmati/Documents/GitHub/kitkat/mon dossier/user.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(455, 257)
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(270, 140, 141, 71))
        self.pushButton.setObjectName("pushButton")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Widget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(100, 30, 251, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(370, 30, 58, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 140, 131, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 70, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.lineEdit.setText(_translate("Widget", "Chaine de caractere"))
        self.pushButton.setText(_translate("Widget", "Hash"))
        self.label_2.setText(_translate("Widget", "Low"))
        self.label_3.setText(_translate("Widget", "Hight"))
        self.pushButton_3.setText(_translate("Widget", "PushButton"))
        self.pushButton_2.setText(_translate("Widget", "hashed file"))