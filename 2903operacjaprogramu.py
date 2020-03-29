number_1 = int(input("Podaj pierwsza liczbe: "))
number_2 = int(input("Podaj druga liczbe: "))
operation = input("Podaj nazwe operacji : ")

if operation == "+" :
    print(f" Wynik {number_1 + number_2}")
elif operation == "-" :
    print(f" Wynik: {number_1 - number_2}")
elif operation == "/" :
    print(f" Wynik: {number_1 / number_2}")
elif operation == "%" :
    print(f" Wynik : {number_1 % number_2}")
else:
    print("niestey, operacja niemozliwa")
