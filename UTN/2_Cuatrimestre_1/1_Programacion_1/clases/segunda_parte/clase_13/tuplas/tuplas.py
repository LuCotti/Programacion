lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
print(type(lista))
print(type(tupla))
##############################################################################
tupla_2 = tuple(lista)
print(tupla_2)

##############################################################################
mi_tupla = (10, 20, 30, 40, 50, 20)
print(mi_tupla[1]) # Acceso por índice
print(mi_tupla[1:4]) # Slicing de la tupla

##############################################################################
# Operaciones con tuplas
print(mi_tupla.count(20))
print(mi_tupla.index(40))
print(mi_tupla * 2)
##############################################################################
# Funciones con tuplas
def calcular_area_y_perimetro(rectangulo: tuple) -> int: # CORREGIR FUNCIÓN
    largo, ancho = rectangulo
    return (largo * ancho, 2 * (largo + ancho))

area, perimetro = calcular_area_y_perimetro((5, 10))
print(calcular_area_y_perimetro((5, 10)))
print(f'Area: {area}')
print(f'Perímetro: {perimetro}')