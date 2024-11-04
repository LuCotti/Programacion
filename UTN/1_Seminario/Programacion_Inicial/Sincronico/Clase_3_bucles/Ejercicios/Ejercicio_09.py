# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

# Ejercicio 09
# Luciano Cotti

clave = '306'

ingreso = input('Ingrese la clave de usuario: ')

while ingreso != clave:
    ingreso = input('Clave incorrecta. Ingrésela nuevamente: ')