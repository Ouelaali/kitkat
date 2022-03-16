import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # titre
        self.setWindowTitle("Kit_Kat")
        #self.setGeometry(100, 100, 500, 300) 
        self.setFixedSize(400, 500) 
  
        self.setLayout(qtw.QVBoxLayout())

        #creation des bouttons
        my_button = qtw.QPushButton("User")
        self.layout().addWidget(my_button)
        my_button.setFont(qtg.QFont('Helvetica', 30))
        #my_button.setStyleSheet ("border :5px solid ;")
                        


        my_button = qtw.QPushButton("Expert")
        self.layout().addWidget(my_button)
        my_button.setFont(qtg.QFont('Halvetica', 30))
        #my_button.setStyleSheet ("border :5px solid ;")

        my_button = qtw.QPushButton("Help")
        self.layout().addWidget(my_button)
        my_button.setFont(qtg.QFont('Halvetica', 30))
        #my_button.setStyleSheet ("border :5px solid ;")

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

sys.exit(app.exec_())

    
