# Mostrar la suma de los números pares desde el 1 hasta el 10.

# Ejercicio 04
# Luciano Cotti

contador = 0
acumulador_pares = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        acumulador_pares += contador
    print(acumulador_pares)