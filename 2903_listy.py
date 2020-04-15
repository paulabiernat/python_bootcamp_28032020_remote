elementy = [1, 2, 3, 4, "xx", 2.0, 2]

print(type(elementy))
print(list())
print(dir(elementy))

## mutowalne sa listy tzn, ze mozna ja modyfikowac

x = elementy.append("cos")
print(elementy)
print(x)
print(len(elementy))

while len(elementy) < 11:
    elementy.append("xx")
    print(elementy)


print(sum([1, 2, 3, 4, 6])
