# A. Ingresar tres precios de productos y mostrar la suma de los mismos.
print('\nSuma de productos:')
producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))

suma = producto1 + producto2 + producto3

print('La suma de los 3 productos es igual a $',suma, sep='')



# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
print('\nPromedio de productos:')
producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))

promedio = (producto1 + producto2 + producto3) / 3

print('El promedio de los 3 productos es $',promedio, sep='')



# C. ingresar tres precios de productos, sumarlos y mostrar el precio final (más IVA 21%).
print('\nSuma de productos más IVA:')
producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))

total = (producto1 + producto2 + producto3) * 1.21

print('El total más el IVA es igual a $',total, sep='')