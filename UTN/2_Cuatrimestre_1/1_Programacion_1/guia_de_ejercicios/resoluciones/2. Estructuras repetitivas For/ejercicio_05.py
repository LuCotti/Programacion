# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
# número 0. Mostrar la suma y el promedio de todos los números.
contador = 0
acumulador = 0

for i in range(10):
    numero = int(input('Ingrese un número (0 para detener): '))
    if numero == 0:
        break
    contador += 1
    acumulador += numero

promedio = acumulador / contador

mensaje = f'''Suma: {acumulador}
Promedio: {promedio}'''

print(mensaje)