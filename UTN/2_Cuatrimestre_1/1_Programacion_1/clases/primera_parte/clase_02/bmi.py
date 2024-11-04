peso = float(input('Ingrese su peso [kg]: '))
while peso < 0:
    peso = float(input('No se pueden ingresar datos negativos. Ingrese su peso nuevamente [kg]: '))
altura = float(input('No se pueden ingresar datos negativos. Ingrese su altura [cm]: '))
while altura < 0:
    altura = float(input('No se pueden ingresar datos negativos. Ingrese su altura [cm]: '))

imc = peso / altura ** 2

mensaje = f'Su Índice de Masa Corporal es igual a {imc}.'

print(mensaje)