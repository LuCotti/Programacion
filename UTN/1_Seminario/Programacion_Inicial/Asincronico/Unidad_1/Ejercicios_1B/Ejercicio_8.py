# Cree un programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.
producto = input('Ingrese el nombre del producto: ')
precio = float(input('Ingrese el precio del producto: '))

iva = precio * 1.21

print('El precio de',producto,'con IVA es igual a $',iva)