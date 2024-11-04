# A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.

# Ejercicio 04
# Luciano Cotti

altura = input('Ingrese su altura [m]: ')
altura = float(altura)

if altura > 1.8:
    print('Usted es pivot.')
else:
    print('Usted NO es pivot.')