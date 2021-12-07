from PyQt5.QtWidgets import QApplication
from ders15 import ders15_main

app =QApplication([])
window=ders15_main()
window.show()
app.exec_()