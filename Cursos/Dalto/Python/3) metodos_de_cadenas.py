# Esto es una función:
# dir
print('DIR')
texto = 'hOlA BuEnAs.'
dir = dir(texto)
print(dir)


# Ahora sí vamos con los métodos:
# upper
print('UPPER')
upper = texto.upper()
print(upper)

print('Texto nada que ver...'.upper())


# lower
print('LOWER')
lower = texto.lower()
print(lower)


# capitalize
print('CAPITALIZE')
capitalize = texto.capitalize()
print(capitalize)


# find
print('FIND')
find = texto.find('BuEnAs') # Devuelve la posición de la primer letra. Si no la encuentra, devuelve -1.
print(find)