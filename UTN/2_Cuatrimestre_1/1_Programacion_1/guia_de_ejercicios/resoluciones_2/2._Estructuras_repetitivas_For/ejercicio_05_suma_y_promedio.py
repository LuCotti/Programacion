'''5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números.'''
suma = 0
contador = 0
for i in range(10):
    numero_ingresado = int(input('Ingrese un número (0 para detener): '))
    if numero_ingresado == 0:
        break
    suma += numero_ingresado
    contador += 1

promedio = suma / contador

mensaje = f'Suma: {suma}\nPromedio: {promedio}'

print(mensaje)