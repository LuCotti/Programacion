# Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento
# obtenido.
# Ejercicio 9
# Luciano Cotti

importe = float(input('Ingrese el importe de la compra: '))
descuento = 25
total = importe * (1 - descuento / 100)

mensaje = f'''Total a pagar: {total}.
Descuento obtenido: {descuento}%.'''
print(mensaje)