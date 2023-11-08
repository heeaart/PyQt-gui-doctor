# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1020, 607)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("rgb(255, 170, 127);")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 80, 231, 41))
        self.lineEdit_name.setStyleSheet("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_2_surname = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2_surname.setGeometry(QtCore.QRect(40, 200, 231, 41))
        self.lineEdit_2_surname.setStyleSheet("")
        self.lineEdit_2_surname.setObjectName("lineEdit_2_surname")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 141, 31))
        self.label_2.setObjectName("label_2")
        self.checkBox_wizyta = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox_wizyta.setEnabled(True)
        self.checkBox_wizyta.setGeometry(QtCore.QRect(40, 290, 261, 41))
        self.checkBox_wizyta.setStyleSheet("")
        self.checkBox_wizyta.setChecked(True)
        self.checkBox_wizyta.setObjectName("checkBox_wizyta")
        self.pushButton_zarezerwuj = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_zarezerwuj.setGeometry(QtCore.QRect(430, 280, 191, 61))
        self.pushButton_zarezerwuj.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 25%;")
        self.pushButton_zarezerwuj.setObjectName("pushButton_zarezerwuj")
        self.label_3_wynik = QtWidgets.QLabel(parent=Dialog)
        self.label_3_wynik.setGeometry(QtCore.QRect(40, 350, 941, 241))
        self.label_3_wynik.setStyleSheet("b")
        self.label_3_wynik.setText("")
        self.label_3_wynik.setObjectName("label_3_wynik")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(500, 80, 194, 146))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_internista = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_internista.setObjectName("radioButton_internista")
        self.verticalLayout.addWidget(self.radioButton_internista)
        self.radioButton_pediatra = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_pediatra.setObjectName("radioButton_pediatra")
        self.verticalLayout.addWidget(self.radioButton_pediatra)
        self.radioButton_dermatolog = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_dermatolog.setObjectName("radioButton_dermatolog")
        self.verticalLayout.addWidget(self.radioButton_dermatolog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Imie"))
        self.label_2.setText(_translate("Dialog", "Nazwisko"))
        self.checkBox_wizyta.setText(_translate("Dialog", "Wizyta prywatna"))
        self.pushButton_zarezerwuj.setText(_translate("Dialog", "Zarezerwuj"))
        self.radioButton_internista.setText(_translate("Dialog", "Internista"))
        self.radioButton_pediatra.setText(_translate("Dialog", "Pediatra"))
        self.radioButton_dermatolog.setText(_translate("Dialog", "Dermatolog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())