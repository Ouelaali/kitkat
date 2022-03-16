import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("form.ui", self)
        self.setWindowTitle("User")
        self.show()


app = QApplication([])
window = MyGUI()


sys.exit(app.exec_())