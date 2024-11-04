def inicializar_matriz(filas,columnas,valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def calcular_matriz_opuesta(matriz):
    matriz_opuesta = inicializar_matriz(len(matriz),len(matriz[0]),0)
    for i in range(len(matriz_opuesta)):
        for j in range(len(matriz_opuesta[i])):
            matriz_opuesta[i][j] = matriz[i][j] * -1
    return matriz_opuesta
M = [[2,4,6],[1,3,5],[-1,-4,-7]]

print(calcular_matriz_opuesta(M))
