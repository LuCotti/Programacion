'''8. Crear una función que (utilizando la función del punto 11 de la guía de
For), muestre todos los números primos comprendidos entre entre la unidad y
un número ingresado como parámetro. La función retorna la cantidad de
números primos encontrados.
'''

def primo(numero):
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
    
    return print(f'Cantidad de primos: {contador_primos}')

primo(7)