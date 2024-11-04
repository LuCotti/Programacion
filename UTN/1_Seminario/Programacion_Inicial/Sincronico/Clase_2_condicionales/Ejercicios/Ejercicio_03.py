# A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.

# Ejercicio 03
# Luciano Cotti

edad = input('Ingrese su edad: ')
edad = int(edad)

if edad >= 18:
    print('UD ES MAYOR DE EDAD')
else:
    print('UD ES MENOR DE EDAD')

print('Sigue el flujo del programa normalmente.')