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