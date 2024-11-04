'''13. Especializar las funciones del punto 10, 11, 12 para hacerlas
reutilizables. Agregar validaciones.'''

# USAR EXPRESIONES REGULARES

# Ejercicio 10 opción 1
# def es_entero():
#     dato = input('Ingrese un número entero: ')
#     while dato.isalpha():
#         dato = input('Dato inválido. Ingrese un número entero: ')
#     return print('Es entero')

# es_entero()



# Ejercicio 10 opción 2
# def es_entero():
#     dato = input('Ingrese un número entero: ')
#     try:
#         int(dato)
#         return print('Es entero')
#     except ValueError:
#         dato = input('Dato inválido. Ingrese un número entero: ')

# es_entero()




# Ejercicio 11 opción 1
# def es_flotante():
#     dato = input('Ingrese un número flotante: ')
#     while dato():
#         dato = input('Dato inválido. Ingrese un número entero: ')
#     return print('Es entero')

# es_flotante()


# Ejercicio 11 opción 2
# def es_flotante():
#     dato = input('Ingrese un número flotante: ')
#     try:
#         valor = float(dato)
#         while not valor.is_integer():
#             dato = input('Dato inválido. Ingrese un número flotante: ')
#         return print(dato)
#     except ValueError:
#         es_flotante()

# es_flotante()





# # Ejercicio 12
# def es_cadena(numero):
#         if type(numero) != str:
#                 return print('No es cadena')
#         else:
#                 return print('Es cadena')

# es_cadena('es cado')

