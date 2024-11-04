contador = 0
numero_maximo = float('-inf')

while contador < 4:
    numero = int(input('Ingrese un número: '))
    if numero > numero_maximo:
        numero_maximo = numero
    contador += 1

print('Número máximo:',numero_maximo)