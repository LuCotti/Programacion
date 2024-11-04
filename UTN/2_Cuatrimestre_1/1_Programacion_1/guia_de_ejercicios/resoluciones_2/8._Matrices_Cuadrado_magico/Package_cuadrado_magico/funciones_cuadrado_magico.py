def verificar_cuadrado_magico(matriz: list):
    filas = 0
    columnas = 0
    
    # Determinamos la cantidad de filas y columnas de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0:
                columnas += 1
        filas += 1
    
    # Verificamos que la matriz sea cuadrada
    if filas != columnas:
        return print('La matriz ingresada no es cuadrada')
    else:
        n = filas
        constante_magica = n * (n ** 2 + 1) // 2
        sumatoria_diagonal_principal = 0
        sumatoria_diagonal_secundaria = 0
        
        # Verificamos que la suma de las filas, columnas y diagonales sean iguales a la constante mágica
        for i in range(len(matriz)):
            sumatoria_fila = 0
            for j in range(len(matriz[i])):
                sumatoria_fila += matriz[i][j] # Verificamos la suma de las filas
                # matriz_auxiliar += matriz[i][j] # CORREGIR
                
                
                if i == j: # Verificamos la suma de la diagonal principal
                    sumatoria_diagonal_principal += matriz[i][j]
                if (len(matriz[i]) - i - 1) == j: # Verificamos la suma de la diagonal secundaria o inversa
                    sumatoria_diagonal_secundaria += matriz[i][j]
            
            if sumatoria_fila != constante_magica:
                return False
        
        if sumatoria_diagonal_principal != constante_magica:
            return False
        
        if sumatoria_diagonal_secundaria != constante_magica:
            return False
        
        # Verificamos la suma de las columnas
        total = [0] * columnas
        for fila in matriz:
            for columna in range(columnas):
                total[columna] += fila[columna]
        
        for i in range(len(total)):
            if total[i] != constante_magica:
                return False
        
        return True

