import datetime

rocznik = int(input("Podaj rok urodzenia: "))
current_year = datetime.datetime.now().year

wiek = rocznik - current_year
if wiek >= 18:
    print("jestes pelnoletni!")
else:
    print("nie jestes pelnoletni gowniarzu, piwa nie bedzie")