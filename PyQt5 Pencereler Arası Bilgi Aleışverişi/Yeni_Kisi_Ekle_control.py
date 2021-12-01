from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from yeni_kisi_ekle import Ui_MainWindow

class yeni_kisi(QMainWindow):

    new_signal_slot =pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_back_main)

    def add_back_main (self):
        new_name =self.ui.lineEdit.text()
        self.new_signal_slot.emit(new_name)
        self.ui.lineEdit.clear()

