#
# cifra = 8
# output = ''
# while cifra != 0:
#     if cifra % 2 == 0 and cifra % 3 == 0:
#         output += 'ce '
#     if cifra % 2 == 0 and cifra <= 7:
#         output += 'delicios '
#         cifra = 1
#     if cifra % 2 == 1 and cifra < 5:
#         output += 'a fost '
#     if cifra % 2 == 0 and cifra < 5:
#         output += ' fifa'
#     cifra -= 1
# output += 'eclerul'
# print(output)


# lista = [12, 9, 5, 6, 14, 15]
# sum = 0
# for i in lista:
#     if lista[i] % 3 == 0:
#         sum = sum + lista[i]
# print(sum)

# given_string = 'murim CU pisoiul asta Rebel'
# new_str = ''
# for i in range(0, len(given_string)):
#     if given_string[i].isupper():
#         new_str += given_string[i]
# print(new_str)



# lista --> outputul sa fie cifra care apare de cele mai multe ori si de cate ori
# list = [1, 1, 2, 5, 7, 9, 7, 2, 2, 3, 2, 3, 3, 3]
# max_appearance = 0
# value_max_app = 0
# for i in list:
#     counter = 0
#     for num in list:
#         if num == i:
#             counter += 1
#     if counter > max_appearance:
#         max_appearance = counter
#         value_max_app = i
#     elif counter == max_appearance and i < value_max_app:
#         value_max_app = i
#
# print(f'Nr maxim de aparitii al lui {value_max_app} este {max_appearance}.')
#
# list = [1, 3, 6, 5, 7, 9, 7, 2, 6, 3, 6, 3, 6, 3]
# numar = 6
# # fara count
# counter = 0
# for num in list:
#     if num == numar:
#         counter += 1
# print(f'{numar} apare de {counter} ori.')


# count cu dictionar
# list = [1, 3, 6, 5, 7, 9, 7, 2, 6, 3, 6, 3, 6, 3]
# aparitii = {num: 0 for num in list}
# for i in list:
#         aparitii[i] += 1
# print(aparitii)
# val_ap_maxime = 0
# aparitii_max = 0
# for value in aparitii.keys():
#     if aparitii[value] > aparitii_max:
#         aparitii_max = aparitii[value]
#         val_ap_maxime = value
#     elif aparitii[value] == aparitii_max and value > val_ap_maxime:
#         val_ap_maxime = value
#
# print(f'{val_ap_maxime} apare de cele mai multe ori: {aparitii_max}')


# print(max(aparitii.values()))
# aparitii = {num:list.count(num) for num in list}
# print(aparitii.get(6))


# Take 2.
list = [1, 3, 6, 5, 7, 9, 7, 2, 6, 3, 6, 3, 6, 3]
val_ap_maxime = 0
aparitii_max = 0
aparitii = {num: 0 for num in list}
for i in list:
        aparitii[i] += 1
        if aparitii[i] > aparitii_max:
            aparitii_max = aparitii[i]
            val_ap_maxime = i
        elif aparitii[i] == aparitii_max and i > val_ap_maxime:
            val_ap_maxime = i
print(aparitii)

print(f'{val_ap_maxime} apare de cele mai multe ori: {aparitii_max}')
