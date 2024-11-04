calificaciones = {
    'juan': 10,
    'pedro': 6,
    'yamila': 9,
    'gonzalo': 5,
    'gladys': 7,
    'jimena': 8
}
cantidad_de_notas = 0
acumulador_de_notas = 0
for valor in calificaciones:
    cantidad_de_notas += 1
    acumulador_de_notas += calificaciones[valor]

promedio = acumulador_de_notas / cantidad_de_notas
print(f'Promedio de las calificaciones: {promedio}')