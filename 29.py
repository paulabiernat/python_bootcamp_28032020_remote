chleb = float(input("ile chcesz kupic chleba:"))
sok = float(input("ile chcesz kupic soku: "))
paczki = float(input("ile chcesz paczkow: "))
x = chleb * 6.50
y = sok * 4.00
z = paczki* 5.50

print("Twoje zamowienie to: ")

print(f" 1. Chlebow {chleb} szt za {x} zł")
print(f" 2. Sokow {sok}  zt za {y} zł")
print(f" 2. Paczkow {paczki} szt za {z} zł")

suma = x + y + z

print(f" Calkowity koszt Twoich zakupow: {suma} zł")

