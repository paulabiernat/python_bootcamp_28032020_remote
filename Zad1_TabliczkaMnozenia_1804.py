
# napisz program wypisujacy na konsole tabliczke mnozenia dla liczb od 0 do 9 w postaci tabelki.


print("   ", end="")
for i in range(10):
    print(f"{i:4}",end="")
print()
print()

for i in range(10):
    print(i,end ="  ")
    for j in range(10):

        print(f"{i*j:4}", end="")

    print()

