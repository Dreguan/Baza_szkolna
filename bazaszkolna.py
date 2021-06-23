import sys

osoby = {}
klasy = {}
wychowawcy_klas = {}
nauczyciele_klas = {}

class Uczen:
    def __init__(self):
        self.nazwa = input()
        self.klasa =input()
        if self.klasa not in klasy:
            klasy[self.klasa] = []
        klasy[self.klasa].append(self) #self to obiekt klasy uczeń
    def wyswietl(self):
        for nauczyciel in nauczyciele_klas[self.klasa]:
            print(nauczyciel.przedmiot)
            print(nauczyciel.nazwa)
        #print("Uczeń: {} - Klasa: {}.".format(self.nazwa, self.klasa))


class Nauczyciel:
    def __init__(self):
        self.nazwa = input()
        self.przedmiot = input()
        self.klasy = []
        while True:
            klasa = input()
            if klasa == "": #tak samo zadziała if not klasa
                break
            self.klasy.append(klasa)
            if klasa not in nauczyciele_klas:
                nauczyciele_klas[klasa] = []
            nauczyciele_klas[klasa].append(self)
    def wyswietl(self):
        for klasa in self.klasy:
            if klasa in wychowawcy_klas:
                print(wychowawcy_klas[klasa].nazwa)
        #print("Nauczyciel: {} - Przedmiot: {} -  Klasy: {}.".format(self.nazwa, self.przedmiot, self.klasy))


class Wychowawca:
    def __init__(self):
        self.nazwa = input()
        self.klasy = []
        while True:
            klasa = input()
            if klasa == "":
                break
            self.klasy.append(klasa)
            wychowawcy_klas[klasa] = self
    def wyswietl(self):
        for klasa in self.klasy:
            for osoba in klasy[klasa]:
                print(osoba.nazwa)
        #print("Wychowawca: {} -  Klasy: {}.".format(self.nazwa, self.klasy))


while True:
    rodzaj = input().strip()
    if rodzaj == "koniec":
        break
    if rodzaj == "nauczyciel":
        osoba = Nauczyciel() #tworzy nowy obiekt klasy Nauczyciel
    if rodzaj == "wychowawca":
        osoba = Wychowawca()
    if rodzaj == "uczen":
        osoba = Uczen()
    #osoba.wyswietl()
    if osoba.nazwa not in osoby:
        osoby[osoba.nazwa] = []
    osoby[osoba.nazwa].append(osoba)
    #osoby[osoba.nazwa] = osoba #z obiektu osoba wyciągnęliśmy nazwę

for nazwa, osoba in osoby.items(): #items dostaje się jednocześnie i do klucza i do wartości
    print(nazwa)
#    print(osoba.__dict__) #przekształca dany obiekt w słownik dzięki czemu widzimy co rzeczywiście siedzi wewątrz obiektu

#print(osoby)
print(klasy.items())

if sys.argv[1] in osoby:
    for osoba in osoby[sys.argv[1]]:
        osoba.wyswietl()

if sys.argv[1] in wychowawcy_klas:
    print("Wychowawca: {}".format(wychowawcy_klas[sys.argv[1]].nazwa))
    for osoba in klasy[sys.argv[1]]:
        print(osoba.nazwa)

