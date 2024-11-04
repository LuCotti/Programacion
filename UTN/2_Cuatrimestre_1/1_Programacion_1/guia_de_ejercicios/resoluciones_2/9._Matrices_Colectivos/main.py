################################## CONSIGNA ##################################
'''
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total
tiene 15 choferes (cada uno con un legajo distinto generado
aleatoriamente).

Nos piden desarrollar un software que presente el siguiente menú de
usuarios:

Menú:

1. Cargar planilla. El chofer se debe identificar (el legajo debe existir
dentro de una matriz de legajos). Si el chofer existe cargará la
recaudación del viaje indicando línea y coche (no necesariamente
un chofer está asignado a una única línea y coche), estos datos
deben estar validados. Un chofer puede cargar más de una
recaudación por día (para distintas líneas y distintos coches). Cada
coche de cada línea puede tener varias recaudaciones diarias.
2. Mostrar la recaudación de cada coche y línea (mostrar la matriz).
3. Calcular y mostrar recaudación por línea.
4. Calcular y mostrar recaudación por coche.
5. Calcular y mostrar la recaudación total.
6. Salir.

Todo el desarrollo tiene que estar modularizado: ingreso de datos,
validaciones de líneas y coches, generación y verificación de existencia
de legajo, cálculos, etc.
'''
################################# RESOLUCIÓN #################################
# import
menu = '''1. Cargar planilla.
2. Mostrar la recaudación de cada coche y línea.
3. Calcular y mostrar recaudación por línea.
4. Calcular y mostrar recaudación por coche.
5. Calcular y mostrar la recaudación total.
6. Salir.'''

# Creamos una lista de legajos con 15 elementos.
lista_legajos = [0] * 15
seguir = 'S'

# Creamos la matriz de recaudaciones
matriz_recaudaciones = [[0] * 5] * 3

while seguir == 'S':
    print(menu)
    opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
    
    match opcion_ingresada:
        case 1:
            pass
        case 1:
            pass
        case 1:
            pass
        case 1:
            pass
        case 1:
            pass
        case 1:
            pass

