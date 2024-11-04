'''2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos.'''
lista = [-2, -1, 0, 1, 2]
def calcular_promedio(lista: list)-> int:
    contador = 0
    acumulador = 0
    
    for i in range(len(lista)):
        if lista[i] >= 0:
            contador += 1
            acumulador += lista[i]
    
    promedio = acumulador / contador
    return promedio

print(calcular_promedio(lista))