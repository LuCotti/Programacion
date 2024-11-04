contador = 0
numero_minimo = float('inf')

while contador < 4:
    numero = int(input('Ingrese un número: '))
    if numero < numero_minimo:
        numero_minimo = numero
    contador += 1

print('Número mínimo:',numero_minimo)