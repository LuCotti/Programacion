import csv

productos = [
    ['ID','Nombre','Cantidad','Precio'],
[1,'Lapiz',50,0.5],
[2,'Lapicera',100,1.2],
[3,"Cuaderno de 100 hojas, color azul",30,2.5],
[4,'Regla',25,0.8]
]

nombre_archivo = 'productos.csv'

file = open(nombre_archivo, 'w', newline='')
escritor_csv = csv.writer(file) # Writer sabe cómo escribir archivos csv
escritor_csv.writerows(productos) # Escribí la matriz
file.close()

print('El archivo fue creado exitosamente!.')
