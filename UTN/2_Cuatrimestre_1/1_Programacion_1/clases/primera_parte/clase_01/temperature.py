temperatura_farenheit = float(input('Ingrese la temperatura en ºF: '))

temperatura_celsius = (temperatura_farenheit - 32) / 1.8

mensaje = f'La temperatura ingresada en ºF es equivalente a {temperatura_celsius} ºC.'

print(mensaje)