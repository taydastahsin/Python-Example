from PyQt5.QtWidgets import *
from  ders_7 import Ui_MainWindow

class Ders_7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionTree.triggered.connect(self.tree_selected)
        self.ui.actionGirl.triggered.connect(self.girl_selected)
        self.ui.actionLion.triggered.connect(self.lion_selected)

    def tree_selected (self):
        self.ui.label.setText("Ağaç Resmi")
        self.ui.frame.setStyleSheet("border-image: url(:/Tree/Resimler/tree.jpg)")

    def girl_selected (self):
        self.ui.label.setText("Kadın Resmi")
        self.ui.frame.setStyleSheet("border-image: url(:/Girl/Resimler/girl.jpg)")


    def lion_selected (self):
        self.ui.label.setText("Aslan Resmi")
        self.ui.frame.setStyleSheet("border-image: url(:/Lion/Resimler/lion.jpg)")





uygulama =QApplication([])
pencere = Ders_7()
pencere.show()
uygulama.exec_()