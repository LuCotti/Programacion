# Los argentinos nativos y por opción desde los dieciséis (16) años y los 
# argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. A partir del 
# ingreso de la edad del usuario y el estado (si es naturalizado o nativo), se deberá 
# informar si es o no posible que la persona concurra a votar en base a la información suministrada.

# Ejercicio 09
# Luciano Cotti

edad = input('Ingrese su edad: ')
edad = int(edad)
estado = input('¿Usted es argentino naturalizado o nativo (sin mayúsculas)? ')

match estado:
    case 'naturalizado':
        if edad >= 18:
            print('Usted puede votar.')
        else:
            print('Usted NO puede votar.')
    case 'nativo':
        if edad >= 16:
            print('Usted puede votar.')
        else:
            print('Usted NO puede votar.')
    case _:
        print('Los datos fueron mal ingresados.')