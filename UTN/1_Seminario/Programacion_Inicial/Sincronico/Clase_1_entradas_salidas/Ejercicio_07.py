# Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.
# Ejercicio 7
# Luciano Cotti

sueldo = float(input('Ingrese el sueldo: '))
incremento = sueldo * 1.15

mensaje = f'Su sueldo +15% es igual a {incremento}.'
print(mensaje)