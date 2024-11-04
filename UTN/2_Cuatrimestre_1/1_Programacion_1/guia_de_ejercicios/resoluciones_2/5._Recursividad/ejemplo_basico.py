def cascada(numero: int):
    if numero >= 0:
        print(numero)
        cascada(numero - 1)
    else:
        return numero

cascada(100)