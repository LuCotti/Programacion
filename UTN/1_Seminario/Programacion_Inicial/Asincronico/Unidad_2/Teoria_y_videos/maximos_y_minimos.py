contador = 0
numero_maximo = float('-inf')
numero_minimo = float('inf')

while contador < 4:
    numero = int(input('Ingrese un número: '))
    if numero > numero_maximo:
        numero_maximo = numero
    if numero < numero_minimo:
        numero_minimo = numero
    contador += 1

print('Número máximo:',numero_maximo)
print('Número mínimo:',numero_minimo)