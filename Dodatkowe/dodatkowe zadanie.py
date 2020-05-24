
#004
print(2 * 2)

#007 - samo 2 * 2
 # dodanie
print(2*2)
 # lub
x = 2
print(x*x)

#010
a = "Ala ma Asa"
b = a.upper()
c = a.lower()
print(b)
print(c)

#020
a = "Ala ma Asa"
a.upper()
print(a)

#030 - LISTA
a = [3, 5, 7]
print(a)

#040 - ODWROCENIE KOLEJNOSCI
a = [3, 5, 7]
a.reverse()
print(a)


#050
a = [3, 5, 7]
b = a.reverse()
print(b)

#060
a = ['ala', 'bartek', 'czarek']
b = ";".join(a)
print(b)

#070
b = ";".join(['ala', 'bartek', 'czarek'])
print(b)

#080
a = ['ala', 'bartek', 'czarek']
b = ";".join(a)
c = b.upper()
print(c)

#090
c = ";".join(['ala', 'bartek', 'czarek']).upper()
print(c)

#100
a = '.'.join(['a', 'b'])
b = a.join(['a', 'b'])
print(b)

#110
a = '.'.join(['a', 'b']).join(['a', 'b'])
print(a)

#120
a = [3, 5, 7]
print(a)

#130
a = [3, 5, 7]
b = ','.join([str(i) for i in a])
print(b)

#150
a = [range(i) for i in range(5)]
print(a)

#160
a = "Ala ma Asa"
print(len(a))

#170?



#180
a = {'imie': 'Adam', 'waga': 2}
b = {'imie': 'Bartek', 'waga': 3}
c = {'imie': 'Celina', 'waga': 4}
d = {'imie': 'Daniel', 'waga': 5}

osoby = [a, b, c, d]
s = 0
for o in osoby:
	s = s + o['waga']
print(s)

