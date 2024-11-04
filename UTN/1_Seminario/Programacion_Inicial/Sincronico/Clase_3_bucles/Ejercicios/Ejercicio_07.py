# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

# Ejercicio 07
# Luciano Cotti

acumulador_positivos = 0
producto_negativos = 1
continuar = True

while continuar == True:
    numero = float(input('Ingrese un número: '))
    if numero >= 0:
        acumulador_positivos += numero
    else:
        producto_negativos *= numero
    pregunta = input('¿Desea seguir ingresando números? ')
    if pregunta == 'no' or pregunta == 'NO' or pregunta == 'No':
        continuar = False

if acumulador_positivos != 0:
    print('La suma de los positivos es',acumulador_positivos)
else:
    print('No se han ingresado números positivos.')

if producto_negativos != 1:
    print('El producto de los negativos es',producto_negativos)
else:
    print('No se han ingresado números negativos.')