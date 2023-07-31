from experta import *
from experta.utils import *

class Oferta(Fact):
    pass

class SilnikPromocje(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.produkty=[]
        self.produktyIlosc={}
        self.naliczoneRabaty = 0
        self.komunikatDiscount = "\nRABAT:\n"
        self.typeProducts = {}

    def getAmount(self, product):
        return self.produktyIlosc[product]

    def discountsSum(self, product, discount):
        whichProduct = list(self.produktyIlosc.keys()).index(product)
        discountAll = discount*(self.produktyIlosc[product]*self.produkty[whichProduct].cena)
        self.naliczoneRabaty = self.naliczoneRabaty + discount*(self.produktyIlosc[product]*self.produkty[whichProduct].cena)
        return discountAll

    def discountsGratis(self, product, count):
        whichProduct = list(self.produktyIlosc.keys()).index(product)
        discountAll = self.produkty[whichProduct].cena
        self.naliczoneRabaty = self.naliczoneRabaty + self.produkty[whichProduct].cena
        return discountAll

    def discountsMultiple(self, product, discount, count):
        whichProduct = list(self.produktyIlosc.keys()).index(product)

        if(self.produktyIlosc[product] % count == 0):
            discountAll = (self.produktyIlosc[product] / count) * (discount * self.produkty[whichProduct].cena)
        else:
            discountAll = (self.produktyIlosc[product] - (self.produktyIlosc[product] % count)) / count * (discount * self.produkty[whichProduct].cena)

        self.naliczoneRabaty = self.naliczoneRabaty + discountAll
        return discountAll

    def funkcja1(self, product1, count1, product2, count2):
        whichProduct1 = list(self.produktyIlosc.keys()).index(product1)
        whichProduct2 = list(self.produktyIlosc.keys()).index(product2)

    def assignType(self):
        x = 0
        for i in self.produkty:
            self.typeProducts[i.nazwa] = self.produkty[x].typ
            x+=1
        print(self.typeProducts)

    #Reguła, która przypisze sobie do zmiennych produkty oraz ich ilości
    @Rule(AS.i << Oferta(produkty=MATCH.produkty) & AS.j << Oferta(produktyIlosc=MATCH.produktyIlosc))
    def przekazZmienne(self, i, j):
        self.produkty = unfreeze(i["produkty"])
        self.produktyIlosc = unfreeze(j["produktyIlosc"])
        self.assignType()

    #Promocja1: Kup min. 4 cukry i zapłać 20% sumy za cukry
    @Rule()
    def promocja1(self):
        if(self.getAmount("Cukier") >= 4):
            self.komunikatDiscount = f'{self.komunikatDiscount} 20% UPUST ZA MIN. 4 CUKRY: -{str("%.2f" % self.discountsSum("Cukier", 0.2))} zł\n'

    #Promocja2: Kup min. 2 mleka i zapłać 60% sumy za mleka
    @Rule()
    def promocja2(self):
        if(self.getAmount("Mleko") >= 2):
            self.komunikatDiscount = f'{self.komunikatDiscount} 60% UPUST ZA MIN. 2 MLEKA: -{str("%.2f" % self.discountsSum("Mleko", 0.6))} zł\n'

    #Promocja3: Na wszystkie makarony 30% zniżki
    @Rule()
    def promocja3(self):
        if(self.getAmount("Makaron") > 0):
            self.komunikatDiscount = f'{self.komunikatDiscount} 30% UPUST NA KAŻDY MAKARON: -{str("%.2f" % self.discountsSum("Makaron", 0.3))} zł\n'

    #4 Promocja: Kiełbaski grillowe 15% tańsze
    @Rule()
    def promocja4(self):
        if(self.getAmount("Kielbaska") > 0):
            self.komunikatDiscount = f'{self.komunikatDiscount} 15% UPUST NA KAŻDĄ KIEŁBASKĘ: -{str("%.2f" % self.discountsSum("Kielbaska", 0.15))} zł\n'

    #5 Promocja: Przy zakupie min 2 chlebów, 1 z nich dostajemy gratis
    @Rule()
    def promocja5(self):
        if(self.getAmount("Chleb") >= 2):
            self.komunikatDiscount = f'{self.komunikatDiscount} 1 CHLEB GRATIS: -{str("%.2f" % self.discountsGratis("Chleb", 1))} zł\n'

    #6 Promocja: Przy zakupie min 4 lodów, 1 dostajemy gratis
    @Rule()
    def promocja6(self):
        if(self.getAmount("Lody") >= 4):
            self.komunikatDiscount = f'{self.komunikatDiscount} 1 LÓD GRATIS: -{str("%.2f" % self.discountsGratis("Lody", 1))} zł\n'

    #7 Promocja: Przy zakupie 6-pak wody, drugi 6-pak 52% tańszy
    @Rule()
    def promocja7(self):
        if(self.getAmount("Woda6pak") >= 2):
            self.komunikatDiscount = f'{self.komunikatDiscount} 52% UPUST NA DRUGI 6PAK WODY: -{str("%.2f" % self.discountsMultiple("Woda6pak", 0.52, 2))} zł\n'

    #8 Promocja: Przy zakupie 4-pak piwa, trzeci 4-pak 56% tańszy
    @Rule()
    def promocja8(self):
        if(self.getAmount("Piwo4pak") >= 3):
            self.komunikatDiscount = f'{self.komunikatDiscount} 56% UPUST NA TRZECI 4PAK PIWA: -{str("%.2f" % self.discountsMultiple("Piwo4pak", 0.56, 3))} zł\n'


    #9 Promocja: Przy zakupie 2 opakowań ryżu i 1 sosu chińskiego, zniżka na zestaw 70% (suma 2 ryżow + 1 sos)
    @Rule()
    def promocja9(self):
        if(self.getAmount("Ryz") >= 2 and self.getAmount("SosChinski") >= 1):
            self.komunikatDiscount = f'{self.komunikatDiscount} 70% UPUST NA 2 RYZU + SOS: -{str("%.2f" % self.funkcja1("Ryz", 2, "SosChinski", 1))} zł\n'

    #10 Promocja: 1 piwko i 3 kielbaski to promocja (zrobić, że jak dobieramy kielbaski i piwo to nalicza się ta promka za kielbaski, a pozostałe z automatu się negują) np zmienną
    @Rule()
    def promocja10(self):
        pass
