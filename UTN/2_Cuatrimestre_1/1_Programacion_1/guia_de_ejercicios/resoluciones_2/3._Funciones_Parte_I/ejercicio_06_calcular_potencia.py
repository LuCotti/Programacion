'''6. Diseña una función que calcule la potencia de un número. La función debe recibir la
base y el exponente como argumentos y devolver el resultado.'''
def calcular_potencia(base:int, exponente:int)->int:
    resultado = base ** exponente
    return resultado

print(calcular_potencia(3, 1))
print(calcular_potencia(3, 2))
print(calcular_potencia(3, 3))
print(calcular_potencia(3, 4))
print(calcular_potencia(3, 5))