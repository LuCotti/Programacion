file = open('notas_1.txt', 'w',) # Apertura del archivo
# Escritura línea a línea
file.write('Primera nota\n')
file.write('segunda nota\n')
file.write('tercera nota\n')
# Escritura por medio de lista
notas = ['Cuarta nota\n', 'Quinta nota\n']
file.writelines(notas)
print('Archivo creado!')
file.close() # Cierre del archivo