from PyQt5.QtWidgets import *
from  sürüyönetimi import Ui_MainWindow
from PyQt5.QtGui import *

class sürükontrol (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

uygulama = QApplication([])
pencere = sürükontrol()
pencere.show()
uygulama.exec_()