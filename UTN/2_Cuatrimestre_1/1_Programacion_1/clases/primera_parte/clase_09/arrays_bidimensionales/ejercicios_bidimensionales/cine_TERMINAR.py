'''Sistema de Reserva de Butacas de Cine

Desarrolla un programa en Python que simule un sistema de reserva de butacas 
en una sala de cine. El cine tiene una disposición de asientos en una matriz 
de tamaño 5x5, donde cada celda representa una butaca.

Requisitos del Sistema:

Visualización del Cine:

El programa debe mostrar el estado actual de las butacas, donde:
'O' representa una butaca disponible.
'X' representa una butaca ocupada.
Al inicio, todas las butacas están disponibles.

Reserva de Asientos:

El usuario puede reservar una butaca proporcionando el número de fila y de 
columna.
Si la butaca está disponible, se marca como ocupada y se muestra un mensaje de
confirmación.
Si la butaca ya está ocupada, se muestra un mensaje indicando que no está 
disponible y se le pide que seleccione otra.

Cancelar una Reserva:

El usuario puede cancelar la reserva de una butaca, proporcionando su fila y 
columna.
Si la butaca está ocupada, se marca como disponible nuevamente y se muestra un
mensaje de confirmación.
Si la butaca no está ocupada, se indica que no hay una reserva en esa posición.

Salir del Sistema:

El sistema debe permitir al usuario realizar varias reservas o cancelaciones, 
hasta que decida salir.'''

# HACER MENÚ
menu = '''Bienvenido al cine. Ingrese una de las siguientes opciones:
1. Reservar un asiento.
2. Cancelar reserva.
3. Salir.'''



def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        
        matriz += [fila]
    
    return matriz

print(inicializar_matriz(4, 4, 1))

def visualizacion_del_cine():
    pass

def reserva_de_asientos():
    pass

def cancelar_una_reserva():
    pass

def salir_del_sistema():
    pass

