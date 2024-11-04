# Empresa de Camiones:
# Para el departamento de logística:
# A. Es necesario saber la cantidad de camiones que harían falta para transportar los
# materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la
# cantidad de toneladas necesarias de materiales a transportar. El programa deberá
# informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por
# viaje 3500kg.
# B. A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones
# para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo
# (en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir
# a una velocidad máxima y constante de 90 km/h.

# Luciano Cotti

# DEFINICIÓN DE VARIABLES
capacidad_por_camion = 3.5 # Toneladas
velocidad_camion = 90 # km/h

# INGRESO DE DATOS
toneladas_a_transportar = int(input('Ingrese la cantidad de toneladas a transportar: '))
kilometros_a_recorrer = int(input('Ingrese la cantidad de kilómetros a recorrer: '))

# CÁLCULOS
cantidad_de_camiones = int(toneladas_a_transportar / capacidad_por_camion)
resto_camiones = toneladas_a_transportar % capacidad_por_camion
if resto_camiones > 0:
    cantidad_de_camiones += 1
tiempo_de_viaje = int(kilometros_a_recorrer / velocidad_camion)

# INFORME DE RESULTADOS
print(f'Se necesitarán {cantidad_de_camiones} camiones para transportar {toneladas_a_transportar} toneladas.')
print(f'Cada camión tardará {tiempo_de_viaje} horas en llegar a la obra.')