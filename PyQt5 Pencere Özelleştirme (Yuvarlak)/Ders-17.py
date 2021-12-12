from PyQt5.QtWidgets import *
from ders_17 import Ui_MainWindow
from PyQt5.QtGui import QRegion

class ders_17(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        my_region =QRegion(self.rect(),QRegion.Ellipse)
        self.setMask(my_region)

app = QApplication([])
window=ders_17()
window.show()
app.exec_()