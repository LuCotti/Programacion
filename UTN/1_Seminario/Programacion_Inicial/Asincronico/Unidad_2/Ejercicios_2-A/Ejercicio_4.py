# Crear un programa que se ingrese la edad del usuario en número y pueda calcular si es adolescente (edad entre 13 y 17 años).
edad = int(input('Ingrese su edad: '))

if edad >= 13 and edad <= 17:
    print('Usted es un adolescente.')
elif edad < 13:
    print('Usted es un niño.')
else:
    print('Usted es un adulto.')