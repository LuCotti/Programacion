# 2. Escribe una función que calcule el área de un círculo. La función debe
# recibir el radio como parámetro y devolver el área.
PI = 3.14

def area_circulo(radio):
    area = PI * radio ** 2
    return area

print(area_circulo(9))