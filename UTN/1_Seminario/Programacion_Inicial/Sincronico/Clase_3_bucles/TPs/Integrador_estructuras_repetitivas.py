# Integrador Estructuras Repetitivas

# Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:
# a. La suma acumulada de los números negativos.
# b. La suma acumulada de los números positivos.
# c. La cantidad de números negativos ingresados.
# d. El promedio de los números positivos.
# e. El número positivo más grande.
# f. El porcentaje de números negativos ingresados, respecto del total de ingresos.


# Luciano Cotti

# DEFINICIÓN DE VARIABLES
acumulador_positivos = 0
acumulador_negativos = 0
contador_positivos = 0
contador_negativos = 0
maximo = 0
contador_total = 0
continuar = True

# BUCLES Y CONDICIONES
while continuar == True:
    numero = float(input('Ingrese un número: '))
    while numero < -10000 or numero > 10000 or numero == 0:
        numero = float(input('El número debe estar comprendido entre -10000 y 10000, y debe ser distinto de 0: '))
    if numero >= 0:
        acumulador_positivos += numero
        contador_positivos += 1
        if numero > maximo:
            maximo = numero
    else:
        acumulador_negativos += numero
        contador_negativos += 1
    pregunta = input('¿Desea seguir ingresando números? ')
    if pregunta == 'no' or pregunta == 'NO' or pregunta == 'No':
        continuar = False
    contador_total += 1

# INFORME DE RESULTADOS
if contador_positivos > 0:
    promedio_positivos = acumulador_positivos / contador_positivos
    print('La suma de los positivos es',acumulador_positivos)
    print('El promedio de los números positivos es',promedio_positivos)
    print('El número positivo más grande es',maximo)
else:
    print('No se han ingresado números positivos.')

if contador_negativos > 0:
    porcentaje_negativos = contador_negativos * 100 / contador_total
    print('La suma de los negativos es',acumulador_negativos)
    print(f'Se han ingresado {contador_negativos} números negativos')
    print(f'Porcentaje de negativos: {porcentaje_negativos} %.')
else:
    print('No se han ingresado números negativos.')