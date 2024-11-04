# Lista de 100 calificaciones (puedes reemplazar estos valores con los tuyos)
calificaciones = [85, 90, 78, 92, 86]

# Inicializar la variable suma en 0
suma = 0

# Ciclo for para acceder a las calificaciones por su índice y sumarlas
for i in range(len(calificaciones)):
    suma += calificaciones[i]

# Calcular el promedio
promedio = suma / len(calificaciones)

print(suma)
print(promedio)