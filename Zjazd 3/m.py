from datetime import date
import datetime


class Osoba:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.age = datetime.datetime.now().year - birth_year

    @property
    def informacje(self):
        return f"imie: {self.name}, nazwisko: {self.last_name}, wiek: {self.age}"


osoba = Osoba("Johny", "Bravo", 2000)

print(osoba.informacje)
print(osoba.age)


class Student:

    def __init__(self, imie, nazwisko, rok_urodzenia, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia
        self.kierunek = kierunek

