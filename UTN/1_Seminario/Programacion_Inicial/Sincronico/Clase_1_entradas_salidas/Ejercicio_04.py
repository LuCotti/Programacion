# Realizar un programa que permita el ingreso de dos números. Realizar la suma de los mismos y mostrar el resultado por pantalla con el siguiente formato: “La suma de los dos números
# es: ___”
# Ejercicio 4
# Luciano Cotti

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

suma = num1 + num2
mensaje = f'La suma de los dos números es: {suma}'

print(mensaje)