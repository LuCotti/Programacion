Desarrollar un programa que permita gestionar el inventario y las ventas de un local. 
Se tienen dos archivos CSV

1. Archivo de inventario (inventario.csv). Contiene la información de los productos disponibles. Los campos son:

ID: Identificador 
Nombre: Nombre del producto
Cantidad: Cantidad del producto
Precio: Precio del producto

2. Archivo de ventas (ventas.csv): Cada vez que se realiza una venta, se registra una entrada en este archivo con los campos:
   
   ID de producto
   Cantidad vendida
   Fecha

El programa debe permitir las siguientes operaciones:

1. Registrar la venta:
   Solicitar al usuario el ID del producto y la cantidad que desea vender
   Verificar si hay suficiente cantidad en el inventario. Si es así, actualizar el archivo inventario y registrar la venta en ventas.csv
2. Mostrar inventario
    Leer y mostrar todos los productos disponibles
3. Generar un reporte de ventas
    Mostrar el total de ingresos generados por cada producto y el total general de ventas
