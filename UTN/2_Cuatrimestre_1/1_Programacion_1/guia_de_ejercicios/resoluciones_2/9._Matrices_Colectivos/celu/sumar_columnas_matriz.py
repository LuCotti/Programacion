A = [[1,2,3],[4,5,6],[7,8,9]]

def sumar_columnas(matriz):
    lista_resultante = [0] * len(matriz)
    for i in range(len(matriz)):
        fila = matriz[i]
        for j in range(len(fila)):
            
            lista_resultante[j] += fila[j]
    
    return lista_resultante


print(sumar_columnas(A))


