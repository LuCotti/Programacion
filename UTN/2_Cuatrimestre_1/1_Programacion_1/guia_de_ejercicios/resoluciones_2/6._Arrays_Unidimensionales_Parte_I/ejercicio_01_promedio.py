'''1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números.'''
lista = [.5, .6, .7]
def calcular_promedio(lista: list)-> int:
    contador = 0
    acumulador = 0
    
    for i in range(len(lista)):
        contador += 1
        acumulador += lista[i]
    
    promedio = acumulador / contador
    return promedio

print(calcular_promedio(lista))