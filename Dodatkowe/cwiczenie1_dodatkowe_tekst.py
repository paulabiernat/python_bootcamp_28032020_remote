## HELLO STRANGER!

napis = input("podaj napis: ")

x = napis[::2]
y = napis[1:3]+napis[7::2]
space1 = " ".join(x)
space2 = " ".join(y)
print(space1)
print(space2)


#HELLO STRANGER!

print(f" {napis[0]} {napis[2]} {napis[4]} {napis[6]} {napis[8]} {napis[10]} {napis[12]} {napis[14]}")
print(f" {napis[1]} {napis[3]} {napis[7]} {napis[9]} {napis[11]} {napis[13]}")

