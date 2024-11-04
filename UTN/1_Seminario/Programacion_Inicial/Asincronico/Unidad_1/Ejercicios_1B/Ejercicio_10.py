# Cree un programa en el cual pida al usuario el nombre y la edad y muestre por consola la edad que tentrá dentro de 10 años.
nombre = input('Escriba su nombre: ')
edad = int(input('Escriba su edad: '))

edad_futura = edad + 10

print(nombre,', dentro de 10 años tendrás ',edad_futura, ' años.', sep='')