from PyQt5.QtWidgets import *
from ders_2 import Ui_MainWindow
from  PyQt5.QtGui import QIcon

class ders_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ders 2 ")


uygulama = QApplication ([])
pencere = ders_2 ()
pencere.show()
uygulama.exec_()