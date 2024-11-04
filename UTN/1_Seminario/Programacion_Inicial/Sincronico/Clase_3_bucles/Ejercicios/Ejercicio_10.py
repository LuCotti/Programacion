# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

# Ejercicio 10
# Luciano Cotti

intento = 1
clave = '306'

ingreso = input('Ingrese la clave de usuario: ')

while ingreso != clave and intento < 3:
    intentos_restantes = 3 - intento
    print('Clave incorrecta (',intentos_restantes,'intentos restantes)')
    ingreso = input('Ingrésela nuevamente: ')
    intento += 1