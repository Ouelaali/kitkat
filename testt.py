import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import QtCore

class user(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # titre
        self.setWindowTitle("Kit_Kat")
        self.setFixedSize(600, 300) 
        
        self.setLayout(qtw.QVBoxLayout())


        # chaine de caractere
        my_label = qtw.QLabel("Chaine de caractere")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)


        my_entry =qtw.QLineEdit()
        my_entry.setObjectName("chaine de caracteres")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton ("hash")
        my_button.setGeometry(200, 100, 100, 40)
        self.layout().addWidget(my_button)
        
    

       # hashed file
        my_labell = qtw.QLabel("Fichier hashé")
        my_labell.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_labell)

        my_entryy = qtw.QLineEdit()
        my_entryy.setObjectName("fichier hashé")
        my_entryy.setText("")
        self.layout().addWidget(my_entryy)
        self.show()

   
        

app = qtw.QApplication([])
u = user()
sys.exit(app.exec_())