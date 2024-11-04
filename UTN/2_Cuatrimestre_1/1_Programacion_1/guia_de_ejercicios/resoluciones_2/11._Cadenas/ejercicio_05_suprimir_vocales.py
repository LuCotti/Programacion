'''
5) Crear una función que reciba una cadena por parámetro y suprima las
vocales de la misma.
Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
'''
def suprimir_vocales(cadena: str) -> str:
    cadena_resultante = ''
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    for i in range(len(cadena)):
        bandera_vocal = 0
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                bandera_vocal = 1
        if bandera_vocal == 0:
            cadena_resultante += cadena[i]
    
    return cadena_resultante

# Test
print(suprimir_vocales('Qué querés? QUÉ QUERÉEÉÉEÉEEÉEÉEÉEÉES?!?!?!?!?!?!'))
