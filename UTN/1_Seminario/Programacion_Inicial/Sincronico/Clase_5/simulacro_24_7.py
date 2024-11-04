# Una empresa internacional está realizando un estudio de mercado para decidir cuál será la nueva plataforma de entretenimiento que se lanzará en el mercado argentino y en la cual
# invertirán.
# Las posibles franquicias son las siguientes: Hulu, Vix+ o CODA.

# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
# Se ingresa de cada encuestado:

# Nombre
# Edad (no menor a 18)
# Tiene suscripción a algún servicio de streaming (sí-no)
# Género (Masculino - Femenino - No binario - Otro)
# Voto (Hulu, Vix+, CODA)
# Se solicita realizar las siguientes búsquedas:

# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por Hulu.
# 2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
# 3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
# 4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
# 5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.

# Luciano Cotti
seguir_encuestando = 'si'

# DEFINICIÓN DE CONTADORES Y ACUMULADORES
# 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por Hulu.
contador_masculino = 0

# 2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
bandera_hulu = 0

# 3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
contador_coda = 0
contador_coda_25_años = 0

# 4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
contador_vix = 0
acumulador_edades = 0

# 5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.
contador_hulu_general = 0
contador_vix_general = 0
contador_coda_general = 0


# INGRESO Y VALIDACIÓN DE DATOS, Y LÓGICA DEL PROGRAMA
while seguir_encuestando == 'si':
    nombre_ingresado = input('Ingrese su nombre: ')
    
    edad_ingresada = int(input('Ingrese su edad: '))
    while edad_ingresada < 18:
        edad_ingresada = int(input('Debe ser mayor a 18. Ingrese su edad nuevamente: '))
    
    suscripcion_ingresada = input('¿Tiene suscripción a algún servicio de streaming? (sí-no) ')
    while suscripcion_ingresada != 'si' and suscripcion_ingresada != 'no':
        suscripcion_ingresada = input('Respuesta inválida. ¿Tiene suscripción a algún servicio de streaming? (¡SI-NO!) ')
    
    genero_ingresado = input('Ingrese su género (Masculino - Femenino - No binario - Otro): ')
    while genero_ingresado != 'Masculino' and genero_ingresado != 'Femenino' and genero_ingresado != 'No binario' and genero_ingresado != 'Otro':
        genero_ingresado = input('Dato inválido. Ingrese su género (Masculino - Femenino - No binario - Otro): ')
    
    voto_ingresado = input('Ingrese su voto (Hulu, Vix+, CODA): ')
    while voto_ingresado != 'Hulu' and voto_ingresado != 'Vix+' and voto_ingresado != 'CODA':
        voto_ingresado = input('Dato inválido. Ingrese su voto nuevamente (Hulu, Vix+, CODA): ')
    
    
    
    # 1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por Hulu.
    if genero_ingresado == 'Masculino':
        if edad_ingresada >= 18 and edad_ingresada <= 25 or edad_ingresada >= 36 and edad_ingresada <= 49:
            contador_masculino += 1
        elif voto_ingresado == 'Hulu':
            contador_masculino += 1
    
    # 2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
    if voto_ingresado == 'Hulu':
        if bandera_hulu == 0:
            nombre_menor_hulu = nombre_ingresado
            genero_menor_hulu = genero_ingresado
            edad_menor_hulu = edad_ingresada
            bandera_hulu = 1
        elif edad_ingresada < edad_menor_hulu:
            nombre_menor_hulu = nombre_ingresado
            genero_menor_hulu = genero_ingresado
            edad_menor_hulu = edad_ingresada
    
    # 3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
    
    if voto_ingresado == 'CODA':
        contador_coda += 1
        if edad_ingresada >= 25:
            contador_coda_25_años += 1
    
    # 4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
    if voto_ingresado == 'Vix+':
        contador_vix += 1
        acumulador_edades += edad_ingresada
    
    # 5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.
    match voto_ingresado:
        case 'Hulu':
            contador_hulu_general += 1
        case 'Vix+':
            contador_vix_general += 1
        case 'CODA':
            contador_coda_general += 1
    
    
    
    seguir_encuestando = input('¿Desea seguir encuestando? ')


# CÁLCULOS
# 3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
porcentaje_coda = contador_coda * 100 / contador_coda_25_años

# 4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
if contador_vix != 0:
    promedio_edades_vix = acumulador_edades / contador_vix

# 5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.
franquicia_mas_votada = 'Hulu'

if contador_vix_general > contador_hulu_general and contador_vix_general > contador_coda_general:
    franquicia_mas_votada = 'Vix+'
else:
    franquicia_mas_votada = 'CODA'



# INFORME DE RESULTADOS
mensaje = f'''Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por Hulu: {contador_masculino}.
{nombre_menor_hulu}, de sexo {genero_menor_hulu} y {edad_menor_hulu} años es la persona de menor edad que ha votado por Hulu.
El {porcentaje_coda}% de los encuestados son mayores de 25 años y han votado por CODA.
El promedio de edad de los encuestados que votaron por Vix+ es igual a: {promedio_edades_vix}.
La franquicia más votada es {franquicia_mas_votada}.'''

print(mensaje)