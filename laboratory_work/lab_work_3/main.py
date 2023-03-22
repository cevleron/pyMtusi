from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import uic
from PyQt6 import QtGui


Form, Windows = uic.loadUiType('formula.ui')
win = QApplication([])
windows = Windows()
ui = Form()
ui.setupUi(windows)

ui.setupUi(windows)
# ui.X.setValidator(QtGui.QDoubleValidator())
# ui.ButtonRez.clicked.connect()

# Это место для кода

windows.show()
win.exec()