
# ax2+ bx + c = 0

a = int(input("podaj liczbe: "))
b = int(input("podaj liczbe 2: "))
c = int(input("podaj liczbe 3: "))
x = 9

delta = (b**2) - 4*a*c

print(f'delta wynosi: {delta}')

if delta < 0:
   print("rownanie nie jest kwadratowe")
elif delta > 0:
   x_1 = (-(b + (delta)** 0.5))
   x_2 =  2 * a
   y_1 = (-b + delta** 0.5)
   y_2 = 2*a
   print(f" X_1 = {x_1 / x_2}")
   print(f" x_2 = {y_1/y_2}")
elif delta == 0:
    x_0 = (-b) / (2 * a)
    print(x_0)



