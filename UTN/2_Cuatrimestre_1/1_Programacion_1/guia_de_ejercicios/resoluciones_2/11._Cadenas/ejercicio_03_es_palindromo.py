'''
3) Crear una función que reciba como parámetro una cadena y determine si la
misma es o no un palíndromo. Deberá retornar un valor booleano indicando
lo sucedido.
'''

def es_palindromo(cadena: str) -> bool:
    cadena_izq_der = ''
    for i in range(len(cadena)):
        cadena_izq_der += cadena[i]
    #print(cadena_izq_der)
    
    cadena_der_izq = ''
    for i in range(len(cadena)):
        cadena_der_izq += cadena[i * (-1) - 1]
    #print(cadena_der_izq)
    
    
    if cadena_izq_der == cadena_der_izq:
        bool = True
    else:
        bool = False
    return bool

# Test
print(es_palindromo('tocot'))
