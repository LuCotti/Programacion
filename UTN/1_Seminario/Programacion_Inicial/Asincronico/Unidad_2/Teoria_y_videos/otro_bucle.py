numeros_pares = 0
numeros_impares = 0

numero = int(input('Ingrese un número entero (0 para detener): '))

while numero != 0:
    if numero % 2 == 1:
        numeros_impares += 1
    else:
        numeros_pares += 1
    numero = int(input('Ingrese un número entero (0 para detener): '))

print(f'''RESULTADOS:
Números pares: {numeros_pares}
Números impares: {numeros_impares}''')