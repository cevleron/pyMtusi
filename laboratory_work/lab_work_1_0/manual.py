from math import sin, cos
from PyQt6 import QtGui, QtWidgets

from form import Ui_Dialog


def rezult():
    try:
        a = float(ui.A.text().replace(',', "."))
        # a = ui.A.serValue()
        # t = ui.T.value()
        z1 = 1 - (1 / 4) * (sin(2 * a) ** 2) + cos(2 * a)
        ui.rez1.setText(str(round(z1, 4)))
        z2 = (cos(a)) ** 2 + (cos(a)) ** 4
        ui.rez2.setText(str(round(z2, 4)))
    except ValueError:
        ui.A.setText('0')
        rezult()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.A.setText('2')

    ui.A.setValidator(QtGui.QDoubleValidator())
    ui.ButtonRezult.clicked.connect(rezult)
    # ui.ButtonClear.clicked.connect(navigator)

    Dialog.show()
    sys.exit(app.exec())
