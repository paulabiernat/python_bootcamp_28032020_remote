import json

"""
load - odczytywanie/deserializacja danych z pliku
dump - zapisywanie/serializacja danych do pliku
loads - odczyt danych z tekstu
dumps - zapisywanie/serializacja do tekstu

"""

text = '{"a":2, "b":4}'

dane = json.loads(text)

print(dane)
print(type(dane))

x ={i: i*3 for i in range(10)}
print(x, type(x))

print(json.dumps(x))

with open("dane.json") as fp:
    dane = json.load(fp)

print(dane)


x= [1,2,3,4]

with open("dane2.json", "w") as fp:
    json.dummp(x, fp)