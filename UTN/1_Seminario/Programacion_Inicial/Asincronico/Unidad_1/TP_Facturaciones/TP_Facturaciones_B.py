# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))

promedio = (producto1 + producto2 + producto3) / 3

print('El promedio de los 3 productos es $',promedio, sep='')