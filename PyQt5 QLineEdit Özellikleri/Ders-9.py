from PyQt5.QtWidgets import *
from  ders_9 import Ui_MainWindow
from PyQt5.QtGui import QIntValidator

class Ders_9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
    #   self.ui.lineEdit_16.setEnabled(False) #line edit kullanıcı tarafından kullanılmaz.
        self.ui.lineEdit_16.returnPressed.connect(self.process)
        self.ui.lineEdit_19.setValidator(QIntValidator(0,10,self))
        self.ui.lineEdit_20.setReadOnly(True) # line edit kullanıcı yazısı değiştirmeme
        self.ui.lineEdit_21.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_22.setPlaceholderText("telefon numarası giriniz 05....")
        self.ui.lineEdit_22.setValidator(QIntValidator(0,100000000,self))
        self.ui.lineEdit_23.setToolTip("TC Kimlik numarası giriniz!!!!")
        self.ui.lineEdit_24.setDragEnabled(True) # line edit te yazılan yazıyı seçerek tutup istediğimiz yere kopyalıyoruz.
        self.ui.lineEdit_25.setMaxLength(3) # Line edit te yazı sayısını kısıtlıyor.
    def process(self):
        line_yazı=self.ui.lineEdit_16.text() # line edit kısmında yazılan yazıyı "line_yazı" atadık
        print("alınan yazı",line_yazı)
        line_okuma =self.ui.lineEdit_17.text()
        print("alınna yazılar",line_yazı+line_okuma)
        self.ui.lineEdit_18.setText(line_yazı+line_okuma)


uygulama =QApplication([])
pencere =Ders_9()
pencere.show()
uygulama.exec_()