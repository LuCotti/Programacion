def menosuno(numero):
    if numero == -1:
        return numero
    else:
        print(numero)
        return menosuno(numero - 1)

menosuno(5)