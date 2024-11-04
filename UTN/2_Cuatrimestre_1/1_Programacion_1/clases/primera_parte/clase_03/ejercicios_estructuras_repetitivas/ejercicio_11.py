# 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
# número ingresado. Informar cuántos números primos se encontraron.

es_primo = False

numero_evaluado = int(input('Ingrese un número: '))

for numero in range(2, numero_evaluado):
    if numero_evaluado % 2 != 0:
        es_primo = True
    if numero_evaluado % 3 != 0:
        es_primo = True
    if numero_evaluado % 4 != 0:
        es_primo = True
    if numero_evaluado % 5 != 0:
        es_primo = True
    if numero_evaluado % 6 != 0:
        es_primo = True
    if numero_evaluado % 7 != 0:
        es_primo = True





if es_primo == True:
    print(f'{numero_evaluado} es primo.')
else:
    print(f'{numero_evaluado} no es primo.')
    
    
    
    




# Función de un compañero
# def es_primo(numero_evaluado):
#     es_primo = True
    
#     if numero_evaluado <= 1:
#         es_primo = False

#     for i in range(2, numero_evaluado):
#         if numero_evaluado % i == 0:
#             es_primo = False
#     return es_primo