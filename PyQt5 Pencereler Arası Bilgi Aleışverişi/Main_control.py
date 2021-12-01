from PyQt5.QtWidgets import *
from main import Ui_MainWindow
from Yeni_Kisi_Ekle_control import yeni_kisi

class ders_13_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.Yeni_Kisi_Ekle = yeni_kisi()
        self.ui.pushButton.clicked.connect(self.people_add)
        self.Yeni_Kisi_Ekle.new_signal_slot.connect(self.add_user_item)

    def add_user_item (self,name):
        self.ui.comboBox.addItem(name)
        self.Yeni_Kisi_Ekle.close()

    def people_add (self):
       self.Yeni_Kisi_Ekle.show()

