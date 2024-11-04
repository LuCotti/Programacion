# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

# Ejercicio 06
# Luciano Cotti

contador = 0
acumulador = 0
continuar = True

while continuar == True:
    numero = float(input('Ingrese un número: '))
    contador += 1
    acumulador += numero
    pregunta = input('¿Desea seguir ingresando números? ')
    if pregunta == 'no' or pregunta == 'NO' or pregunta == 'No':
        continuar = False

promedio = acumulador / contador

print('La suma de los números es',acumulador,'\nEl promedio de los números es',promedio)