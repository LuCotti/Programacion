# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.

# Ejercicio 05
# Luciano Cotti
contador = 0
acumulador = 0


while contador < 5:
    numero = float(input('Ingrese un número: '))
    acumulador += numero
    contador += 1
promedio = acumulador / contador

print('La suma de los números es',acumulador,'\nEl promedio de los números es',promedio)