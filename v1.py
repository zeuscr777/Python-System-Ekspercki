from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from random import choice
from experta import *
import time
from fpdf import FPDF
import os
from datetime import date
import unidecode

#Załączanie innych plików
from products import *
from engineRun import *
from pdfGenerator import *

komunikat2 = ""
komunikat3 = ""
komunikat4 = ""

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Dodaj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dodaj.setGeometry(QtCore.QRect(320, 230, 83, 81))
        self.pushButton_Dodaj.setObjectName("pushButton_Dodaj")
        self.pushButton_Przelicz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Przelicz.setGeometry(QtCore.QRect(300, 320, 120, 31))
        self.pushButton_Przelicz.setObjectName("pushButton_Przelicz")

        self.pushButton_Zastosuj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Zastosuj.setGeometry(QtCore.QRect(300, 410, 120, 31))
        self.pushButton_Zastosuj.setObjectName("pushButton_Zastosuj")

        self.pushButton_GenerujPdf = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GenerujPdf.setGeometry(QtCore.QRect(300, 450, 120, 31))
        self.pushButton_GenerujPdf.setObjectName("pushButton_GenerujPdf")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 550, 221, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 550, 661, 300))
        self.label_2.setObjectName("label_2")
        self.listWidget_Produkty = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Produkty.setGeometry(QtCore.QRect(20, 40, 201, 500))
        self.listWidget_Produkty.setObjectName("listWidget_Produkty")

        for i in range(len(produkty)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget_Produkty.addItem(item)

        self.listWidget_Koszyk = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Koszyk.setGeometry(QtCore.QRect(440, 40, 211, 500))
        self.listWidget_Koszyk.setObjectName("listWidget_Koszyk")
        self.listWidget_Cena = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Cena.setGeometry(QtCore.QRect(220, 40, 71, 500))
        self.listWidget_Cena.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_Cena.setProperty("showDropIndicator", True)
        self.listWidget_Cena.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_Cena.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget_Cena.setObjectName("listWidget_Cena")

        for i in range(len(produkty)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget_Cena.addItem(item)

        self.listWidget_Cena2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Cena2.setGeometry(QtCore.QRect(720, 40, 71, 500))
        self.listWidget_Cena2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_Cena2.setProperty("showDropIndicator", True)
        self.listWidget_Cena2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_Cena2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget_Cena2.setObjectName("listWidget_Cena2")
        self.listWidget_Ilosc = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Ilosc.setGeometry(QtCore.QRect(650, 40, 71, 500))
        self.listWidget_Ilosc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_Ilosc.setProperty("showDropIndicator", True)
        self.listWidget_Ilosc.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_Ilosc.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget_Ilosc.setObjectName("listWidget_Ilosc")
        self.label_Produkty = QtWidgets.QLabel(self.centralwidget)
        self.label_Produkty.setGeometry(QtCore.QRect(20, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Produkty.setFont(font)
        self.label_Produkty.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Produkty.setObjectName("label_Produkty")
        self.label_Cena = QtWidgets.QLabel(self.centralwidget)
        self.label_Cena.setGeometry(QtCore.QRect(220, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Cena.setFont(font)
        self.label_Cena.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Cena.setObjectName("label_Cena")
        self.label_Koszyk = QtWidgets.QLabel(self.centralwidget)
        self.label_Koszyk.setGeometry(QtCore.QRect(440, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Koszyk.setFont(font)
        self.label_Koszyk.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Koszyk.setObjectName("label_Koszyk")
        self.label_Ilosc = QtWidgets.QLabel(self.centralwidget)
        self.label_Ilosc.setGeometry(QtCore.QRect(650, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Ilosc.setFont(font)
        self.label_Ilosc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ilosc.setObjectName("label_Ilosc")
        self.label_Cena2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Cena2.setGeometry(QtCore.QRect(720, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Cena2.setFont(font)
        self.label_Cena2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Cena2.setObjectName("label_Cena2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_Dodaj.clicked.connect(self.dodaj) #Na kliknięcie przycisku "Dodaj" wywoła funkcje "dodaj"
        self.pushButton_Przelicz.clicked.connect(self.wyczysc_koszyk) #Na kliknięcie przycisku "Przelicz" wywoła funkcje "wyczysc koszyk"
        self.pushButton_Zastosuj.clicked.connect(self.zastosuj) #Na kliknięcie przycisku "Zastosuj" wywoła funkcję "Zastosuj" - stosuje podane reguły
        self.pushButton_GenerujPdf.clicked.connect(self.generuj_pdf) #Na kliknięcie przycisku "Generuj pdf" wywoła funkcję "Generuj pdf" - generuj pdf z rachunkiem i zastosowanymi regułami

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Dodaj.setText(_translate("MainWindow", ">>"))
        self.pushButton_Przelicz.setText(_translate("MainWindow", "Wyczyść koszyk"))
        self.pushButton_Zastosuj.setText(_translate("MainWindow", "Zastosuj"))
        self.pushButton_GenerujPdf.setText(_translate("MainWindow", "Generuj PDF"))

        self.label.setText(_translate("MainWindow", "Do zapłaty:"))
        self.label_2.setText(_translate("MainWindow", "PARAGON FISKALNY:"))
        __sortingEnabled = self.listWidget_Produkty.isSortingEnabled()
        self.listWidget_Produkty.setSortingEnabled(False)

        for i in range(len(produkty)):
            item = self.listWidget_Produkty.item(i)
            name = produkty[i].nazwa
            item.setText(_translate("MainWindow", name))

        self.listWidget_Produkty.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_Cena.isSortingEnabled()
        self.listWidget_Cena.setSortingEnabled(False)

        for i in range(len(produkty)):
            item = self.listWidget_Cena.item(i)
            prize = produkty[i].cena
            item.setText(_translate("MainWindow", str(("%.2f" %prize)) + " zł"))

        self.listWidget_Cena.setSortingEnabled(__sortingEnabled)
        self.label_Produkty.setText(_translate("MainWindow", "Produkty:"))
        self.label_Cena.setText(_translate("MainWindow", "Cena:"))
        self.label_Koszyk.setText(_translate("MainWindow", "Koszyk:"))
        self.label_Ilosc.setText(_translate("MainWindow", "Ilość:"))
        self.label_Cena2.setText(_translate("MainWindow", "Cena:"))

    def dodaj(self):
        global do_zaplaty
        item = QtWidgets.QListWidgetItem()
        ii = self.listWidget_Produkty.currentItem().text() #Pobiera do zmiennej zaznaczony element z listy produktów
        produktyIlosc[ii] = produktyIlosc.get(ii) + 1

        self.listWidget_Koszyk.clear() #Usuwamy zawartość listy
        self.listWidget_Ilosc.clear() #Usuwamy zawartość listy
        self.listWidget_Cena2.clear() #Usuwamy zawartość listy

        do_zaplaty = 0
        for i in produktyIlosc: #Zapełniamy koszyk produktami i ich ilością
            if(produktyIlosc[i] > 0):
                self.listWidget_Koszyk.addItem(i)
                self.listWidget_Ilosc.addItem(str(produktyIlosc[i]))
                x = list(produktyIlosc.keys()).index(i)
                self.listWidget_Cena2.addItem(str("%.2f" % (produktyIlosc[i]*produkty[x].cena)) + " zł")
                do_zaplaty = do_zaplaty + (produktyIlosc[i]*produkty[x].cena)

        komunikat = "Do zapłaty: " + str("%.2f" % do_zaplaty) + " zł"
        self.label.setText(str(komunikat))

    def wyczysc_koszyk(self):
        global do_zaplaty
        self.listWidget_Koszyk.clear() #Usuwamy zawartość listy
        self.listWidget_Ilosc.clear() #Usuwamy zawartość listy
        self.listWidget_Cena2.clear() #Usuwamy zawartość listy
        produktyIlosc.clear()
        addProductsPrize()

        do_zaplaty = ""
        komunikat = "Do zapłaty: "
        self.label.setText(str(komunikat))

    def generuj_pdf(self):
        global komunikat2, komunikat3, komunikat4
        pdf = PDF()
        pdf.add_page()
        pdf.titles(komunikat2, komunikat3, komunikat4)
        pdf.lines()
        pdf.output('Rachunek.pdf','F')
        path = 'Rachunek.pdf'
        os.system(path)

    def zastosuj(self):
        global komunikat2, komunikat3, komunikat4, do_zaplaty

        komunikat = "PARAGON FISKALNY:\n"
        komunikat2 = ""

        for i in produktyIlosc:
            if (produktyIlosc[i] > 0):
                x = list(produktyIlosc.keys()).index(i)
                suma_zl = produktyIlosc[i]*produkty[x].cena
                komunikat = f'{komunikat} {i} {produktyIlosc[i]} szt. * {str("%.2f" % produkty[x].cena)} = {str("%.2f" % suma_zl)} zł\n'
                komunikat2 = f'{komunikat2} {i}    {produktyIlosc[i]}x{str("%.2f" % produkty[x].cena)}    {str("%.2f" % suma_zl)} zł\n'

        komunikat2 = unidecode.unidecode(komunikat2)

        engine = SilnikPromocje()
        engine.reset()
        engine.declare(Oferta(produkty = produkty), Oferta(produktyIlosc = produktyIlosc))
        engine.run()

        self.label_2.setText(f'{komunikat} {engine.komunikatDiscount} \n Suma: {str("%.2f" % (do_zaplaty - engine.naliczoneRabaty))} zł')

        komunikat3 = unidecode.unidecode(engine.komunikatDiscount)
        komunikat4 = unidecode.unidecode(str("%.2f" % (do_zaplaty - engine.naliczoneRabaty)))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
