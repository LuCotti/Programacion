'''9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados.'''
cantidad_de_divisores = 0
numero_ingresado = int(input('Ingrese un número: '))
if numero_ingresado < 0: # Consideramos los números negativos
    numero_ingresado *= -1

for i in range(1, numero_ingresado + 1):
    if numero_ingresado % i == 0:
        if cantidad_de_divisores == 0:
            print('Se encontraron los siguientes divisores:')
        cantidad_de_divisores += 1
        print(i)

print(f'Cantidad de divisores: {cantidad_de_divisores}')