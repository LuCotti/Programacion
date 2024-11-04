import random
# Funciones
def inicializar_matriz(filas: int, columnas: int, valor_inicial: int) -> list:
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz: list) -> None:
    for i in range(len(matriz)):
        print('')
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' ')

def generar_lista_aleatoria(cantidad_elementos: int, minimo: int, maximo: int) -> list:
    lista_aleatoria = []
    for i in range(cantidad_elementos):
        lista_aleatoria += [random.randint(minimo, maximo)]
    return lista_aleatoria

def buscar_legajo(lista: list, valor_buscado: int) -> bool:
    coincide = False
    for i in range(len(lista)):
        if valor_buscado == lista[i]:
            coincide = True
    return coincide

def cargar_planilla(planilla: list, linea: int, coche: int, recaudacion: int) -> list: # CORREGIRRRRRRRRRRRRRRRRRRRRRRRRRRR
    for i in range(len(planilla)):
        if i == linea:
            for j in range(len(planilla[i])):
                if j == coche:
                    planilla[i][j] += recaudacion
    return planilla

def mostrar_recaudacion_por_linea(planilla: list) -> None:
    for i in range(len(planilla)):
        total_linea = 0
        for j in range(len(planilla[i])):
            total_linea += planilla[i][j]
        print(f'Línea {i}: {total_linea}')




# Definición de variables.
lista_legajos = generar_lista_aleatoria(15, 10, 30)
matriz_recaudaciones = inicializar_matriz(3,5,0)
menu = '''
1. Cargar planilla.
2. Mostrar todas las recaudaciones.
3. Mostrar recaudación por línea.
4. Mostrar recaudación por coche.
5. Mostrar recaudación total.
6. Salir.
'''

while True:
    print(menu)
    opcion_ingresada = input('Ingrese la opción: ')
    match opcion_ingresada:
        case '1':
            print(lista_legajos)
            id_ingresada = int(input('Identifíquese: '))
            if buscar_legajo(lista_legajos, id_ingresada):
                linea = int(input('Ingrese la línea: '))
                coche = int(input('Ingrese el coche: '))
                recaudacion = int(input('Ingrese el monto recaudado: '))
                cargar_planilla(matriz_recaudaciones, linea, coche, recaudacion)
            else:
                print('Identificación no encontrada.')
        case '2':
            mostrar_matriz(matriz_recaudaciones)
        case '3':
            mostrar_recaudacion_por_linea(matriz_recaudaciones)
        case '4':
            pass
        case '5':
            pass
        case '6':
            break
        case _:
            pass