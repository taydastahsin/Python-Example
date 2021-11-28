from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon ,QKeySequence
from PyQt5.QtCore import Qt
from ders_10 import Ui_MainWindow

class Ders_10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.setText("Tahsin Taydaş")
        self.ui.pushButton_3.setIcon(QIcon(":/icons/laptop_2.ico"))
        self.ui.pushButton_3.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.ui.pushButton_5.pressed.connect(self.start_button)
        self.ui.pushButton_5.released.connect(self.stop_button)
        self.ui.pushButton_6.clicked['bool'].connect(self.bool_control)
        self.ui.pushButton_7.clicked.connect(self.clicked_button)
        self.ui.pushButton_7.setToolTip("Başlatmak için F6 bas")
        self.ui.pushButton_7.setShortcut(QKeySequence("F6"))
        self.ui.pushButton_8.released.connect(self.released_button)

    def released_button(self):
        self.ui.pushButton_8.setStyleSheet("background-color: rgba(255,0,0)")
    def start_button(self):
        self.ui.pushButton_5.setIcon(QIcon(":/icons/start.ico"))
    def stop_button(self):
        self.ui.pushButton_5.setIcon(QIcon(":/icons/stop.ico"))
    def clicked_button(self):
        print("Tuşa basıldı.")

    def bool_control(self,state):
        print("state :",state)

        if state:
            self.ui.pushButton_6.setText("Stop")
        else:
            self.ui.pushButton_6.setText("Start")


uygulama =QApplication([])
pencere =Ders_10()
pencere.show()
uygulama.exec_()