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

def selection_sort(vector: list, orientacion= 'ASC') -> list:
    if orientacion == 'ASC':
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
    else:
        for i in range(len(vector)):
            maximo = vector[i]
            posicion_maximo = i
            for j in range(i + 1, len(vector)):
                if vector[j] > maximo:
                    maximo = vector[j]
                    posicion_maximo = j
            
            auxiliar = vector[i]
            vector[i] = maximo
            vector[posicion_maximo] = auxiliar
    
    return vector

# Test
lista = [3, 2, 58, 4, 1]
print(selection_sort(lista, 'DES'))

def quick_sort(vector):
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
    return quick_sort(vector_izquierdo) + [pivote] + quick_sort(vector_derecho)
