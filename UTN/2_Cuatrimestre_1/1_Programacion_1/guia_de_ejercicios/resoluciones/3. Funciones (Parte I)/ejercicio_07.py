# 7. Crear una función que reciba un número y retorne True si el número es
# primo, False en caso contrario.

def primo(numero):
    contador = 0
    for i in range(2, numero):
        resto = numero % i
        if resto == 0:
            contador += 1
    
    if numero < 2:
        return False
    elif contador > 0:
        return False
    else:
        return True

print(primo(11))