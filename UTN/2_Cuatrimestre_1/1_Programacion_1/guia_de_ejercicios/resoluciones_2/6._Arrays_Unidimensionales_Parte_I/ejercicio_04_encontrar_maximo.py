'''4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.'''
lista = [132, -4, 0, 3, 15]
def posicion_maximo(lista: list)-> int:
    posicion_maximo = 0
    valor_maximo = 0
    for i in range(len(lista)):
        if i == 0:
            posicion_maximo = i
            valor_maximo = lista[i]
        elif lista[i] > valor_maximo:
            posicion_maximo = i
            valor_maximo = lista[i]
    return posicion_maximo

print(posicion_maximo(lista))