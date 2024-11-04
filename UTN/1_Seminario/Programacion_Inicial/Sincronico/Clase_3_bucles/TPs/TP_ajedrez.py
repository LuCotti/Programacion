# TP Ajedrez.

# De los jugadores participantes en un torneo de ajedrez, se registra:

# nombre
# la edad (mayor de 10 años)
# la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.

# Informar:
# a. Nombre del jugador con más partidas ganadas.
# b. Nombre y edad del jugador con menos partidas ganadas.
# c. El promedio de edades de los jugadores.
# d. El total de partidas ganadas.

# Luciano Cotti

# INGRESO DE DATOS
total_edades = 0
total_victorias = 0
ingresar_mas_jugadores = True
contador = 0

while ingresar_mas_jugadores == True:
    if contador == 0:
        nombre = input('Ingrese su nombre: ')
        nombre_ganador = nombre
        nombre_perdedor = nombre
        edad = int(input('Ingrese su edad: '))
        edad_ganador = edad
        edad_perdedor = edad
        total_edades += edad
        
        # Filtro de edad (10 años).
        while edad < 10:
            print('Solo pueden participar mayores de 10 años. Retírese, por favor.')
            nombre = input('Ingrese su nombre: ')
            nombre_ganador = nombre
            nombre_perdedor = nombre
            edad = int(input('Ingrese su edad: '))
            edad_ganador = edad
            edad_perdedor = edad
            total_edades = 0
            total_edades += edad
        victorias = int(input('¿Cuántas partidas ha ganado en el torneo? '))
        victorias_ganador = victorias
        victorias_perdedor = victorias
        total_victorias += victorias
        # Filtro de victorias (mayores a 0).
        while victorias < 0:
            print('No se pueden ingresar números negativos.')
            victorias = int(input('¿Cuántas partidas ha ganado en el torneo? '))
            victorias_ganador = victorias
            victorias_perdedor = victorias
            total_victorias = 0
            total_victorias += victorias
    else:
        nombre_provisorio = input('Ingrese su nombre: ')
        edad_provisoria = int(input('Ingrese su edad: '))
        total_edades += edad_provisoria
        while edad_provisoria < 10:
            total_edades -= edad_provisoria
            print('Solo pueden participar mayores de 10 años. Retírese, por favor.')
            nombre_provisorio = input('Ingrese su nombre: ')
            edad_provisoria = int(input('Ingrese su edad: '))
            total_edades += edad_provisoria
        victorias_provisorias = int(input('¿Cuántas partidas ha ganado en el torneo? '))
        total_victorias += victorias_provisorias
        while victorias_provisorias < 0:
            total_victorias -= victorias_provisorias
            print('No se pueden ingresar números negativos.')
            victorias_provisorias = int(input('¿Cuántas partidas ha ganado en el torneo? '))
            total_victorias += victorias_provisorias
        
        # Definición de ganador y perdedor.
        if victorias_provisorias > victorias:
            nombre_ganador = nombre_provisorio
            edad_ganador = edad_provisoria
            victorias_ganador = victorias_provisorias
        elif victorias_provisorias < victorias:
            nombre_perdedor = nombre_provisorio
            edad_perdedor = edad_provisoria
            victorias_perdedor = victorias_provisorias
    
    
    seguir_ingresando_jugadores = input('¿Desea ingresar más jugadores? ')
    if seguir_ingresando_jugadores == 'no' or seguir_ingresando_jugadores == 'No' or seguir_ingresando_jugadores == 'NO':
        ingresar_mas_jugadores = False
    contador += 1

promedio_edades = total_edades / contador

# Informe de resultados
print('El jugador con más partidas ganadas es',nombre_ganador)
print('El jugador con menos partidas ganadas es',nombre_perdedor,'de',edad_perdedor,'años')
print('El promedio de las edades es',promedio_edades)
print('En el torneo han habido',total_victorias,'partidas ganadas en total')