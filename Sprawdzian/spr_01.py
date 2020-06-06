#zad 1 . listy, krotki, zbiory i słowniki
#Zad 2. listy, slowniki,
#Zad 3  Zaimplementuj funkcję realizującą algorytm sortowanie przez wybieranie:
lista = [9, 1, 6, 8, 4, 3, 2, 0]
for indeks_podstawienia in range(len(lista)):
    indeks_min_wartosci = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wartosci]:
            indeks_min_wartosci = indeks_ogona

    lista[indeks_podstawienia], lista[indeks_min_wartosci] = lista[indeks_min_wartosci], lista[indeks_podstawienia]
print(lista)
assert lista == [0, 1, 2, 3, 4, 6, 8, 9]

#zad4.

zrodla = {"a": 10, "b":30}

if "c" in zrodla:
    print(zrodla["c"])
else:
    print("brak")

#Zad5.

def foo(*args, **kwargs):
    print("Pozycyjnych: ", len(args))
    print("Kluczowych: ", len(kwargs))


foo(10, 20, a=1, b=2, c=3)


def power(a, b=2):
    licz = a ** b
    return licz


print(power(2, 3))
print(power(4))

