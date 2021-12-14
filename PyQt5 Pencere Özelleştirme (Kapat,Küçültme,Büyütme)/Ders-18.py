from PyQt5.QtWidgets import QMainWindow ,qApp,QApplication
from ders_18 import Ui_MainWindow
from PyQt5.QtGui import QRegion

class ders_18(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.panel_mask()
        self.ui.pushButton.clicked.connect(self.close_button)
        self.ui.pushButton_2.clicked.connect(self.small_button)
        self.ui.pushButton_3.clicked.connect(self.big_button)

    def close_button(self):
        self.close()
    def small_button(self):
        self.showMinimized()
    def big_button(self):
        if self.isMaximized() :
            self.showNormal()
        else:
            self.showMaximized()
        self.panel_mask()
        self.showMaximized()

    def panel_mask(self):
        qApp.processEvents()
        my_region = QRegion(self.rect(), QRegion.Ellipse)
        self.setMask(my_region)




app = QApplication([])
window=ders_18()
window.show()
app.exec_()