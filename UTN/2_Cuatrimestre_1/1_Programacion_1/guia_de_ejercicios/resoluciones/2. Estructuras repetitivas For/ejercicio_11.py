'''11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
número ingresado. Informar cuántos números primos se encontraron.'''

numero = int(input('Ingrese un número: '))
contador_primos = 0

for i in range(2, numero + 1):
    contador_divisores = 0
    
    for o in range(2, i):
        resto = i % o
        if resto == 0:
            contador_divisores += 1
    
    if numero < 2:
        pass
    elif contador_divisores > 0:
        pass
    else:
        contador_primos += 1
        print(i)

print(f'Cantidad de primos: {contador_primos}')