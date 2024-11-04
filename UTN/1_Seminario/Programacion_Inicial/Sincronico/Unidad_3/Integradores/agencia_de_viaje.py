# Agencia de viaje:
# Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por
# kilo de pasajero es 1000 pesos.Se ingresan todos los datos por PROMPT los datos a solicitar
# de dos personas son: nombre, edad y peso
# Se pide armar el siguiente mensaje:
# "Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos ,
# el promedio de edad es 33 y su viaje vale 140000 pesos "

# Luciano Cotti

precio_por_kg_pasajero = 1000

nombre1 = input('Ingrese el nombre de la primera persona: ')
edad1 = int(input('Ingrese el edad de la primera persona: '))
peso1 = int(input('Ingrese el peso de la primera persona [kg]: '))
nombre2 = input('Ingrese el nombre de la segunda persona: ')
edad2 = int(input('Ingrese el edad de la segunda persona: '))
peso2 = int(input('Ingrese el peso de la segunda persona [kg]: '))

suma_pesos = peso1 + peso2
promedio_edades = (edad1 + edad2) / 2
precio_pasajero1 = peso1 * precio_por_kg_pasajero
precio_pasajero2 = peso2 * precio_por_kg_pasajero
precio_total = precio_pasajero1 + precio_pasajero2

print(f'Hola {nombre1} y {nombre2}, sus pesos son {peso1} kilos y {peso2} kilos respectivamente, sumados da {suma_pesos} kilos, el promedio de edad es {promedio_edades} y su viaje vale {precio_total} pesos.')
