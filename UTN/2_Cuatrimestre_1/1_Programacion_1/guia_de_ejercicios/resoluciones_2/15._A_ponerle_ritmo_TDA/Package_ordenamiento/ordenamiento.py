def bubble_sort(vector: list, orientacion='ASC') -> list:
    if orientacion == 'ASC':
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
    else:
        flag_cambio = True
        while flag_cambio:
            contador_cambios = 0
            for i in range(len(vector) - 1):
                if vector[i] < vector[i + 1]:
                    auxiliar = vector[i]
                    vector[i] = vector[i + 1]
                    vector[i + 1] = auxiliar
                    contador_cambios += 1
            if contador_cambios > 0:
                flag_cambio = True
            else:
                flag_cambio = False
    
    return vector

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

def quick_sort(vector: list, orientacion='ASC'):
    if orientacion == 'ASC':
        if len(vector) <= 1: # 0 o 1
            return vector
        else:
            pivote = vector[0]
            
            vector_izquierdo = []
            vector_derecho = []
            
            for i in range(1, len(vector)):
                if vector[i] <= pivote:
                    vector_izquierdo += [vector[i]]
                else:
                    vector_derecho += [vector[i]]
        
        vector_ordenado = quick_sort(vector_izquierdo, orientacion) + [pivote] + quick_sort(vector_derecho, orientacion)
        return vector_ordenado
    else:
        if len(vector) <= 1: # 0 o 1
            return vector
        else:
            pivote = vector[0]
            
            vector_izquierdo = []
            vector_derecho = []
            
            for i in range(1, len(vector)):
                if vector[i] <= pivote:
                    vector_derecho += [vector[i]]
                else:
                    vector_izquierdo += [vector[i]]
        
        vector_ordenado = quick_sort(vector_izquierdo, orientacion) + [pivote] + quick_sort(vector_derecho, orientacion)
        return vector_ordenado

# lista = [5, 1, 10, 3, 20]
# print(quick_sort(lista, 'ASC'))
