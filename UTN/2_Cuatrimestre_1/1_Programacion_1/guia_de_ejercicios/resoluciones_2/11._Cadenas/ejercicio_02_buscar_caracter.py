'''
2) Crear una función que reciba una cadena y un caracter. La función deberá
devolver el índice en el que se encuentre la primera ocurrencia de dicho
caracter, o -1 en caso de que no esté.
'''

def buscar_caracter(cadena: str, caracter: str) -> int:
    posicion_caracter = -1
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            posicion_caracter = i
    
    return posicion_caracter

# Test
print(buscar_caracter('cadena', 'g'))
