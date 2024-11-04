# Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).

# Ejercicio 07
# Luciano Cotti

edad = input('Ingrese su edad: ')
edad = int(edad)

if edad < 10:
    print('Usted es niño/a.')
elif edad >= 10 and edad <= 13:
    print('Usted es preadolescente.')
elif edad > 13 and edad <= 17:
    print('Usted es adolescente.')
else:
    print('Usted es mayor.')