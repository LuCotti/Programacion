lista = [4, 7, 2, 78, 90, -1]

def selection_sort(vector: list) -> list:
    for i in range(len(vector)):
        minimo = vector[i]
        posicion_minimo = i
        for j in range(i + 1, len(vector)):
            if vector[j] < minimo:
                minimo = vector[j]
                posicion_minimo = j
        
        auxiliar = vector[i]
        vector[i] = minimo
        vector[posicion_minimo] = auxiliar
    
    return vector



print(selection_sort(lista))