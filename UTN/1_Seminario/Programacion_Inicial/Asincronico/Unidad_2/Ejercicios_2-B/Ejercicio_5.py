# Crear un programa que solicite 5 números mediante input. Calcular la suma acumulada y el promedio de los números ingresados.
num1 = float(input('Ingresar el primer número: '))
num2 = float(input('Ingresar el segundo número: '))
num3 = float(input('Ingresar el tercer número: '))
num4 = float(input('Ingresar el carto número: '))
num5 = float(input('Ingresar el quinto número: '))

suma = num1 + num2 + num3 + num4 + num5
promedio = (num1 + num2 + num3 + num4 + num5) / 5

print('Suma de los números ingresados:',suma,'\nPromedio de los números ingresados:',promedio)