from PyQt5.QtWidgets import *
from ders_14 import Ui_MainWindow

class ders_14(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.critical_text)
        self.ui.pushButton_2.clicked.connect(self.information_text)
        self.ui.pushButton_3.clicked.connect(self.qestion_text)
        self.ui.pushButton_4.clicked.connect(self.warning_text)
        self.ui.pushButton_5.clicked.connect(self.about_text)
        self.ui.pushButton_6.clicked.connect(self.qtabout_text)
        self.ui.pushButton_7.clicked.connect(self.number_text)

    def critical_text(self):
        QMessageBox.critical(self,"Critical message","Bu kritik bir mesajdır.")
    def information_text(self):
        result=  QMessageBox.information(self, "Information message", "Bu bir  bilgi  mesajıdır.",QMessageBox.Yes,QMessageBox.No)
        if result == QMessageBox.Yes:
            print("Yes")
        elif result == QMessageBox.No:
            print("No")
    def qestion_text(self):
         QMessageBox.question(self,"Qestion message","Bu bir soru mesajdır.",QMessageBox.Open|QMessageBox.Close|QMessageBox.Yes|QMessageBox.No)
    def warning_text(self):
        QMessageBox.warning(self,"Warning message","Tehlike mesajıdır.")
    def about_text(self):
        QMessageBox.about(self," Ders 14 Hakkında","< font size = 5 >Bu kısımda about aracının nasıl kullanıldığını ve <b>kullanıcıya</b> yazılan uygulama hakkında bilgi vermek için kullanabilceğimizi gösterir."
                          " </font> "
                          "<a href =\"https://github.com/taydastahsin\">Github </a>")
    def qtabout_text(self):
        QMessageBox.aboutQt(self,"QT Hakkında")
    def number_text(self):
        message_box =QMessageBox()
        message_box.setIcon(QMessageBox.Qestion)
        message_box.setText("hangi sayıları kullanmak istiyorsunuz ?")
        message_box.setWindowTitle("Özel Kulanım")
        message_box.standardButton(QMessageBox.Yes | QMessageBox.No)
        message_box.setEscapeButton(QMessageBox.Yes)

        button_evet =message_box.button(QMessageBox.Yes)
        button_evet.setText("Tek sayılar")

        button_hayır =message_box.button(QMessageBox.No)
        button_hayır.setText("Çift sayılar")

        result = message_box.exec_()


app=QApplication([])
window=ders_14()
window.show()
app.exec_()