'''1. Escribir una función que reciba una lista de enteros, la misma calculará
y devolverá el promedio de todos los números.'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def promedio(lista):
    suma = 0
    contador = 0
    for i in range(len(lista)):
        suma += lista[i]
        contador += 1
    
    promedio = suma / contador
    return promedio

print(promedio(lista))