'''2. Escribir una función parecida a la anterior, pero la misma deberá
calcular y devolver el promedio de los números positivos.'''


lista = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

def promedio_positivos(lista):
    suma = 0
    contador = 0
    for i in range(len(lista)):
        if lista[i] >= 0:
            suma += lista[i]
            contador += 1
    
    promedio = suma / contador
    return promedio

print(promedio_positivos(lista))