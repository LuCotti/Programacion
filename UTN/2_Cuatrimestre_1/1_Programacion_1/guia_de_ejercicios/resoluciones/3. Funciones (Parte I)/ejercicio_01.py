# 1. Escribir una función que calcule el área de un rectángulo. La función
# recibe la base y la altura y retorna el área.

def area_rectangulo(base, altura):
    area = base * altura / 2
    return area

print(area_rectangulo(4, 7))