#--------------------------------- CONSIGNAS ---------------------------------
'''UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.

Las posibles aplicaciones son las siguientes:
● Inteligencia artificial (IA),
● Realidad virtual/aumentada (RV/RA),
● Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
● nombre del empleado
● edad (no menor a 18)
● género (Masculino - Femenino - Otro)
● tecnologia (IA, RV/RA, IOT)
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.
3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.'''
# -------------------------------- RESPUESTAS --------------------------------
# Contador para finalizar el bucle
contador = 0

# 1. Cantidad de empleados de género masculino que votaron por IOT o IA,
# cuya edad esté entre 25 y 50 años inclusive.
contador_iot_1 = 0
contador_ia_1 = 0

# 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
# género no sea Femenino o su edad se encuentre entre los 33 y 40.
contador_no_ia_2 = 0

# 3. Nombre y tecnología que votó, de los empleados de género masculino con
# mayor edad de ese género.
bandera_mayor = 0


while contador < 10:
    # A) Los datos a ingresar por cada empleado encuestado son:
    # ● nombre del empleado
    # ● edad (no menor a 18)
    # ● género (Masculino - Femenino - Otro)
    # ● tecnologia (IA, RV/RA, IOT)
    nombre_encuestado = input('Ingrese su nombre: ')
    
    edad_encuestado = int(input('Ingrese su edad (no menor a 18): '))
    while edad_encuestado < 18:
        edad_encuestado = int(input('Dato erróneo. Ingrese su edad nuevamente (no menor a 18): '))
    
    genero_encuestado = input('Ingrese su género (Masculino - Femenino - Otro): ')
    while genero_encuestado != 'Masculino' and genero_encuestado != 'Femenino' and genero_encuestado != 'Otro':
        genero_encuestado = input('Dato erróneo. Ingrese su género nuevamente (Masculino - Femenino - Otro): ')
    
    voto_encuestado = input('Ingrese la tecnología (IA, RV/RA, IOT): ')
    while voto_encuestado != 'IA' and voto_encuestado != 'RV/RA' and voto_encuestado != 'IOT':
        voto_encuestado = input('Dato erróneo. Ingrese la tecnología (IA, RV/RA, IOT): ')
    
    # 1. Cantidad de empleados de género masculino que votaron por IOT o IA,
    # cuya edad esté entre 25 y 50 años inclusive.
    if genero_encuestado == 'Masculino':
        if edad_encuestado >= 25 and edad_encuestado <= 50:
            if voto_encuestado == 'IOT':
                contador_iot_1 += 1
            elif voto_encuestado == 'IA':
                contador_ia_1 += 1
    
    # 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
    # género no sea Femenino o su edad se encuentre entre los 33 y 40.
    if voto_encuestado != 'IA':
        if genero_encuestado != 'Femenino' or (edad_encuestado >= 33 and edad_encuestado <= 40):
                contador_no_ia_2 += 1
    
    # 3. Nombre y tecnología que votó, de los empleados de género masculino con
    # mayor edad de ese género.
    if genero_encuestado == 'Masculino':
        if bandera_mayor == 0:
            nombre_mayor = nombre_encuestado
            edad_mayor = edad_encuestado
            voto_mayor = voto_encuestado
            bandera_mayor = 1
        else:
            if edad_encuestado > edad_mayor:
                nombre_mayor = nombre_encuestado
                edad_mayor = edad_encuestado
                voto_mayor = voto_encuestado
    
    contador += 1

# 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
# género no sea Femenino o su edad se encuentre entre los 33 y 40.
porcentaje_no_ia_2 = contador_no_ia_2 * 10



# Informe de resultados
mensaje = f'''Cantidad de empleados de género masculino que votaron por IOT, de entre 25 y 50 años: {contador_iot_1}
Cantidad de empleados de género masculino que votaron por IA, de entre 25 y 50 años: {contador_ia_1}
Porcentaje de empleados que no votaron por IA, de género diferente de Femenino o su edad se encuentra entre los 33 y 40: {porcentaje_no_ia_2}%
{nombre_mayor}, cuyo voto es {voto_mayor}, es el empleado de mayor edad cuyo género es masculino.'''

print(mensaje)