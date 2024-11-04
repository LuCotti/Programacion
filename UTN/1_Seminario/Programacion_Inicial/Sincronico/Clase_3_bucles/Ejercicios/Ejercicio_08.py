# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# Ejercicio 08
# Luciano Cotti

contador = 0

while contador < 10:
    numero = int(input('Ingrese un número entero: '))
    # if contador == 0:
    #     maximo = numero
    #     minimo = numero
    # elif numero > maximo:
    #     maximo = numero
    # elif numero < minimo:
    #     minimo = numero
    
    if contador == 0 or numero > maximo:
        maximo = numero
    if contador == 0 or numero < minimo:
        minimo = numero
    
    contador += 1

print('Valor máximo ingresado:',maximo,'\nValor mínimo ingresado:',minimo)