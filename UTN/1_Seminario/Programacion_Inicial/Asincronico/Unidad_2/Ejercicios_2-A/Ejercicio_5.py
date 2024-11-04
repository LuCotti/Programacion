# Crear un programa que al ingresar un número puede calcular si es mayor, niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad.
edad = int(input('Ingrese su edad: '))

if edad < 10:
    print('Usted es niño/a.')
elif edad >= 10 and edad < 13:
    print('Usted es preadolescente.')
elif edad >= 13 and edad <= 17:
    print('Usted es adolescente.')
else:
    print('Usted es mayor.')