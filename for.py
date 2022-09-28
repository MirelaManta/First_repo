# dalmatienii
# for i in range(1,102):
#     print(f'Dalmatianul cu nr {i}')

# dalmatienii din 2 in 2
# for i in range(1, 102, 2):
#     print(f'Dalmatianul cu nr {i}')

# parcurgere lista cu for prin intermediul indexului
numere  = [3, 7, 10, 20, 30]
# for i in range(0, len(numere)):
#     print(f'Indexul curent este {i}')
#     print(f'Nr curent este {numere[i]}')

# for each
# s = 0
# for numar in numere:
#     print(f'Nr curent este {numar}')
#     s = s + numar
# print(f'Suma este {numar}')

#tema - de cate ori apare 3 in [3, 2, 3, 5, 3]
# numere = [3, 2, 3, 5, 3]
# fuck = 0;
# for i in range(0, len(numere)):
#     if numere[i] == 3:
#         print(f'Am gasit unul')
#         fuck = fuck + 1
# print(f'Cifra 3 apare de {fuck} ori')

# am o lista de integers si vreau sa afisez produsul elementelor adiacente
numere = [1, 5, 7, 9, 2, 5]
produs_maxim = 0
for i in range(1, len(numere)):
    print('Produsul numerelor adiacente este ', {numere[i] * numere[i-1]})
    if (numere[i]*numere[i-1] > produs_maxim):
        produs_maxim = numere[i] * numere[i-1]
    else:
        print('Produsul maxim ramane', {produs_maxim})
print('Produsul maxim al elementelor adiacente este ', {produs_maxim})


