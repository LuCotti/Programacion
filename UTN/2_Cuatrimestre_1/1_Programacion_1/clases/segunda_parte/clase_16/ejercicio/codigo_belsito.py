import csv
from datetime import datetime


# Paso 1
# Función para leer el archivo de inventario
def leer_inventario():
    inventario = [] # inicia una lista vacía
    with open("inventario.csv", "r") as archivo:
        lector_csv = csv.reader(archivo) # crea un objeto que permite leer el archivo
        next(lector_csv)  # Omitir encabezado
        
        for fila in lector_csv: # aca creo un diccionario con los datos del archivo csv.
            inventario.append({
                "ID": fila[0],
                "Nombre": fila[1],
                "Cantidad": int(fila[2]),
                "Precio": float(fila[3])
            })
    return inventario


# Paso 3
# Función para escribir en el archivo de inventario

def escribir_inventario(inventario):
    with open("inventario.csv", "w", newline='') as archivo: # newline='' opción para manejar el salto de línea, asegurando que los registros se escriban correctamente.
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["ID", "Nombre", "Cantidad", "Precio"])
        for item in inventario:
            escritor_csv.writerow([item["ID"], item["Nombre"], item["Cantidad"], item["Precio"]])


# Paso 2
# Función para registrar una venta

def registrar_venta():
    inventario = leer_inventario()
    id_producto = input("Ingrese el ID del producto: ")
    cantidad_vender = int(input("Ingrese la cantidad que desea vender: "))

    # Buscar el producto en el inventario
    for item in inventario:
        if item["ID"] == id_producto:
            if item["Cantidad"] >= cantidad_vender:
                item["Cantidad"] -= cantidad_vender  # Reducir cantidad en inventario
                escribir_inventario(inventario)  # Actualizar inventario

                # Registrar la venta en ventas.csv
                with open("ventas.csv", "a", newline='') as archivo: # abre el archivo en modo de agregar "a"
                    escritor_csv = csv.writer(archivo)
                    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    escritor_csv.writerow([id_producto, cantidad_vender, fecha_venta])

                print(f"Venta registrada. Producto: {item['Nombre']}, Cantidad vendida: {cantidad_vender}")
                return
            else:
                print("No hay suficiente cantidad en el inventario.")
                return
    print("Producto no encontrado en el inventario.")

# Función para mostrar el inventario
def mostrar_inventario():
    inventario = leer_inventario()
    print("Inventario actual:")
    for item in inventario:
        print(f"ID: {item['ID']}, Nombre: {item['Nombre']}, Cantidad: {item['Cantidad']}, Precio: {item['Precio']}")

# Función para generar el reporte de ventas
def generar_reporte_ventas():
    ventas = {} # Crea un diccionario vacío para almacenar la cantidad vendida de cada producto.
    with open("ventas.csv", "r") as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            id_producto, cantidad_vendida, _ = fila # el _ se usa para ignorar la fecha, extrae el ID del producto y la cantidad vendida de cada fila.
            cantidad_vendida = int(cantidad_vendida)

            if id_producto not in ventas:
                ventas[id_producto] = 0
            ventas[id_producto] += cantidad_vendida

    # Leer precios y nombres del inventario
    inventario = leer_inventario()
    total_ingresos = 0

    print("\nReporte de ventas:")
    for item in inventario:
        id_producto = item["ID"]
        if id_producto in ventas:
            ingresos = ventas[id_producto] * item["Precio"]
            total_ingresos += ingresos
            print(f"Producto: {item['Nombre']}, Cantidad vendida: {ventas[id_producto]}, Ingresos: {ingresos:.2f}")

    print(f"Total de ingresos por ventas: {total_ingresos:.2f}")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Inventario y Ventas ---")
        print("1. Registrar venta")
        print("2. Mostrar inventario")
        print("3. Generar reporte de ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            generar_reporte_ventas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()
