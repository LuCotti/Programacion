'''
Dada una lista csv, imprimir solo los productos mayores a 50.
'''
file = open('productos.csv', 'r')
lista_productos = file.readlines()
lista_productos = lista_productos[1].split(',')
lista_mayores_50 = []

# for fila in lista_productos:
#     if type(fila[2]) == int:
#         if fila[2] > 50:
#             lista_mayores_50.append(fila)
# print(lista_mayores_50)
# print(lista_productos)
file.close()

print(lista_productos)