from Package_barcos.funciones_barcos import *
tablero = inicializar_matriz(5, 5, 0)
cantidad_barcos = int(input('Ingrese la cantidad de barcos: '))
posicionar_barcos(tablero, cantidad_barcos)
imprimir_tablero(tablero)
