from math import tan, cos, pi, sin, log

from PyQt6 import QtGui, QtWidgets

from form import Ui_MainWindow


def rezult():
    try:
        x = float(ui.X.text().replace(',', "."))
        a = ui.A.value()
        # t = ui.T.value()
        y = (tan(x * x / 2 - 1)) ** 2 + 2 * cos(x - pi / 6) / (0.5 + sin(a) ** 2)
        ui.rez1.setText(str(round(y)))
        y = 2 ** (log((3 - cos(pi / 4 + 2 * x)), 3 + sin(x)) / (1 + tan(2 * x / pi) ** 2))
        ui.rez2.setText(str(round(y)))
    except ValueError:
        ui.X.setText('0')
        rezult()

def navigator():
    ui.A.setValue(12)
    ui.T.setValue(2)
    ui.X.setText("2")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.X.setText("2")

    ui.X.setValidator(QtGui.QDoubleValidator())
    ui.ButtonRez.clicked.connect(rezult)
    ui.ButtonClear.clicked.connect(navigator)

    MainWindow.show()
    sys.exit(app.exec())
