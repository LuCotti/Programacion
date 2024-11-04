'''7. Crear una función que reciba un número y retorne True si el número es primo, False
en caso contrario.'''
def verificar_primo(numero):
    contador_divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador_divisores += 1
    
    if contador_divisores == 2:
        return True
    else:
        return False


for i in range(-1, 12):
    print(f'{i} {verificar_primo(i)}')