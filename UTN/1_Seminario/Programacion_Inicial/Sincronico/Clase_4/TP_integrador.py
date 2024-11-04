"""

Se realiza un estudio de mercado para determinar cuál será la nueva franquicia 
que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes:
    STARBUCKS
    Zara
    MCDONALDS
    Bershka
    KFC

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, 
con el propósito de conocer cuáles son los gustos de los encuestados.

Datos a ingresar:
    Nombre del encuestado
    Edad (no menor a 18)
    Género (Masculino - Femenino - Otro)
    Voto (STARBUCKS, MCDONALDS, ZARA, KFC)
    Situación Laboral (Empleado - Desempleado)



Consignas:
    a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
    b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
    c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
    d-Quien de todos los sexos fue el que mas votó por Zara.
"""

# Luciano Cotti

votos_zara = 0
seguir_encuestando = True

# a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
edad_mayor = 0
nombre_voto_por_zara = ''
situacion_laboral_voto_por_zara = ''

# b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
nombre_otro_60_a_70_años = ''
voto_otro_60_a_70_años = ''

# c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
contador_desempleados_voto_starbucks_30_a_45_años = 0

# d-Quien de todos los sexos fue el que mas votó por Zara.
contador_masculino_voto_zara = 0
contador_femenino_voto_zara = 0
contador_otro_voto_zara = 0


while seguir_encuestando == True:
    # INGRESO Y VALIDACIÓN DE DATOS
    nombre_encuestado = input('Ingrese su nombre: ')
    
    edad_encuestado = int(input('Ingrese su edad: '))
    while edad_encuestado < 18:
        edad_encuestado = int(input('Debe ser mayor de 18 años. Ingrese su edad nuevamente: '))
    
    genero_encuestado = input('Ingrese su género (Masculino - Femenino - Otro): ')
    while genero_encuestado != 'Masculino' and genero_encuestado != 'Femenino' and genero_encuestado != 'Otro':
        genero_encuestado = input('Dato inválido. Ingrese su género nuevamente (Masculino - Femenino - Otro): ')
    
    voto_encuestado = input('Ingrese su voto (STARBUCKS, MCDONALDS, ZARA, BERSHKA, KFC): ')
    while voto_encuestado != 'STARBUCKS' and voto_encuestado != 'MCDONALDS' and voto_encuestado != 'ZARA' and voto_encuestado != 'BERSHKA' and voto_encuestado != 'KFC':
        voto_encuestado = input('Dato inválido. Ingrese su voto nuevamente (STARBUCKS, MCDONALDS, ZARA, BERSHKA, KFC): ')
    
    situacion_laboral_encuestado = input('Ingrese su situación laboral (Empleado - Desempleado): ')
    while situacion_laboral_encuestado != 'Empleado' and situacion_laboral_encuestado != 'Desempleado':
        situacion_laboral_encuestado = input('Dato inválido. Ingrese su situación laboral nuevamente (Empleado - Desempleado): ')
    
    
    
    # a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
    if voto_encuestado == 'ZARA':
        if votos_zara == 0:
            edad_mayor = edad_encuestado
            nombre_voto_por_zara = nombre_encuestado
            situacion_laboral_voto_por_zara = situacion_laboral_encuestado
            votos_zara = 1
        elif edad_encuestado > edad_mayor:
            edad_mayor = edad_encuestado
            nombre_voto_por_zara = nombre_encuestado
            situacion_laboral_voto_por_zara = situacion_laboral_encuestado
        
        # c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
    elif voto_encuestado == 'STARBUCKS':
        if edad_encuestado >= 30 and edad_encuestado <= 45:
            if situacion_laboral_encuestado == 'Desempleado':
                contador_desempleados_voto_starbucks_30_a_45_años += 1
    
    # b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
    if genero_encuestado == 'Otro':
        if edad_encuestado >= 60 and edad_encuestado <= 70:
            nombre_otro_60_a_70_años = nombre_encuestado
            voto_otro_60_a_70_años = voto_encuestado
    
    
    # d-Quien de todos los sexos fue el que mas votó por Zara.
    if voto_encuestado == 'ZARA':
        match genero_encuestado:
            case 'Masculino':
                contador_masculino_voto_zara += 1
            case 'Femenino':
                contador_femenino_voto_zara += 1
            case 'Otro':
                contador_otro_voto_zara += 1
    
    
    pregunta_seguir_encuestando = input('¿Desea seguir encuestando? ')
    if pregunta_seguir_encuestando == 'No' or pregunta_seguir_encuestando == 'no' or pregunta_seguir_encuestando == 'NO':
        seguir_encuestando = False

maximo_votos_zara = contador_masculino_voto_zara
sexo_maximo_votos_zara = 'Masculino'

if contador_femenino_voto_zara > contador_masculino_voto_zara and contador_femenino_voto_zara > contador_otro_voto_zara:
    maximo_votos_zara = contador_femenino_voto_zara
    sexo_maximo_votos_zara = 'Femenino'
elif contador_otro_voto_zara > contador_masculino_voto_zara and contador_otro_voto_zara > contador_femenino_voto_zara:
    maximo_votos_zara = contador_otro_voto_zara
    sexo_maximo_votos_zara = 'Otro'



# INFORME DE RESULTADOS
# a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.
if nombre_voto_por_zara != '':
    print(f'{nombre_voto_por_zara}, cuya situación laboral es {situacion_laboral_voto_por_zara}, es la persona de mayor edad que votó por Zara.')
else:
    print('Nadie ha votado por Zara.')


# b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
if nombre_otro_60_a_70_años != '':
    print(f'{nombre_otro_60_a_70_años}, de sexo Otro y de entre 60 y 70 años, ha votado por {voto_otro_60_a_70_años}.')
else:
    print('No se ha encuestado ninguna persona de sexo Otro de entre 60 y 70 años.')


# c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
print(f'{contador_desempleados_voto_starbucks_30_a_45_años} encuestados de entre 30 y 45 años han votado por Starbucks.')


# d-Quien de todos los sexos fue el que mas votó por Zara.
if maximo_votos_zara != 0:
    print(f'El sexo que más votó por Zara es {sexo_maximo_votos_zara}.')
else:
    print('Nadie ha votado por Zara.')