from PyQt5.QtWidgets import *
from ders_3 import Ui_MainWindow

class ders_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

uygulama = QApplication ([])
pencere = ders_3 ()
pencere.show()
uygulama.exec_()