from PyQt5.QtWidgets import*
from ders_1 import Ui_MainWindow

class ders1(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setText("Merhaba Tahsin Bey ")

uygulama =QApplication([])
pencere =ders1()
pencere.show()
uygulama.exec_()

