'''2. Crear una función intercalar_vectores que reciba dos vectores de números
enteros ordenados en orden ascendente, y devuelva un único vector también
ordenado. La función debe tener un parámetro opcional descendente para que el
vector resultante esté en orden descendente.'''
vector_1 = [1, 3, 5, 7, 9]
vector_2 = [2, 4, 6, 8, 10]

def intercalar_vectores(vector_1, vector_2, bool= False):
    vector_resultante = []
    for i in range(len(vector_1)):
        if vector_1[i] <= vector_2[i]:
            vector_resultante += [vector_1[i]]
            vector_resultante += [vector_2[i]]
        else:
            vector_resultante += [vector_2[i]]
            vector_resultante += [vector_1[i]]
    
    if bool == True:
        for i in range(len(vector_resultante) // 2):
            auxiliar = vector_resultante[i]
            vector_resultante[i] = vector_resultante[-i - 1]
            vector_resultante[-i - 1] = auxiliar
    
    return vector_resultante


print(f'Ascendente: {intercalar_vectores(vector_1, vector_2)}')
print(f'Descendente: {intercalar_vectores(vector_1, vector_2, True)}')