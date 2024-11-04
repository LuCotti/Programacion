# Crear un programa que solicite al usuario que ingrese un número. Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.
numero = int(input('Ingrese un número del 0 al 9: '))
while numero < 0 or numero > 9:
    numero = int(input('DIJE DEL 0 AL 9: '))
print('Podés seguir con tu vida.')