from PyQt5.QtWidgets import *
from ders_6 import Ui_MainWindow

class ders_6(QMainWindow):
     def __init__(self):
         super().__init__()
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)
         self.ui.actionSpor.triggered.connect(self .selectc)
         self.ui.actionC.triggered.connect(self.selectcc)
         self.ui.actionPython.triggered.connect(self.selectp)

     def selectc(self):
         print("C++ dili")

     def selectcc(self):
         print("C# dili")

     def selectp(self):
         print("Python dili")


uygulama =QApplication([])
pencere =ders_6()
pencere.show()
uygulama.exec_()
