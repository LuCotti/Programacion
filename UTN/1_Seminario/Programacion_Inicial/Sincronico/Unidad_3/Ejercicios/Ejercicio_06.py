# Ejercicio 6
# Tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y
# operador_b), transformarlos en números enteros, realizar la operación que nos permita
# obtener el resto de una división y luego mostrar el resultado de la misma utilizando print.
# Ej: "El resto de dividir 7 por 2 es: 1"

# Luciano Cotti

operador_a = int(input('Ingrese el primer número entero: '))
operador_b = int(input('Ingrese el segundo número entero: '))

resto = operador_a % operador_b

print('El resto de la división es igual a',resto)