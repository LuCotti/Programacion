file = open('notas_1.txt', 'r+')

texto = file.read() # Todo el contenido del archivo

print(texto)

file.close()