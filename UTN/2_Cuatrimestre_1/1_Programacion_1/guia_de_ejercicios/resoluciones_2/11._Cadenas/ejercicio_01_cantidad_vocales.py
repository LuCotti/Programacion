'''
1) Crear una función que reciba como parámetro una cadena y determine la
cantidad de vocales que hay de cada una (individualmente). La función
retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
la cantidad.
'''
def mostrar_matriz(matriz: list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print('')

def buscar_vocales(cadena: str) -> list:
    matriz = [['a', 0], ['e', 0], ['i', 0], ['o', 0], ['u', 0]]
    for i in range(len(cadena)):
        for j in range(len(matriz)):
            if cadena[i] == matriz[j][0]:
                matriz[j][1] += 1
    return matriz

# Test
mostrar_matriz(buscar_vocales('paleontologia'))
