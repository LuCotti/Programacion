lista = [4, 7, 2, 78, 90, -1]
def bubble_sort(vector: list) -> list:
    flag_cambio = True
    while flag_cambio:
        contador_cambios = 0
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                auxiliar = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = auxiliar
                contador_cambios += 1
        if contador_cambios > 0:
            flag_cambio = True
        else:
            flag_cambio = False
    
    return vector

print(bubble_sort(lista))