# Pedirle al usuario su edad, determinar si el usuario NO es adolescente.

# Ejercicio 06
# Luciano Cotti

edad = input('Ingrese su edad: ')
edad = int(edad)

if edad < 13 or edad > 17:
    print('Usted NO es adolescente.')

print('Sigue el flujo del programa normalmente.')