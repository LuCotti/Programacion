def sumar_naturales(numero: int)-> int:
    if numero == 0:
        return numero
    else:
        return numero + sumar_naturales(numero - 1)

print(sumar_naturales(6))