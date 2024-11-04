matrix = [[2, 4, 5, 8], [6, 3, 1, 9]]
# matrix[0][2] = 50

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print('')
##############################################################################
# mi forma
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any)-> list:
    matriz = [[valor_inicial] * cantidad_columnas] * cantidad_filas
    return matriz

# print(f'Mi forma: {inicializar_matriz(3, 5, 1)}')

# otra forma
def inicializar_matroz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any)-> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz
##############################################################################
# mi_matriz = inicializar_matroz(2, 4, 0)
# print(mi_matriz)

def cargar_matriz_secuencialmente(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f'Fila {i} Columna {j}: '))

# cargar_matriz_secuencialmente(mi_matriz)
# print(mi_matriz)
##############################################################################
def cargar_matriz_aleatoriamente(matriz: list):
    seguir = 'S'
    while seguir == 'S':
        fila = int(input('Ingrese la fila: '))
        columna = int(input('Ingrese la columna: '))
        matriz[fila][columna] = int(input('Ingrese el valor: '))
        seguir = input('¿Desea seguir? S/N: ')

# cargar_matriz_aleatoriamente(mi_matriz)
# print(mi_matriz)
##############################################################################
def buscar_valor_entero(matriz: list, valor: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f'Se encontró el número en fila {i} columna {j}!')

buscar_valor_entero(matrix, 8)