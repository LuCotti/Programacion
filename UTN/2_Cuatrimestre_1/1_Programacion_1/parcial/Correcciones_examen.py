import random
# Punto 2
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




# Punto 4
# Lo que debería haber hecho
def validar_cadena_alfanum(entrada_usuario):
    if (len(entrada_usuario) != 0) and (entrada_usuario.isalnum):
        return True
    else:
        return False

entrada_usuario = input('Ingrese una opción alfanumérica: ')
if validar_cadena_alfanum(entrada_usuario):
    print('La cadena es válida.')
else:
    print('La cadena es inválida.')


# Max y min otra forma
def buscar_min_max_en_rango(lista, valor_inicio, valor_fin):
    lista_numeros_rango = []
    
    for i in range(len(lista)):
        if lista[i] >= valor_inicio and lista[i] <= valor_fin:
            lista_numeros_rango += [lista[i]]
    
    # max min
    minimo = lista_numeros_rango[0]
    maximo = lista_numeros_rango[0]
    for i in range(1, len(lista_numeros_rango)):
        if lista_numeros_rango[i] < minimo:
            minimo = lista_numeros_rango[i]
        if lista_numeros_rango[i] > maximo:
            maximo = lista_numeros_rango[i]
    
    return minimo, maximo

# minimo, maximo = buscar_min_max_en_rango(lista, 0, 1)




# Mostrar Menú
def mostrar_menu():
    print('\nMenú de opciones: ')
    print('1. Generar lista de números aleatorios. ')
    print('2. Ordenar lista de números aleatorios. ')
    print('3. Buscar cantidad de números en un rango. ')
    print('4. Máximo y mínimo en un rango. ')
    print('5. Generar matriz alfanuméricos. ')
    print('6. Salir. ')

def programa():
    while True:
        mostrar_menu()
        opcion = input('Ingrese su opción: ')
        
        if opcion == '1':
            pass
        elif opcion == '2':
            # criterio = input('Ingrese el criterio')
            # if criterio == 'ASC' or criterio == 'DESC':
            #   ordenar_lista(lista_numeros)
            #   print lista_numeros
            # else:
            #   print('Debe ingresar el criterio')
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            # if valor_inicial != 0 and valor_final != 0:
            #     minimo, maximo = buscar_min_max()
            # else:
            #     print('Debe generar el rango de la opción 3')
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            print('El programa ha finalizado!')
            break