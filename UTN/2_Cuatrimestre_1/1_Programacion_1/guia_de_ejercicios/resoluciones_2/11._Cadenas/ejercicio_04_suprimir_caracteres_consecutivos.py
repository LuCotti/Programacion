'''
4) Crear una función que reciba como parámetro una cadena y suprima los
caracteres repetidos consecutivos.
Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
'''
def suprimir_caracteres_consecutivos(cadena: str) -> str:
    cadena_nueva = ''
    for i in range(len(cadena)):
        try:
            if cadena[i] != cadena[i + 1]:
                cadena_nueva += cadena[i]
        except IndexError:
            cadena_nueva += cadena[i]
    
    return cadena_nueva

# Test
print(suprimir_caracteres_consecutivos('oooooooooooooooooooooooooooooooooooooojjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjoooooooooooooooooooooooooo'))
