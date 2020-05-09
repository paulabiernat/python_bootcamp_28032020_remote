
# Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika wagi i nazwy produktu. Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie.

produkty = {
    "marchew": 2.00,
    "ziemniaki": 3.00,
    "buraki": 4.00,
    "pietruszka": 1.50,
    "pomidor": 4.50,
}

magazyn = {
    "marchew": 10,
    "ziemniaki": 10,
    "buraki": 10,
    "pietruszka": 10,
    "pomidor": 10,
}

while True:
    komenda = input(" Co chcesz kupic? [k-kup] [z-zakoncz] [m-magazyn] ")

    if komenda == "z":
        break
    elif komenda == "k":
        print(" Nasz zielnik oferuje: ")
        for nazwa, cena in produkty.items():
             print(f" - {nazwa} w cenie: {cena} PLN (stan: {magazyn[nazwa]}")

        zakup = input("Co chcesz kupic: ")

        if zakup in produkty:
            ile = input(f"ile chcesz kupic [{zakup}]? ")
            ile = float(ile)
            if ile < magazyn[zakup]:
                print(f"Za {ile} kg {zakup} zaplaczisz {ile * produkty[zakup]:.2f}")
                magazyn[zakup] = magazyn[zakup] - ile
            else:
                print("nie mamy tyle produktow")
    elif komenda == "m":
        produkt = input(f" Jaki nowy produkt chcialbys kupic? ")
        ile = int(input(f"ile dodajemy [{produkt}] ? "))
        magazyn[produkt] = magazyn.get(produkt,0) + ile
        if produkt not in produkty:
            cena = float(input(f"jaka cena za [{produkt}]"))
            produkty[produkt] = cena





