# C. ingresar tres precios de productos, sumarlos y mostrar el precio final (más IVA 21%).
producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))

total = (producto1 + producto2 + producto3) * 1.21

print('El total más el IVA es igual a $',total, sep='')