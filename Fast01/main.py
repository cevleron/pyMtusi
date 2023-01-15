from PyQt6 import QtWidgets
from PyQt6 import uic
from math import tan, cos, pi, sin, log

from PyQt6 import QtGui


def rezult():
    x = float(ui.X.text().replace(',', "."))
    a = ui.A.value()
    print(x, a)
    print(type(x),type(a))

Form, Windows = uic.loadUiType('formula.ui')
win = QtWidgets.QApplication([])
windows = Windows()
ui = Form()

ui.setupUi(windows)
ui.X.setValidator(QtGui.QDoubleValidator())
ui.ButtonRez.clicked.connect(rezult)

#Это место для кода

windows.show()
win.exec()