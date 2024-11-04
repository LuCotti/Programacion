'''10.Ingresar un número. Determinar si el número es primo o no.'''

numero = int(input('Ingrese un número: '))
contador_divisores = 0

for i in range(2, numero):
    resto = numero % i
    if resto == 0:
        contador_divisores += 1

if numero < 2:
    print('No es primo.')
elif contador_divisores > 0:
    print('No es primo.')
else:
    print('Es primo.')