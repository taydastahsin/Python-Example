from PyQt5.QtWidgets import QApplication
from Main_sage_control import main_sage

app=QApplication([])
window=main_sage()
window.show()
app.exec_()