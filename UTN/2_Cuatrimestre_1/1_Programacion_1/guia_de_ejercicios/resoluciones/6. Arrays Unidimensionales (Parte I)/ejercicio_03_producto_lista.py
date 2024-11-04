'''3. Escribir una función que calcule y retorne el producto de todos los
elementos de la lista que recibe como parámetro.'''

lista = [2, 4, 3, 5]

def promedio_positivos(lista):
    acumulador = 1
    for i in range(len(lista)):
        acumulador *= lista[i]
    
    return acumulador

print(promedio_positivos(lista))