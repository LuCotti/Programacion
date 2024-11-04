'''5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado.'''
lista = [132, -4, 132, 3, 15, 132]
def posiciones_maximo(lista: list)-> list:
    posiciones_maximo = []
    valor_maximo = 0
    for i in range(len(lista)):
        if i == 0:
            posiciones_maximo += [i]
            valor_maximo = lista[i]
        elif lista[i] >= valor_maximo:
            posiciones_maximo += [i]
            valor_maximo = lista[i]
    return posiciones_maximo

print(posiciones_maximo(lista))