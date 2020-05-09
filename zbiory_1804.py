

zbior = set()
print(zbior)

zbior.add(1)
zbior.add("x")
print(zbior)


for element in zbior:
    print(element)

print(dir(zbior))

a = {1,2,3,4,5,6}
b = {2,3,4,5,6,7}

print(a | b)
print(a & b)
print(a-b)
print(a^b)
print(a.pop())
print(a)