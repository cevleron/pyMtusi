from PyQt6 import QtWidgets
from PyQt6 import uic
from math import cos, sin
from PyQt6 import QtGui

Form, Windows = uic.loadUiType('formula_lab_1.ui')
win = QtWidgets.QApplication([])
windows = Windows()
ui = Form()
ui.setupUi(windows)

ui.setupUi(windows)
ui.A.setValidator(QtGui.QDoubleValidator())
ui.ButtonRez.clicked.connect()

# Это место для кода

windows.show()
win.exec()