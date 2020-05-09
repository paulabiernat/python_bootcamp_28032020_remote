zbior = set()


while True:
    polecenie = input("wpisz liczbe lub k by zakonczyc: " )
    if polecenie == "k":
        break
    zbior.add(int(polecenie))

liczby_parzyste = set(range(0,101,2))

print(f" unikalne liczby:{len(zbior)}")
print(f" Przystych z zakresu 1-100: {len(zbior & liczby_parzyste)}")



elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]

elementy_2 = {"aaa", "aba",  "ccc"}

elementy = set(elementy)

print(f"liczba unikalnych elementow to: {len(elementy)}")
print(f"wspolna czesc tych zbiorow to: {elementy & elementy_2 }")


