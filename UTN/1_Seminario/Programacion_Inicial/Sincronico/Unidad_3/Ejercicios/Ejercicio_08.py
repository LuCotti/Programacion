# Ejercicio 8
# Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),
# transformarlos en números enteros y mostrar el importe de sueldo actualizado con el
# incremento porcentual utilizando print.

# Luciano Cotti

sueldo = int(input('Ingrese su sueldo: '))
incremento = int(input('Ingrese el incremento: %'))

sueldo_incrementado = sueldo * (1 + (incremento / 100))

print('Su sueldo incrementado es igual a',sueldo_incrementado)