x = input("Podaj liczbe: ")

for y in x:
   cyfra =('0','1','2','3','4','5','6','7','8','9')
   if y in cyfra:
       slowo=("zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć")
       print(slowo[int(y)])