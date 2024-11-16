'''
6) Crear una función para contar cuántas veces aparece una subcadena dentro
de una cadena.
Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
retornar el valor 2.
'''
def buscar_subcadenas(cadena: str, subcadena: str) -> int:
    contador_subcadena = 0
    for i in range(len(cadena)):
        contador_auxiliar = 0
        if cadena[i] == subcadena[0]:
            try:
                for j in range(1, len(subcadena)):
                    if cadena[i + j] == subcadena[j]:
                        contador_auxiliar += 1
                if contador_auxiliar == len(subcadena) - 1:
                    contador_subcadena += 1
                else:
                    continue
            except IndexError:
                continue
    
    return contador_subcadena

# Test
print(buscar_subcadenas('El pan del panadero napa', 'pan'))
