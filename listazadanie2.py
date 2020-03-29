dane = [1, 2, 3, 4, -10,-40]

liczb_dod = 0
liczba_uj = 0
for element in dane :
    if element >0:
        liczb_dod = liczb_dod + 1
    else:
        liczba_uj = liczba_uj + 1

print("ile dodatnich: ", liczb_dod)
print("ile uje: ", liczba_uj)
