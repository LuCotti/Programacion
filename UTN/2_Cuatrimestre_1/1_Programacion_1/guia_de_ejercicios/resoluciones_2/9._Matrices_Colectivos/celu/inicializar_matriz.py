def inicializar_matriz(filas,columnas,valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print('')
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' ')

M = inicializar_matriz(2,3,1)
mostrar_matriz(M)
