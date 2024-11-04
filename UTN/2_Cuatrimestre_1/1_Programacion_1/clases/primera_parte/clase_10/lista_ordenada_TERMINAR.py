lista = [4, 7, 2, 78, 90, -1]
# Ordenar la lista
# lista_ordenada = [-1, 2, 4, 7, 78, 90]

# lista_ordenada = [0] * 6
# for i in range(len(lista)):
#     if i == 0:
#         lista_ordenada[i] = lista[i]
#     elif lista[i] < lista[i - 1]:
#         lista_ordenada[i - 1] = lista[i]
#     else:
#         lista_ordenada[i] = lista[i]

# print(lista_ordenada)
##############################################################################
lista_auxiliar = [9999] * len(lista)
lista_ordenada = [0] * len(lista)
minimo = 9999
posicion_minimo = 9999
for i in range(len(lista)):
    if i == 0:
        minimo = lista[i]
        posicion_minimo = i
        lista_auxiliar[i] = lista[i]
    elif lista[i] < minimo:
        minimo = lista[i]
        posicion_minimo = i
        lista_auxiliar[i] = lista[i]

print(lista_ordenada)


##############################################################################
