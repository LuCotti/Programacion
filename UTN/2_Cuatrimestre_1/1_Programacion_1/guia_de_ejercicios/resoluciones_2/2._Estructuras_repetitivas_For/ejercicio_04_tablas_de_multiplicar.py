'''4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5:

5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15...
'''
numero_ingresado = int(input('Ingrese un número: '))
for i in range(11):
    resultado = numero_ingresado * i
    print(f'{numero_ingresado} x {i} = {resultado}')