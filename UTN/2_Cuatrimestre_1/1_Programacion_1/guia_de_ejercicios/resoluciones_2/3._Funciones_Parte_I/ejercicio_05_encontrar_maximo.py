'''5. Define una función que encuentre el máximo de tres números. La función debe
aceptar tres argumentos y devolver el número más grande.'''
def encontrar_maximo(numero_1:int, numero_2:int, numero_3:int)->int:
    maximo = numero_1
    if numero_2 > numero_1 and numero_2 > numero_3:
        maximo = numero_2
    elif numero_3 > numero_1 and numero_3 > numero_2:
        maximo = numero_3
    
    return maximo

print(encontrar_maximo(10, 0, 10))