# Form implementation generated from reading ui file 'formula_lab_1.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 482)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 30, 638, 421))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("formula1.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.rez1 = QtWidgets.QLabel(self.widget)
        self.rez1.setMinimumSize(QtCore.QSize(0, 110))
        self.rez1.setObjectName("rez1")
        self.horizontalLayout_3.addWidget(self.rez1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("formula2.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.rez2 = QtWidgets.QLabel(self.widget)
        self.rez2.setMinimumSize(QtCore.QSize(0, 110))
        self.rez2.setObjectName("rez2")
        self.horizontalLayout_4.addWidget(self.rez2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(85, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.A = QtWidgets.QLineEdit(self.widget)
        self.A.setMinimumSize(QtCore.QSize(361, 35))
        self.A.setObjectName("A")
        self.horizontalLayout_7.addWidget(self.A)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(85, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.T = QtWidgets.QDoubleSpinBox(self.widget)
        self.T.setMinimumSize(QtCore.QSize(361, 35))
        self.T.setObjectName("T")
        self.horizontalLayout_8.addWidget(self.T)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ButtonClear = QtWidgets.QPushButton(self.widget)
        self.ButtonClear.setMinimumSize(QtCore.QSize(165, 75))
        self.ButtonClear.setObjectName("ButtonClear")
        self.horizontalLayout_9.addWidget(self.ButtonClear)
        self.ButtonRezult = QtWidgets.QPushButton(self.widget)
        self.ButtonRezult.setMinimumSize(QtCore.QSize(165, 75))
        self.ButtonRezult.setObjectName("ButtonRezult")
        self.horizontalLayout_9.addWidget(self.ButtonRezult)
        self.ButtonClose = QtWidgets.QPushButton(self.widget)
        self.ButtonClose.setMinimumSize(QtCore.QSize(165, 75))
        self.ButtonClose.setObjectName("ButtonClose")
        self.horizontalLayout_9.addWidget(self.ButtonClose)
        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.ButtonClear.clicked.connect(self.rez1.clear) # type: ignore
        self.ButtonClear.clicked.connect(self.rez2.clear) # type: ignore
        self.ButtonClear.clicked.connect(self.A.clear) # type: ignore
        self.ButtonClear.clicked.connect(self.T.clear) # type: ignore
        self.ButtonClose.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "1)"))
        self.label_6.setText(_translate("Dialog", "Ответ:"))
        self.rez1.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "2)"))
        self.label_5.setText(_translate("Dialog", "Ответ:"))
        self.rez2.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "А"))
        self.label_8.setText(_translate("Dialog", "Точность"))
        self.ButtonClear.setText(_translate("Dialog", "Очистить"))
        self.ButtonRezult.setText(_translate("Dialog", "Посчитать"))
        self.ButtonClose.setText(_translate("Dialog", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())