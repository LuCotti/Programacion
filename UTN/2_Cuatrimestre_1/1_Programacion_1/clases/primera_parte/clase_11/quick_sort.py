lista = [33, 10, 59, 270, 1, 90, 50]

# pivot = lista[8]
# lista_menores = []
# lista_mayores = []

# for i in range(len(lista)):
#     if lista[i] < pivot:
#         lista_menores[i] = lista[i]
#     elif lista[i] > pivot:
#         lista_mayores[i] = lista[i]


# print(lista)
# print(lista_menores)
# print(lista_mayores)
##############################################################################
def quicksort(vector):
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
    return quicksort(vector_izquierdo) + [pivote] + quicksort(vector_derecho)

print(quicksort(lista))