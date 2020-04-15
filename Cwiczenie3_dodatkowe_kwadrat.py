
x = int(input("podaj liczbe: "))

print(x * "*")
for i in range (2,x):
    print(f'*{" " * (x-2)}*')
print(x * "*")
