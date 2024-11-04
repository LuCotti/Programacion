'''9. Crear una función que imprima la tabla de multiplicar de un número recibido como
parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
el rango de multiplicación. Por defecto es del 1 al 10.'''
def tabla_de_multiplicar(numero, inicio=1, fin=10):
    for i in range(inicio, fin + 1):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')


tabla_de_multiplicar(2, 3, 7)