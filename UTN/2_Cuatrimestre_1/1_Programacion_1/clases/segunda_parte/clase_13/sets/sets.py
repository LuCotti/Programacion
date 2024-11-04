# Crear un set vacío
conjunto = set()

# Crear un set con elementos ya definidos
frutas = {'manzana', 'banana', 'cereza', 'banana'}
print(frutas)

# Operaciones básicas
frutas.add('Kiwi') # Agregar un elemento
frutas.discard('cereza') # Elimina si existe, si no existe no da error.
frutas.remove('banana') # Elimina si existe, si no existe avisa
print(frutas)
frutas.clear() # Vaciamos el set

# Operaciones de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 7, 8}

union = set1 | set2 | set3 # Unión de dos sets
print(union)

diferencia = set1 - set2 # Diferencia de dos sets
print(diferencia)

interseccion = set1 & set2 # Intersección de dos sets
print(interseccion)

diferencia_simetrica = set1 ^ set2
print(diferencia_simetrica)

# Pertenencia
print(1 in set1) # True
print(10 in set1) # False
print(1 not in set1) # False
print(10 not in set1) # True