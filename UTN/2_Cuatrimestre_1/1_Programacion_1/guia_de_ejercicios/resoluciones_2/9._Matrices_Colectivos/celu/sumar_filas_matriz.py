A = [[1,2,3],[4,5,6],[7,8,9]]

def sumar_filas(matriz):
    lista_resultante = [0] * len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista_resultante[i] += matriz[i][j]
    
    return lista_resultante


print(sumar_filas(A))


