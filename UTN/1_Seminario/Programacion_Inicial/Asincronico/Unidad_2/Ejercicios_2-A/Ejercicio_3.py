# Crear un programa que a partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.
altura = float(input('Ingrese su altura [m]: '))

if altura > 1.8:
    print('Usted puede ser pivot.')
else:
    print('Dedíquese al ping pong.')