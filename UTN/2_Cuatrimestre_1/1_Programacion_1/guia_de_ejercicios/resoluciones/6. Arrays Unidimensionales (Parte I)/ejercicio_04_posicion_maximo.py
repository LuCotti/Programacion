'''4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.'''

lista = [16, -2, 9, 1, 4, -8]
def posicion_maximo(lista):
    maximo = None
    posicion_maximo = None
    for i in range(len(lista)):
        if i == 0:
            maximo = lista[i]
            posicion_maximo = i
        elif lista[i] > maximo:
            maximo = lista[i]
            posicion_maximo = i
    
    return posicion_maximo

print(posicion_maximo(lista))