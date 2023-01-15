from PyQt6 import QtWidgets
from PyQt6 import uic
from math import tan, cos, pi, sin, log
from PyQt6 import QtGui

Form, Windows = uic.loadUiType('formula.ui')
win = QtWidgets.QApplication([])
windows = Windows()
ui = Form()
ui.setupUi(windows)

ui.setupUi(windows)
ui.X.setValidator(QtGui.QDoubleValidator())
ui.ButtonRez.clicked.connect()

# Это место для кода

windows.show()
win.exec()
