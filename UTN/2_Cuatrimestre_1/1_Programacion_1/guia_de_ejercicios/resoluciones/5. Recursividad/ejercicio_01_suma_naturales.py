'''1. Realizar una función recursiva que calcule la suma de los primeros
números naturales:
def sumar_naturales(numero: int)->int:
    pass'''
    
def sumar_naturales(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

print(sumar_naturales(7))