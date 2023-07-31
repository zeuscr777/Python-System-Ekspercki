produkty = []
produktyIlosc = {}

class Produkt:
    def __init__(self, nazwa, cena, typ):
        self.nazwa = nazwa
        self.cena = cena
        self.typ = typ

class Mleko(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.99, "Nabial")

class Chleb(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 3.20, "Pieczywo")

class Maka(Produkt):
    def __init__(self):
        super().__init__( __class__.__name__, 2.50, "Zboza")

class Makaron(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 4.00, "Zboza")

class Ryz(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 3.50, "Zboza")

class Kasza(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 3.10, "Zboza")

class Cukier(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.99, "Inne")

class BulkaTarta(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.60, "Inne")

class Smietana(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 1.80, "Nabial")

class Jaja(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 8.50, "Nabial")

class Kielbaska(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 9.99, "Mieso")

class Lody(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.50, "Inne")

class Woda6pak(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 12.00, "Napoj")

class Piwo4pak(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 14.50, "Napoj")

class SosChinski(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 6.98, "Inne")

class Pomidor(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 1.50, "Warzywo")

class Ogorek(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.39, "Warzywo")

class Jablko(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.00, "Owoc")

class Pomarancza(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 1.80, "Owoc")

class Kiwi(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 2.20, "Owoc")

class Ananas(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 9.20, "Owoc")

class Mango(Produkt):
    def __init__(self):
        super().__init__(__class__.__name__, 5.99, "Owoc")

produkty.append(Mleko())
produkty.append(Chleb())
produkty.append(Maka())
produkty.append(Makaron())
produkty.append(Ryz())
produkty.append(Kasza())
produkty.append(Cukier())
produkty.append(BulkaTarta())
produkty.append(Smietana())
produkty.append(Jaja())
produkty.append(Kielbaska())
produkty.append(Lody())
produkty.append(Woda6pak())
produkty.append(Piwo4pak())
produkty.append(SosChinski())
produkty.append(Pomidor())
produkty.append(Ogorek())
produkty.append(Jablko())
produkty.append(Pomarancza())
produkty.append(Kiwi())
produkty.append(Ananas())
produkty.append(Mango())

#Funkcja, która tworzy dynamiczną listę produktów z ilością (domyślnie = 0)
def addProductsPrize():
    for i in produkty:
        produktyIlosc[i.nazwa] = 0

addProductsPrize()
