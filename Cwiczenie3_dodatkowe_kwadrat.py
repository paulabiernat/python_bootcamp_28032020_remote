
x = int(input("podaj liczbe: "))

z =int(x/x)

print(x * "*")
for i in range (2,x):
    print(f'{z * "*"}{" " * (x-2)}{z * "*"}')
print(x * "*")

