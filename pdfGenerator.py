from fpdf import FPDF
from experta import *
from experta.utils import *
import os
from datetime import date
from v1 import *
from engineRun import *

class PDF(FPDF):
    def titles(self, komunikat2, komunikat3, komunikat4):
        self.set_xy(0.0,20)
        self.set_font('Courier', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.multi_cell(w=210.0, h=10.0, align='C', txt="UWB MARKET \n 13-540 Bialystok ul. Ciolkowskiego 3 \n Wydzial Informatyki SA \n NIP 901738146213", border=0)

        self.multi_cell(w=210.0, h=10.0, align='L', txt=f'{date.today()}', border=0)

        self.set_font('Courier', 'B', 24)
        self.multi_cell(w=190.0, h=10.0, align='C', txt="PARAGON FISKALNY", border=0)

        self.set_font('Courier', 'B', 12)
        self.multi_cell(w=190.0, h=10.0, align='J', txt=komunikat2, border=0)
        self.multi_cell(w=190.0, h=10.0, align='C', txt="- - - - - - - - - - - - - - - - -", border=0)
        self.multi_cell(w=190.0, h=10.0, align='C', txt="RABATY", border=0)

        self.multi_cell(w=190.0, h=10.0, align='L', txt=str(komunikat3[8:]), border=0)

        self.multi_cell(w=190.0, h=10.0, align='C', txt="- - - - - - - - - - - - - - - - -", border=0)
        self.set_font('Courier', 'B', 24)

        self.multi_cell(w=190.0, h=10.0, align='C', txt=f'SUMA: {komunikat4} zl', border=0)

    def lines(self):
        self.rect(5.0, 5.0, 200.0,287.0)
        self.rect(8.0, 8.0, 194.0,282.0)
