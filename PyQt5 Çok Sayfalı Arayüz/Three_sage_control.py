from PyQt5.QtWidgets import *
from three_sage import Ui_MainWindow

class three_sage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)