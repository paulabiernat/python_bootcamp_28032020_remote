first_name = input("Podaj imie:")
last_name = input("Podaj nazwisko: ")
b_year = input("Podaj rok urodzenia: ")
profession = input("podaj zawod: ")
current_year = 2020

b_year = int(b_year)
age = current_year - b_year


result = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}
rok urodzenia : {b_year}
zawod: {profession.lower()}
emerytura mozliwa?
"""


print(result)
