import random
import sys

from PyQt6.QtWidgets import QDialog, QApplication


from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_zarezerwuj.clicked.connect(self.wynik)
        self.show()

    def wynik(self):
        lekarz = ""
        cena = 0
        dni = 0

        if self.ui.radioButton_internista.isChecked():
            lekarz = "Internista"
        elif self.ui.radioButton_pediatra.isChecked():
            lekarz = "Pediatra"
        elif self.ui.radioButton_dermatolog.isChecked():
            lekarz = "Dermatolog"

        if self.ui.checkBox_wizyta.isChecked():
            cena = 200
            dni = random.randrange(1,14)
        else:
            cena = 0
            dni = random.randrange(1,1000)
        if self.ui.lineEdit_name.text() == "" or self.ui.lineEdit_2_surname.text() == "":
            self.ui.label_3_wynik.setText("wypelnij pole imie lub nazwisko")
        else:
            self.ui.label_3_wynik.setText(f'Pomyślnie zarezerwowano wizytę u lekarza: {lekarz}.\nTermin wizyty przypada za: {dni}.\nKoszt wizyty: {cena}.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
