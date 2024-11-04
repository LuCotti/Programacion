# Ejercicio 10
# Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el
# usuario por consola, transformarlos en números y mostrar el importe actualizado con el
# descuento utilizando print.

# Luciano Cotti

importe = int(input('Ingrese el importe: '))
descuento = int(input('Ingrese el descuento: '))

importe_actualizado = importe * (1 - descuento / 100)

print('El importe con eldescuento ingresado es igual a $',importe_actualizado)