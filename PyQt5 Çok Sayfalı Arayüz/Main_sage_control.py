from PyQt5.QtWidgets import *
from main_sage import Ui_MainWindow
from One_sage_control import one_sage
from Two_sage_control import two_sage
from Three_sage_control import  three_sage

class main_sage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_one_sage)
        self.ui.pushButton_2.clicked.connect(self.open_two_sage)
        self.ui.pushButton_3.clicked.connect(self.open_three_sage)
        self.One_sage_control =one_sage()
        self.Two_sage_control =two_sage()
        self.Three_sage_control =three_sage()

    def open_one_sage(self):
        self.One_sage_control.show()
        self.Two_sage_control.hide()
        self.Three_sage_control.hide()
    def open_two_sage(self):
        self.Two_sage_control.show()
        self.One_sage_control.hide()
        self.Three_sage_control.hide()
    def open_three_sage(self):
        self.Three_sage_control.show()
        self.Two_sage_control.hide()
        self.One_sage_control.hide()