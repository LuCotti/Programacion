# from ..Package_Input.Input import get_int
# input = __import__("../Package_Input/Input.py")
import sys
import os
sys.path.append(os.path.abspath("../Package_Input"))
# import Input
# from Input import get_int
# from Package_Input import Input
from Package_Input.Input import *

# lista_numeros = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7]


'''a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.'''
def ingresar_numeros(lista: list) -> list:
    for i in range(10):
        lista += [get_int('Ingrese un número entre -1000 y 1000: ', 'Dato inválido.', -1000, 1000, 4)]
    return lista

'''b. Mostrar la cantidad de números positivos y negativos.'''
def mostrar_positivos_y_negativos(lista: list):
    contador_positivos = 0
    contador_negativos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contador_negativos += 1
        else:
            contador_positivos += 1
    
    print(f'Cantidad de números positivos: {contador_positivos}\nCantidad de números negativos: {contador_negativos}')

'''c. Mostrar la sumatoria de los números pares.'''
def mostrar_suma_pares(lista: list):
    sumatoria = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            sumatoria += lista[i]
    
    print(f'La suma de los números pares ingresados es igual a {sumatoria}')

# mostrar_suma_pares(lista_numeros)

'''d. Informar el mayor de los números impares.'''
def mostrar_impar_mayor(lista: list):
    impar_mayor = -1000
    for i in range(len(lista)):
        if lista[i] == 0:
            impar_mayor = lista[i]
        elif lista[i] % 2 == 1 and lista[i] > impar_mayor:
            impar_mayor = lista[i]
    
    print(f'El mayor de los números impares es {impar_mayor}')

'''e. Listar todos los números ingresados.'''
def listar_numeros(lista: list):
    lista_2 = []
    for i in range(len(lista)):
        lista_2 += [lista[i]]
    
    print(f'Números ingresados: {lista_2}')

'''f. Listar todos los números pares.'''
def listar_pares(lista: list):
    lista_pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pares += [lista[i]]
    
    print(f'Números pares ingresados: {lista_pares}')

'''g. Listar los números de las posiciones impares.'''
def listar_posiciones_impares(lista: list):
    lista_posiciones_impares = []
    for i in range(len(lista)):
        if i % 2 == 1:
            lista_posiciones_impares += [lista[i]]
    
    print(f'Números de posiciones impares: {lista_posiciones_impares}')

