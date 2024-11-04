'''5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado.'''

lista = [-2, 16, 9, 1, 16, -8]
def posicion_maximo(lista):
    maximo = None
    posicion_maximo = []
    for i in range(len(lista)):
        if i == 0:
            maximo = lista[i]
            posicion_maximo.append(i)
        elif lista[i] > maximo:
            maximo = lista[i]
            posicion_maximo = []
            posicion_maximo.append(i)
        elif lista[i] == maximo:
            maximo = lista[i]
            posicion_maximo.append(i)
    
    return posicion_maximo

print(posicion_maximo(lista))

# CORREGIR SIN USAR APPEND