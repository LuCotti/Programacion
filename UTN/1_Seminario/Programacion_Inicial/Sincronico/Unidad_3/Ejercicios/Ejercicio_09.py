# Ejercicio 9
# Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por
# consola(input), transformar en número y mostrar el importe actualizado con un descuento
# del 20% utilizando print.

# Luciano Cotti

importe = int(input('Ingrese el importe: '))
descuento = 20

importe_actualizado = importe * (1 - descuento / 100)

print('El importe con descuento del 20% es igual a $',importe_actualizado)