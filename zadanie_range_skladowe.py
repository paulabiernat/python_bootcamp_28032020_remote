{1,2,3}

print([[el, el**3] for el in range(-10,10)])

#1
print([x/10 for x in range(11)])
#2
print({(x, x**2, x**3) for x in range (-10,11)})
#3
napisy = {"xxx", "yyyyy", "xx", "xxxxxxxxxdhddhdhd"}
print({napis:len(napis) for napis in napisy})



