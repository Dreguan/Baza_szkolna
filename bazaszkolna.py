import sys

osoby = {}
klasy = {}


class Uczen:
    def __init__(self):
        self.nazwa = input()
        self.klasa =input()


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


class Wychowawca:
    def __init__(self):
        self.nazwa = input()
        self.klasy = []
        while True:
            klasa = input()
            if klasa == "":
                break
            self.klasy.append(klasa)


while True:
    rodzaj = input()
    if rodzaj == "koniec":
        break
    if rodzaj == "nauczyciel":
        osoba = Nauczyciel() #tworzy nowy obiekt klasy Nauczyciel
    if rodzaj == "wychowawca":
        osoba = Wychowawca()
    if rodzaj == "uczen":
        osoba = Uczen()
    osoby[osoba.nazwa] = osoba #z obiektu osoba wyciągnęliśmy nazwę

for nazwa, osoba in osoby.items(): #items dostaje się jednocześnie i do klucza i do wartości
    print(nazwa)
    print(osoba.__dict__) #przekształca dany obiekt w słownik
