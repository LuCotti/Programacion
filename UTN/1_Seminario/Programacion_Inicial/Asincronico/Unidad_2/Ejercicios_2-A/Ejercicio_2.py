# Crear un programa que pida al usuario un número y pueda calcular si es o no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso contrario “MENOR”.
numero = int(input('Ingrese un número: '))

if numero >= 18:
    print('MAYOR')
else:
    print('MENOR')