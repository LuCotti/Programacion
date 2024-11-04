# Ejercicio 5
# Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y
# división), tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y
# operador_b), transformarlos en números enteros, realizar dicha operación y luego mostrar el
# resultado de la misma utilizando print.
# Ej: "El resultado de la …… es: 755"

# Luciano Cotti

# INGRESO DE DATOS
operador_a = int(input('Ingrese el primer número entero: '))
operador_b = int(input('Ingrese el segundo número entero: '))

# CÁLCULOS
suma = operador_a + operador_b
resta = operador_a - operador_b
multiplicacion = operador_a * operador_b
division = operador_a / operador_b

# MUESTRA DE RESULTADOS
print('La suma de los números ingresados es igual a',suma)
print('La resta de los números ingresados es igual a',resta)
print('La multiplicación de los números ingresados es igual a',multiplicacion)
print('La división de los números ingresados es igual a',division)