'''10.Ingresar un número. Determinar si el número es primo o no.'''
contador_divisores = 0

numero_ingresado = int(input('Ingrese un número: '))
for i in range(1, numero_ingresado + 1):
    if numero_ingresado % i == 0:
        contador_divisores += 1

if contador_divisores == 2:
    print('El número es primo.')
else:
    print('El número no es primo.')