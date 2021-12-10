from PyQt5.QtWidgets import *
from ders_16 import Ui_MainWindow

class Ders_16 (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
    def close_tab (self,index):
        print ("kapatılan :",index)




app=QApplication([])
window=Ders_16()
window.show()
app.exec_()