'''6. Implementar una función llamada reemplazar_nombres que reciba los siguientes
parámetros:
● Una lista de nombres (lista_nombres).
● Un nombre a buscar en la lista (nombre_antiguo).
● Un nombre de reemplazo (nombre_nuevo).
La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por
nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.'''
lista_nombres = ['Pepe', 'María', 'Ignacio', 'Camila', 'María']

def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str)-> int:
    lista_nueva = []
    cantidad_reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nueva += [nombre_nuevo]
            cantidad_reemplazos += 1
        else:
            lista_nueva += [lista_nombres[i]]
    
    return cantidad_reemplazos

print(reemplazar_nombres(lista_nombres, 'María', 'Ricardo'))
