# Enunciado:
# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos.
# Informar:
# a. nombre del candidato con más votos.
# b. nombre y edad del candidato con menos votos.
# c. el promedio de edades de los candidatos.
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()

# Luciano Cotti

# REQUISITOS
edad_minima = 25

# CONTADOR Y ACUMULADORES
contador = 0
acumulador_edades = 0
acumulador_votos = 0

while contador < 3:
    # INGRESO DE DATOS
    nombre = input('Ingrese el nombre del jugador: ')
    
    edad = int(input('Ingrese la edad del jugador: '))
    # VALIDACIÓN DE EDAD MÍNIMA
    while edad < edad_minima:
        print('Usted es menor de 25, vuelva a su casa. ¡Siguiente!')
        edad = int(input('Ingrese la edad del jugador: '))
    
    votos = int(input('Ingrese la cantidad de votos del jugador: '))
    # VALIDACIÓN DE VOTOS MÍNIMOS
    while votos < 0:
        votos = int(input('No se puede votar en negativo. Ingrese nuevamente la cantidad de votos del jugador: '))
    
    if contador == 0:
        nombre_votos_maximo = nombre
        votos_maximo = votos
        
        nombre_votos_minimo = nombre
        edad_votos_minimo = edad
        votos_minimo = votos
    
    elif votos > votos_maximo:
        votos_maximo = votos
        nombre_votos_maximo = nombre
    elif votos < votos_minimo:
        votos_minimo = votos
        nombre_votos_minimo = nombre
        edad_votos_minimo = edad
    
    acumulador_edades += edad
    acumulador_votos += votos
    contador += 1

# CÁLCULO DEL PROMEDIO DE LAS EDADES
promedio_edades = acumulador_edades / contador



# A. MOSTRAR EL NOMBRE DEL CANDIDATO CON MÁS VOTOS.
print(f'El candidato con más votos es {nombre_votos_maximo}.')

# B. MOSTRAR EL NOMBRE Y LA EDAD DEL CANDIDATO CON MENOS VOTOS.
print(f'El candidato con menos votos es {nombre_votos_minimo} de {edad_votos_minimo} años.')

# C. MOSTRAR EL PROMEDIO DE LAS EDADES.
print(f'El promedio de las edades de los candidatos es de {promedio_edades} años.')

# D. MOSTRAR EL TOTAL DE LOS VOTOS EMITIDOS.
print(f'Se emitieron {acumulador_votos} votos en total.')