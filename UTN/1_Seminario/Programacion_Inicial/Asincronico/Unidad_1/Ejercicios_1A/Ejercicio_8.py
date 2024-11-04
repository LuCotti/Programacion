# Escribe un programa que muestre por consola el resultado de la siguiente operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin los paréntesis?
calculo1 = (10 + 3) * (6+6) # Primero realiza las sumas y luego el producto, dando como resultado 156.
calculo2 = 10 + 3 * 6+6     # Primero realiza el producto y luego las sumas, dando como resultado 34.
print('Con paréntesis: ', calculo1)
print('Sin paréntesis: ', calculo2)