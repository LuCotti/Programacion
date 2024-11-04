'''10. Crear una función que le solicite al usuario el ingreso de un número
entero y lo retorne.'''

def numero(numero):
        if type(numero) != int:
                return print('No es entero')
        else:
                return print('Es entero')

numero(10)