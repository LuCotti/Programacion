import random
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        
        matriz += [fila]
    
    return matriz

def posicionar_barcos(tablero, cantidad_barcos):
    for i in range(cantidad_barcos):
        fila = random.randint(0, len(tablero) - 1)
        columna = random.randint(0, len(tablero) - 1)
        tablero[fila][columna] = 'B'
    
    return tablero

def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(f'|  {tablero[i][j]}  ', end=' ')
        print('')
