import csv

# Inicializar matriz
matriz = []

# Leer el archivo CSV
archivo = open('datos.csv', 'r')

# Leer el CSV
lector_csv = csv.reader(archivo)
for fila in lector_csv:
    matriz.append(fila)

# Imprimir la matriz
for fila in matriz:
    print(fila)

archivo.close()

