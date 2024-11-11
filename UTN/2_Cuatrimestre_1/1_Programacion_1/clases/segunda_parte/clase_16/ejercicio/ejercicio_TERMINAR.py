# Funciones.
def registrar_venta():
    inventario = open('inventario.csv', 'r') # Abrimos el archivo inventario.
    lista = inventario.readlines()
    print(lista) # Mostramos el contenido del archivo
    id_ingresada = input('Ingrese el ID del producto que desea vender: ') # Le pedimos al usuario que ingrese el id del producto.
    lista_ids = [] # Definimos una lista que contenga los ids de cada producto.
    for i in range(len(lista)):
        if i != 0:
            lista_ids.append(lista[i].split(',')[0])
    
    lista_cantidades = [] # Definimos una lista que contenga la cantidad disponible de cada producto.
    for i in range(len(lista)):
        if i != 0:
            lista_cantidades.append(lista[i].split(',')[2])
    print(f'Lista de cantidades: {lista_cantidades}')
    
    coincide = False # Verificamos si el ID ingresado existe en la lista.
    for i in range(len(lista_ids)):
        if id_ingresada == lista_ids[i]:
            coincide = True
    
    if coincide:
        cantidad_ingresada = int(input('Ingrese la cantidad que desea vender: '))
    else:
        print('El ID ingresado no existe.')
    inventario.close() # Cerramos el archivo inventario.





ventas = open('ventas.csv', 'r')
ventas.close()








# Menú y bucle.
menu = '''
1. Registrar venta.
2. Mostrar inventario.
3. Generar reporte de ventas.
4. Salir.
'''
while True:
    print(menu)
    opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
    
    match opcion_ingresada:
        case '1':
            registrar_venta()
        case '2':
            pass
        case '3':
            pass
        case '4':
            break
        case _:
            print('La opción ingresada no existe.')