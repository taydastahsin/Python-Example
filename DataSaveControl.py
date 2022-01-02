from PyQt5.QtWidgets import *
from data_save import Ui_MainWindow
import json
import os

class Veri_Ekleme (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_2.clicked.connect(self.sil)
        self.ui.pushButton_3.clicked.connect(self.goster)

    def sil(self):
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()
        gcalisanlar = []
        for calisan in calisanlar:
            gcalisanlar.append(" ".join(calisan[:-2].split("-")))

        secim = int(self.ui.lineEdit.text()) - 1

        calisanlar.pop(secim - 1)
        sayac = 1
        dcalisanlar = []
        for calisan in calisanlar:
            dcalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac += 1
        with open("calisanlar.txt", "w") as dosya:
            dosya.writelines(dcalisanlar)

        a = self.ui.lineEdit.text()
        self.ui.tableWidget.removeRow(int(a) - 1)
        self.ui.lineEdit.clear()


    def save(self):
        a=self.ui.lineEdit.text()

        row =self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        self.ui.tableWidget.setItem(row,0,QTableWidgetItem(a))

        id = 1
        ad = a
        with open("calisanlar.txt", "r") as dosya:
            calısanliste = dosya.readline()
        if len(calısanliste) == 0:
            id = 1
        else:
            with open("calisanlar.txt", "r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
        with open("calisanlar.txt", "a+") as dosya:
            dosya.write("{}){}\n".format(id, ad))

        self.ui.lineEdit.clear()
    def goster(self):
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()
        gcalisanlar = []
        for calisan in calisanlar:
            a = 0
            gcalisanlar.append(" ".join(calisan[:-2].split("-")))
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(calisan[a]))
            a += 1


app =QApplication([])
window=Veri_Ekleme()
window.show()
app.exec_()