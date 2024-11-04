'''1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y
la altura y retorna el área.'''
def calcular_area_rectangulo(base:int, altura:int)->int:
    area = base * altura
    return area

print(calcular_area_rectangulo(5, 20))