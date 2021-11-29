from PyQt5.QtWidgets import *
from ders_11 import Ui_MainWindow

class Ders_11 (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("kırmızı",50) #"combox" a eleman ekledik.
        self.ui.comboBox.addItem("mavi",100) #"combox" a eleman ekledik.
        self.ui.comboBox.addItem("yeşil",150) #"combox" a eleman ekledik.
        self.ui.comboBox.addItem("Sarı") #"combox" a eleman ekledik.
        self.ui.comboBox_2.addItems(["elma","armut","ayva","çilek"]) #"combox_2" a  toplu eleman ekledik.
        self.ui.comboBox.insertItem(0,"seçiniz...") #"combox" a istediğimiz indexde gösterilcek eleman ekledik.
        self.ui.pushButton.clicked.connect(self.clear_combo_box) #"ComboBox_2" nin elemanlarını silmek için butona yönlendirdik.
        self.ui.comboBox.removeItem(0) #"ComboBox" daki ilk elemanı sildi.
        self.ui.pushButton_2.clicked.connect(self.show_combo_box_items) # "ComboBox" elemanlarını butona tıklandığında göstercek.
        self.ui.comboBox_3.addItems(["inek","aslan","köpek","kedi","koyun"])
        self.ui.comboBox_4.insertItem(0, "Seçiniz.....")
        self.ui.comboBox_4.addItems(["Ford","Fiat","BMW","Audi","Tofaş"])
        self.ui.comboBox_3.activated['int'].connect(self.item_show)
        self.ui.comboBox_4.currentIndexChanged['int'].connect(self.combo_box_4_index)

    def combo_box_4_index(self,current_index):
        if current_index !=0:
            print("current index : ",current_index)
            print("combo box item text : ",self.ui.comboBox_4.itemText(current_index))


    def item_show(self,activated_index):#"ComboBox_3"daki seçili elemanları gösterir.
        print("activated index : ",activated_index )
        print("activated text : ",self.ui.comboBox_3.itemText(activated_index))

    def  clear_combo_box (self):
        self.ui.comboBox_2.clear() # "ComboBox_2" deki bütün elemanları sildi.

    def show_combo_box_items(self):#"ComboBox" daki elemanları gösterir.
        text_number=self.ui.comboBox.currentIndex()+1
        text_items=self.ui.comboBox.currentText()
        text_index=self.ui.comboBox.currentIndex()
        text_data=self.ui.comboBox.currentData()
        print("text_items: ",text_items)
        print("text_index: ",text_index)
        print("text_number: ",text_number)
        print("text_data: ",text_data)

uygulama =QApplication([])
pencere = Ders_11()
pencere.show()
uygulama.exec_()