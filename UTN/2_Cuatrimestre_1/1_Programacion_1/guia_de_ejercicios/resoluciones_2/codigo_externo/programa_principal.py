import random
#-----------------------------------------------------------
#1
def generar_lista_aleatoria():
    lista = [0] * 50
    for i in range(len(lista)):
        lista[i] = random.randint(1, 100)
    return lista
print(generar_lista_aleatoria())
#2
def ordenar_lista(lista, criterio = "ASC"):
    n = len(lista)
    for i in range(n):
       for j in range(0, n- i - 1):
           if criterio == "ASC":
                if lista[j] > lista[j + 1]:
                    auxiliar = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = auxiliar
           elif criterio == "DESC":
               if lista[j] < lista[j + 1]:
                    auxiliar = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = auxiliar
    return lista
#3
def calcular_cantidad_numeros_rango(lista, valor_inicio, valor_fin):
        cantidad = 0
        for i in range(len(lista)):
            if (lista[i] >= valor_inicio) and (lista[i] <= valor_fin):
                cantidad += 1
        return cantidad
#4
def buscar_min_max_en_rango(lista, valor_inicial, valor_final):
    lista_numeros_rango = []
    for i in range(len(lista)):
        if (lista[i] >= valor_inicial) and (lista[i] <= valor_final):
            lista_numeros_rango += [lista[i]]
    minimo = lista_numeros_rango[0]
    maximo = lista_numeros_rango[0]
    for i in range(1, (lista_numeros_rango)):
        if lista_numeros_rango[i] < minimo:
            minimo = lista_numeros_rango[i]
        if lista_numeros_rango[i] > maximo:
            maximo = lista_numeros_rango[i]
    return minimo, maximo
#5
def inicializar_matriz(cant_filas, cant_columnas, valor):
    matriz = []
    
    for i in range(cant_filas):
        fila = [valor] * cant_columnas
        matriz += [fila]
    
    return matriz    
def cargar_matriz_alfanum(matriz):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "0123456789"
    alfanumericos = letras + digitos
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            num_ran = random.randint(0, len(alfanumericos) - 1)
            matriz[i][j] = alfanumericos[num_ran]
    return matriz
#------------------------------------------------------------
def mostrar_menu():
    print("********** MENÚ **********")
    print("1. generar lista de números aleatorios")
    print("2. ordenar lista de números aleatorios")
    print("3. buscar cantidad de uúmeros en un rango")
    print("4. Máximos y mínimos en un rango")
    print("5. generar la matriz de alfanuméricos")
    print("6. Salir")
    
def programa():
    lista_numeros = []
    valor_final = 0
    valor_inicial = 0
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        #-------------------------------------------
        if opcion == "1":
            lista_numeros = generar_lista_aleatoria()
            print(lista_numeros)
        #-------------------------------------------    
        elif opcion == "2":
            if len(lista_numeros) != 0:
                criterio = input("ordenar lista ASC o DESC: ")
                if criterio == "ASC" or criterio == "DESC":
                    ordenar_lista(lista_numeros, criterio)
                    print(lista_numeros)
                else:
                    print("opción no válida")
            else:
                print("lista vacia pa")
        #-------------------------------------------
        elif opcion == "3":
            if len(lista_numeros) != 0:
                valor_inicial = int(input("ingrese valor inicial: "))
                valor_final = int(input("ingrese valor final: "))
                cantidad = calcular_cantidad_numeros_rango(lista_numeros, valor_inicial, valor_final)
                print(f"La cantidad de números en el rango {valor_inicial}, {valor_final}")
            else:
                print("lista vacia pa")
        #-------------------------------------------
        elif opcion == "4":
            if len(lista_numeros) != 0:
                if (valor_inicial != 0) and (valor_final != 0):
                    minimo , maximo = buscar_min_max_en_rango(lista_numeros, valor_inicial, valor_final)
                    print(f"El minimo es {minimo} y el maximo es {maximo}")                
                else:
                    print("no hay rango de la opción 3")
            else:
                print("lista vacia pa")
        #-------------------------------------------    
        elif opcion == "5":
            matriz = inicializar_matriz(6, 15, "*")
            matriz = cargar_matriz_alfanum(matriz)
            print(matriz)
        #-------------------------------------------    
        elif opcion == "6":
            print("programa finalizado pa")
            break        
programa()