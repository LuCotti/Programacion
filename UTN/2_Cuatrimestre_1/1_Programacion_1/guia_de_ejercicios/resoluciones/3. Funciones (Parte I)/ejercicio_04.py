# 4. Crea una función que verifique si un número dado es par o impar. La
# función retorna True si el número es par, False en caso contrario.

def emparejar(numero):
    resto = numero % 2
    if resto == 0:
        return True
    else:
        return False

print(emparejar(4))