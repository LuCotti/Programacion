'''3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.'''
lista = [-1, 2, 3, 4]
def multiplicar_lista(lista: list)-> int:
    total = 1
    for i in range(len(lista)):
        total *= lista[i]
    
    return total

print(multiplicar_lista(lista))