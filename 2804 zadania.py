first_name = "JAN"
last_name = "KoWalski"
b_year = 1950
profession = "Hydraulik"

result = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}
rok urodzenia : {b_year}
zawod: {profession.lower()}

"""

expected = """
imie i nazwisko: Jan Kowalski
rok urodzenia : 1950
zawod: hydraulik

"""

assert result == expected
print(result)

