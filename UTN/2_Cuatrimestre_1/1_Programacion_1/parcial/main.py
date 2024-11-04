################################## CONSIGNA ##################################
'''
Desarrollar una biblioteca que contenga las siguientes funciones:
1.Generar una lista de números enteros aleatorios: Desarrollar una función que
genere de manera aleatoria una lista de 50 números enteros positivos entre 1
y 100.

2.Generar una matriz de caracteres alfanuméricos: Desarrollar una función que
genere de manera aleatoria una matriz de 6 filas por 15 columnas (6 listas de
15 elementos cada una), compuesta de caracteres alfanuméricos (letras y
dígitos).

3.Ordenar una lista de números enteros: Desarrollar una función que ordene una
lista de números enteros, recibiendo como parámetro el criterio de
ordenamiento "ASC" o "DESC" (ascendente o descendente).

4.Validar el ingreso de una cadena alfanumérica: Desarrollar una función que
valide el ingreso de una cadena de caracteres alfanuméricos (letras y
números), y que será utilizada en el menú de opciones.



Menú de Opciones Operado por Consola:
El programa debe contar con un menú de opciones que permita realizar las
siguientes operaciones:
1.  Generar la lista de números enteros aleatorios utilizando la función
desarrollada en el punto 1.

2. Ordenar la lista de números generada anteriormente, utilizando la función
desarrollada en el punto 3.

3. Buscar cuántos números están en un rango dado: Solicitar al usuario que
ingrese un rango (por ejemplo, entre 10 y 50) e informar cuántos números de la
lista generada en el punto 1 caen dentro de dicho rango.
El informe deberá seguir este formato:
CANTIDAD DE NÚMEROS EN EL RANGO [Valor Inicial-Valor Final]: Cantidad

4. Del ítem anterior, obtener: El número máximo y mínimo que se encuentre
dentro del rango, e informar su valor.

5. Generar la matriz de caracteres alfanuméricos, utilizando la función
desarrollada en el punto 2.
'''
################################# RESOLUCIÓN #################################
# DESARROLLAR BIBLIOTECA
# Punto 1
import random
lista_numeros_aleatorios = []

def generar_lista_aleatorios(vector: list, cantidad_numeros: int, minimo: int, maximo: int) -> list:
    vector = [0] * cantidad_numeros
    for i in range(cantidad_numeros):
        vector[i] = random.randint(minimo, maximo)
    return vector

# Las siguientes dos líneas son para probar el código.
# lista_numeros_aleatorios = generar_aleatorios(lista_numeros_aleatorios, 5, 20, 30)
# print(lista_numeros_aleatorios)



# Punto 2
matriz_alfanumerica = []

def generar_matriz_alfanumerica(filas: int, columnas: int) -> list:
    matriz = [0] * filas
    for i in range(filas):
        matriz[i] = [0] * columnas
        for j in range(columnas):
            caracter_alfanumerico = random.randint(48, 90)
            while caracter_alfanumerico >= 58 and caracter_alfanumerico <= 64: # Omitimos los símbolos que no sean ni letras ni números
                caracter_alfanumerico = random.randint(48, 90)
            caracter_alfanumerico = chr(caracter_alfanumerico)
            
            matriz[i][j] = caracter_alfanumerico
    
    return matriz

# Las siguientes dos líneas son para probar el código.
# matriz_alfanumerica = generar_matriz_alfanumerica(2, 4)

# OTRA FORMA
def cargar_matriz_alfanum(matriz):
    letras = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    digitos = '0123456789'
    alfanumericos = letras + digitos # Rango 0 - 61
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            num_ran = random.randint(0, len(alfanumericos) - 1)
            matriz[i][j] = alfanumericos[num_ran]
    
    return matriz

# OTRA FORMA MÁS
# may 65-90
# min 97-122
# dig 48-57
def cargar_matriz_alfanum_2(matriz):
    for i in range(len(matriz)): # Ciclo por fila
        for j in range(len(matriz[i])): # Ciclo por columna
            codigo_ascii = random.randint(0, 61)
            if codigo_ascii < 10: # Dígitos
                matriz[i][j] = chr(codigo_ascii + 48)
            elif codigo_ascii < 36: # Mayúsculas
                matriz[i][j] = chr(codigo_ascii + 55)
            else:
                matriz[i][j] = chr(codigo_ascii + 61)
    
    return matriz




def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print('')
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')

# La siguiente línea es para probar el código.
# mostrar_matriz(matriz_alfanumerica)



# Punto 3
import funciones.ordenamiento
# Las siguientes dos líneas son para probar el código.
# lista = [7, 1, 5, 4, 9]
# print(funciones.ordenamiento.bubble_sort(lista, 'DES'))



# Punto 4
import funciones.input

# Lo que debería haber hecho
def validar_cadena_alfanum(entrada_usuario):
    if (len(entrada_usuario) != 0) and (entrada_usuario.isalnum):
        return True
    else:
        return False

# entrada_usuario = input('Ingrese una opción alfanumérica: ')
# if validar_cadena_alfanum(entrada_usuario):
#     print('La cadena es válida.')
# else:
#     print('La cadena es inválida.')





# MENÚ DE OPCIONES
menu = '''\n1. Generar lista.
2. Ordenar lista.
3. Buscar e Informar cantidad de números en la lista dentro de un rango.
4. Mostrar máximo y mínimo de la opción 3.
5. Generar la matriz de caracteres alfanuméricos.
6. Salir.
'''

# 3. Buscar cuántos números están en un rango dado.
def buscar_rango_en_lista(lista: list, minimo: int, maximo: int) -> any:
    contador = 0
    lista_encontrados = []
    for i in range(len(lista)):
        if lista[i] >= minimo and lista[i] <= maximo:
            lista_encontrados += [lista[i]]
            contador += 1
    
    return contador, lista_encontrados

# Las siguientes tres líneas son para probar el código
# lista = [7, 1, 5, 4, 9, 15, 18, 26, 29, 37, 41]
# inicio = 1
# fin = 20
# buscar_rango_en_lista(lista, inicio, fin)





# 4. Obtener el número máximo y mínimo
lista_encontrados = []
def maximo_y_minimo(vector: list) -> int:
    minimo = None
    maximo = None
    if len(vector) == 0:
        print('La lista ingresada está vacía.')
        minimo = 0
        maximo = 0
        return minimo, maximo
    else:
        for i in range(len(vector)):
            if i == 0:
                minimo = vector[i]
                maximo = vector[i]
            elif vector[i] > maximo:
                maximo = vector[i]
            elif vector[i] < minimo:
                minimo = vector[i]
    
    return minimo, maximo

# Las siguientes dos líneas son para probar el código
# print('Valor mínimo encontrado:', maximo_y_minimo(lista)[0])
# print('Valor mínimo encontrado:', maximo_y_minimo(lista)[1])



seguir = 'S'

while seguir == 'S':
    print(menu)
    opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
    
    if lista_numeros_aleatorios == [] and opcion_ingresada != '1':
        print('Primero debe generar la lista de números.')
    else:
        match opcion_ingresada:
            case '1':
                lista_numeros_aleatorios = generar_lista_aleatorios(lista_numeros_aleatorios, 50, 1, 100)
                print(lista_numeros_aleatorios)
            case '2':
                criterio_de_ordenamiento = funciones.input.get_string('Ingrese el criterio de ordenamiento (ASC/DES): ', 'Dato inválido', 0, 3)
                print(funciones.ordenamiento.bubble_sort(lista_numeros_aleatorios, criterio_de_ordenamiento))
            case '3':
                minimo = funciones.input.get_int('Ingrese el mínimo: ', 'Dato inválido', -9999, 9999, 3)
                maximo = funciones.input.get_int('Ingrese el máximo: ', 'Dato inválido', -9999, 9999, 3)
                contador_encontrados = buscar_rango_en_lista(lista_numeros_aleatorios, minimo, maximo)[0]
                lista_encontrados = buscar_rango_en_lista(lista_numeros_aleatorios, minimo, maximo)[1]
                print('\nSe encontraron los siguientes números:', lista_encontrados)
                print(f'Cantidad encontrada en el rango {minimo}-{maximo}:', contador_encontrados)
            case '4':
                print('Valor mínimo encontrado:', maximo_y_minimo(lista_encontrados)[0])
                print('Valor mínimo encontrado:', maximo_y_minimo(lista_encontrados)[1])
            case '5':
                filas = funciones.input.get_int('Ingrese la cantidad de filas: ', 'Dato inválido', -9999, 9999, 3)
                columnas = funciones.input.get_int('Ingrese la cantidad de columnas: ', 'Dato inválido', -9999, 9999, 3)
                matriz_alfanumerica = generar_matriz_alfanumerica(filas, columnas)
                mostrar_matriz(matriz_alfanumerica)
            case '6':
                break
            case _:
                print('La opción ingresada no existe.')