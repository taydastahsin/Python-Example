from PyQt5.QtWidgets import *
from ders4 import Ui_MainWindow

class ders_4 (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

uygulama = QApplication([])
pencere = ders_4()
pencere.show()
uygulama.exec_()