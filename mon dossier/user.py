import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5 import uic 

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("user.ui", self)
        self.setWindowTitle("User")
        self.show()

def button()
    button = QPushButton("CLICK", self) 

        
    button.setGeometry(200, 150, 100, 30) 

        
    button.clicked.connect(self.clickme) 

def clickme(self): 
    print("pressed") 

app = QApplication([])
window = MyGUI()


sys.exit(app.exec_())
