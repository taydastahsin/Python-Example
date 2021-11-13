from PyQt5.QtWidgets import *
from  ders_5 import  Ui_MainWindow

class ders_5 (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def myslot(self,index):
        self.ui.label.setText("değer: "+str(index))

uygulama = QApplication([])
pencere = ders_5()
pencere.show()
uygulama.exec_()