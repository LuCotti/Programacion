# Crear un programa que pueda sumar los números pares comprendidos entre el 1 y el 10.
sumador = 0

numero = int(input('Ingresar un número par entre 1 y 10 (0 para detener): '))

while numero != 0:
    if numero >= 1 and numero <= 10 and numero % 2 == 0:
        sumador += numero
        print('Suma:',sumador)
        numero = int(input('Ingresar un número par entre 1 y 10 (0 para detener): '))
    else:
        print('No sumaste nada, capo. Seguimos en',sumador)
        numero = int(input('Ingresar un número par entre 1 y 10 (0 para detener): '))