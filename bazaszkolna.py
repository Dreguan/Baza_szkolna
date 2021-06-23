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
        klasy[self.klasa].append(self)
    def wyswietl(self):
        for nauczyciel in nauczyciele_klas[self.klasa]:
            print(nauczyciel.przedmiot)
            print(nauczyciel.nazwa)


class Nauczyciel:
    def __init__(self):
        self.nazwa = input()
        self.przedmiot = input()
        self.klasy = []
        while True:
            klasa = input()
            if klasa == "":
                break
            self.klasy.append(klasa)
            if klasa not in nauczyciele_klas:
                nauczyciele_klas[klasa] = []
            nauczyciele_klas[klasa].append(self)
    def wyswietl(self):
        for klasa in self.klasy:
            if klasa in wychowawcy_klas:
                print(wychowawcy_klas[klasa].nazwa)


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


while True:
    rodzaj = input().strip()
    if rodzaj == "koniec":
        break
    if rodzaj == "nauczyciel":
        osoba = Nauczyciel()
    if rodzaj == "wychowawca":
        osoba = Wychowawca()
    if rodzaj == "uczen":
        osoba = Uczen()
    if osoba.nazwa not in osoby:
        osoby[osoba.nazwa] = []
    osoby[osoba.nazwa].append(osoba)

if sys.argv[1] in osoby:
    for osoba in osoby[sys.argv[1]]:
        osoba.wyswietl()

if sys.argv[1] in wychowawcy_klas:
    print("Wychowawca: {}".format(wychowawcy_klas[sys.argv[1]].nazwa))
    for osoba in klasy[sys.argv[1]]:
        print(osoba.nazwa)

