matrix = [[2, 4, 5, 8],
            [6, 3, 1, 9]]

print(matrix)

print(matrix[0])
print(matrix[1])


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print('')
################################################################

print(matrix[1][0]) # 6

matrix[1][0] = 15

print(matrix[1][0]) # 15

################################################################

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        
        matriz += [fila]
    
    return matriz

mi_matriz = inicializar_matriz(0, 0, 0)