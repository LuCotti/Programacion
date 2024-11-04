# Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.
# Ejercicio 8
# Luciano Cotti

sueldo = float(input('Ingrese su sueldo: '))
porcentaje = float(input('Ingrese el porcentaje de aumento: '))

resultado = sueldo * (porcentaje / 100 + 1)
mensaje = f'El sueldo aumentado es: {resultado}.'

print(mensaje)