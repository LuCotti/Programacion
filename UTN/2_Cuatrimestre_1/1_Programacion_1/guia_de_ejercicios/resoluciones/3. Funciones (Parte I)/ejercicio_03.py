# 3. Crea una función que verifique si un número dado es par o impar. La
# función debe imprimir un mensaje indicando si el número es par o impar.

def emparejar(numero):
    resto = numero % 2
    if resto == 0:
        print('El número es par.')
    else:
        print('El número es impar.')

emparejar(4)