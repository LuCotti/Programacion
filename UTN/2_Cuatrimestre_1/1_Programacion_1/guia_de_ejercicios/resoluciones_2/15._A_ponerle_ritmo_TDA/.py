lista_1 = ['    manzana ', '    pera    ']
lista_2 = ['    banana  ', '    ananá   ']

lista_1.extend(lista_2)
lista_1[0].strip()
for i in range(len(lista_1)):
    lista_1[i] = lista_1[i].strip()
print(lista_1)
