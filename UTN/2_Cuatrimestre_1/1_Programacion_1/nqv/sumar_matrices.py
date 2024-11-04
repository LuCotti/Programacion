A = [[11,12,13],[14,15,16],[17,18,19]]
B = [[21,22,23],[24,25,26],[27,28,29]]

def comparar_filas_y_columnas(matriz_a,matriz_b):
    #Verificar igualdad entre columnas y filas de a y b.
    #Matriz_a
    filas_a = 0
    columnas_a = 0
    for i in range(len(matriz_a)):
        filas_a += 1
        for j in range(len(matriz_a[i])):
            columnas_a += 1
    #Matriz_b
    filas_b = 0
    columnas_b = 0
    for i in range(len(matriz_b)):
        filas_b += 1
        for j in range(len(matriz_b[i])):
            columnas_b += 1
    
    if filas_a == filas_b and columnas_a == columnas_b:
        return True
    else:
        return False

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print('')
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' ')

def sumar_matrices(matriz_a,matriz_b):
    se_pueden_sumar = comparar_filas_y_columnas(matriz_a,matriz_b)
    if se_pueden_sumar:
        matriz_resultante = [0] * 3
        for i in range(len(matriz_a)):
            matriz_resultante[i] = [0] * 3
            for j in range(len(matriz_a[i])):
                valor_a = matriz_a[i][j]
                valor_b = matriz_b[i][j]
                suma = valor_a + valor_b
                matriz_resultante[i][j] = suma
        mostrar_matriz(matriz_resultante)
        return matriz_resultante
    else:
        print('Las filas y/o columnas no coinciden')
        return None

sumar_matrices(A,B)