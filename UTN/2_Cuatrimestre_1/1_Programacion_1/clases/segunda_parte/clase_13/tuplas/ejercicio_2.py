'''
Ejercicio 2: crear una función que reciba una tupla de dos valores y devuelva
el cociente y residuo de la división de ambos números.
'''
tupla = (10, 3)
def calcular_cociente_y_residuo(tupla: tuple) -> int:
    cociente = tupla[0] // tupla[1]
    residuo = tupla[0] % tupla[1]
    return cociente, residuo

# Test
print(calcular_cociente_y_residuo(tupla))
