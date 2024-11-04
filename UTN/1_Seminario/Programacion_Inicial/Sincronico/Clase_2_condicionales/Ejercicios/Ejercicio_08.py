# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

# Ejercicio 08
# Luciano Cotti

altura = input('Ingrese su altura [cm]: ')
altura = int(altura)

if altura < 160:
    print('Usted es base.')
elif altura >= 160 and altura < 180:
    print('Usted es escolta.')
elif altura >= 180 and altura < 200:
    print('Usted es Alero.')
elif altura >= 200:
    print('Usted es ala-pivot o pivot.')
else:
    print('Usted no debe estar aquí.')