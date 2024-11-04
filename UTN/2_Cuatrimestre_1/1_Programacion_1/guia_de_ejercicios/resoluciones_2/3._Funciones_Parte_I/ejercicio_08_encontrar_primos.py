'''8. Crear una función que (utilizando la función del punto 11 de la guía de For), muestre
todos los números primos comprendidos entre entre la unidad y un número
ingresado como parámetro. La función retorna la cantidad de números primos
encontrados.'''


numero_ingresado = int(input('Ingrese un número: '))
def encontrar_primos(numero):
    contador_primos = 0
    
    for i in range(1, numero + 1):
        contador_divisores = 0
        for j in range(1, i + 1):
            if i % j == 0:
                contador_divisores += 1
        
        if contador_divisores == 2:
            contador_primos += 1
            print(i)
    
    return contador_primos


print(f'Cantidad de números primos encontrados: {encontrar_primos(numero_ingresado)}')