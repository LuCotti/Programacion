################################# CONSIGNAS ##################################
'''UTN Technologies, una reconocida software factory se encuentra en la
búsqueda de ideas para su próximo desarrollo en Python, que promete
revolucionar el mercado.

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
################################# RESOLUCIÓN #################################
# Punto 1
contador_1 = 0

# Punto 2
contador_2 = 0

# Punto 3
bandera_3 = False

# Bucle
for i in range(10):
    nombre_encuestado = input('Ingrese su nombre: ')
    
    edad_encuestado = int(input('Ingrese su edad (no menor a 18): '))
    while edad_encuestado < 18:
        edad_encuestado = int(input('Dato inválido. Ingrese nuevamente su edad (no menor a 18): '))
    
    genero_encuestado = input('Ingrese su género (Masculino - Femenino - Otro): ')
    while genero_encuestado != 'Masculino' and genero_encuestado != 'Femenino' and genero_encuestado != 'Otro':
        genero_encuestado = input('Dato inválido. Ingrese nuevamente su género (Masculino - Femenino - Otro): ')
    
    voto_encuestado = input('Ingrese su voto (IA, RV/RA, IOT): ')
    while voto_encuestado != 'IA' and voto_encuestado != 'RV/RA' and voto_encuestado != 'IOT':
        voto_encuestado = input('Dato inválido. Ingrese nuevamente su voto (IA, RV/RA, IOT): ')
    
    # Punto 1
    if genero_encuestado == 'Masculino':
        if voto_encuestado == 'IOT' or voto_encuestado == 'IA':
            if edad_encuestado >= 25 and edad_encuestado <= 50:
                contador_1 += 1
        
        # Punto 3
        if bandera_3 == False:
            nombre_3 = nombre_encuestado
            edad_3 = edad_encuestado
            voto_3 = voto_encuestado
            bandera_3 = True
        elif edad_encuestado > edad_3:
            nombre_3 = nombre_encuestado
            edad_3 = edad_encuestado
            voto_3 = voto_encuestado
    
    # Punto 2
    if voto_encuestado != 'IA':
        if genero_encuestado != 'Femenino':
            if edad_encuestado >= 33 and edad_encuestado <= 40:
                contador_2 += 1
    

# Punto 2
porcentaje_2 = contador_2 * 10

mensaje = f'''1. Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {contador_1}
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje_2} %
{nombre_3} es el votante de {voto_3} de género masculino y mayor edad.'''

print(mensaje)