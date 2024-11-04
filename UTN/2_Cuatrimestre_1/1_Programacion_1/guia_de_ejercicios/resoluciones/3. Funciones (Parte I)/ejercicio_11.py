'''11. Crear una función que le solicite al usuario el ingreso de un número
flotante y lo retorne.'''

def numero(numero):
        if type(numero) != float:
                return print('No es flotante')
        else:
                return print('Es flotante')

numero(10.3)