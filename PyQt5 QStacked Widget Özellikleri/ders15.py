from PyQt5.QtWidgets import *
from ders_15 import Ui_MainWindow

class ders15_main (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.kitap_ekle_index  = 0
        self.uye_ekle_index  = 1
        self.uye_listesi_index = 2
        self.home_page_index = 3
        self.kitap_listesi_index = 4

        self.ui.actionAna_Sayfa.triggered.connect(self.go_home_page)
        self.ui.actionKitap_Listesi.triggered.connect(self.go_kitap_listesi)
        self.ui.actionKitap_Ekle.triggered.connect(self.go_kitap_ekle)
        self.ui.action_ye_Listesi.triggered.connect(self.go_uye_listesi)
        self.ui.action_ye_Ekle.triggered.connect(self.go_uye_ekle)


    def go_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(self.home_page_index)
    def go_kitap_listesi(self):
        self.ui.stackedWidget.setCurrentIndex(self.kitap_listesi_index)
    def go_kitap_ekle(self):
        self.ui.stackedWidget.setCurrentIndex(self.kitap_ekle_index)
    def go_uye_listesi(self):
        self.ui.stackedWidget.setCurrentIndex(self.uye_listesi_index)
    def go_uye_ekle(self):
        self.ui.stackedWidget.setCurrentIndex(self.uye_ekle_index)



