# LISTA
print('LISTA')
lista = ['Luciano', 22, True]
print(lista[0])
lista[0] = 'Ariel'
print(lista[0])
lista = ['Cambio los datos', 'pongo otro dato']
print(lista)

# TUPLA
print('TUPLA')
tupla = ('Luciano', 22, True)
print(tupla[0])
tupla = ('Cambio los datos', 'pongo otro dato')
print(tupla)
# tupla[0] = 'Ariel'
# print(tupla[0]) Devuelve un error ya que no se pueden cambiar los valores de las tuplas.

# CONJUNTO O SET
print('CONJUNTO O SET')
conjunto = {'Luciano', 22, True}
# print(conjunto[0]) Devuelve un error ya que no se puede acceder a los elementos.
print(conjunto)
# Los elementos no tienen un orden
conjunto = {'Cambio los datos', 'pongo otro dato'}
print(conjunto)
# No se admiten datos duplicados
conjunto = {'Cambio los datos', 'pongo otro dato', 'pongo otro dato', 'pongo otro dato'}
print(conjunto)

# DICCIONARIO
print('DICCIONARIO')
dict = {
    'nombre' : 'Luciano Cotti',
    'edad' : 22,
    'estatura' : 1.65
}

print(dict['estatura'])