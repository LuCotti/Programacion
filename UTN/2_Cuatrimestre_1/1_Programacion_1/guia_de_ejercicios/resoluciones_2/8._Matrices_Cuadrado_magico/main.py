################################## CONSIGNA ##################################
'''
Un cuadrado mágico es una matriz cuadrada en la
que la suma de los números en cada fila, cada
columna y cada diagonal principal es la misma. Esto
se conoce como constante mágica del cuadrado.
La misma se calcula:

M = n*(n² + 1)/2

Formalmente, un cuadrado mágico de orden n, es
una matriz cuadrada de nxn donde los números
enteros del 1 al n² están dispuestos de tal manera
que la suma de los números en cada fila, cada
columna y cada diagonal principal es igual a la
misma constante mágica.

Deberán desarrollar un programa que determine si
el cuadrado de valores ingresado por el usuario es o
no un cuadrado mágico. Tener en cuenta todas las
validaciones posibles.
'''
################################# RESOLUCIÓN #################################
from Package_cuadrado_magico.funciones_cuadrado_magico import *

matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

print(verificar_cuadrado_magico(matrix))
