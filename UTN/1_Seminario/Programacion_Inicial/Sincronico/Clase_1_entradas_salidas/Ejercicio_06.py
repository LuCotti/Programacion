# Realizar un programa que pida dos números enteros. Calcular y mostrar el resto de la división entre ambos números. Ej: "El resto de dividir 7 por 2 es: 1" .
# Ejercicio 6
# Luciano Cotti

num1 = int(input('Ingrese el primer número entero: '))
num2 = int(input('Ingrese el segundo número entero: '))

resto = num1 % num2
mensaje = f'El resto de dividir {num1} por {num2} es: {resto}.'
print(mensaje)