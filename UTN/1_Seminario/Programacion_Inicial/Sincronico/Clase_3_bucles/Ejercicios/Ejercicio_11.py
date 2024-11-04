# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

# Ejercicio 11
# Luciano Cotti

nota = int(input('Ingrese la nota: '))

while nota < 1 or nota > 10:
    nota = int(input('La nota debe estar comprendida entre 1 y 10 inclusive. Ingrese la nota nuevamente: '))