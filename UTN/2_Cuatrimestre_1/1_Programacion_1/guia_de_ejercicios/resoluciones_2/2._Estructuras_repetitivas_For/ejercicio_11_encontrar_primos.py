'''11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
número ingresado. Informar cuántos números primos se encontraron.'''
contador_primos = 0
numero_ingresado = int(input('Ingrese un número: '))

for i in range(1, numero_ingresado + 1):
    contador_divisores = 0
    for j in range(1, i + 1):
        if i % j == 0:
            contador_divisores += 1
    
    if contador_divisores == 2:
        contador_primos += 1
        print(i)

print(f'Se encontraron {contador_primos} números primos.')