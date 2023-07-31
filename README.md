# Python-System-Ekspercki
Program ekspercki, który odzwierciedla generowanie rachunku na podstawie wybranych produktów w koszyku i naliczonych rabatów. Aplikacja przechowuje informacje na temat danego produktu (nazwa, cena, ilość). 

Wykorzystane technologie:
• Python (v3.8)
• Experta library (v1.9.4)
• PyQt (v5.15.6)

Założenia:
Założeniem programu jest możliwość zastosowania zaimplementowanych reguł
(rabatów) dla różnych układów produktów. Aplikacja wypisuje w formie rachunku informacje
o produkcie (nazwa, ilość, cena, suma) oraz informacje na temat wykorzystanych rabatów. Co
więcej pozwala na wygenerowanie dokumentu *.pdf z formą rachunku.

Interfejs graficzny użytkownika:
Graficzny interfejs użytkownika składa się po lewej stronie z listy, która przechowuje
produkty oraz cenę za sztukę. Po prawej stronie natomiast znajduje się lista, która pełni rolę
koszyka. Przesuwać produkty do koszyka możemy za pomocą specjalnego przycisku. Mamy
również możliwość usuwania produktów z koszyka oraz stosowania rabatów i obliczania ceny
końcowej. Interfejs jest bardzo intuicyjny i wyświetla tylko potrzebne informacje oraz
komunikaty. Po zastosowaniu i wyświetleniu podsumowania możemy wygenerować pdf za
pomocą widniejącego przycisku.

Literatura:
1. Dokumentacja biblioteki Experta pypi
https://pypi.org/project/experta/
2. Dokumentacja biblioteki Experta Read the docs
https://experta.readthedocs.io/en/stable/
3. Dokumentacja biblioteki Experta Open base
https://openbase.com/python/experta/documentation
