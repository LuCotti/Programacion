'''
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

'''

encuestar = "si"
voto_zara = 0
contador_desempleados_starbucks = 0
contador_femenino_zara = 0
contador_masculino_zara = 0
contador_otro_zara = 0

while encuestar == "si":

    nombre_ingresado = input("Ingrese su nombre: ")

    edad_ingresada = int(input("Ingrese su edad: "))
    while edad_ingresada < 18:
        edad_ingresada = int(input("Ingrese nuevamente su edad: "))
    
    genero_ingresado = input("Ingrese su género (Masculino - Femenino - Otro): ")
    while genero_ingresado != "Masculino" and genero_ingresado != "Femenino" and genero_ingresado != "Otro":
        genero_ingresado = input("Ingrese su género nuevamene (Masculino - Femenino - Otro): ")
    
    situacion_laboral = input("Ingrese su situación laboral (Empleado - Desempleado)")
    while situacion_laboral != "Empleado" and situacion_laboral != "Desempleado":
        situacion_laboral = input("Ingrese su situación laboral correctamente (Empleado - Desempleado)")
    
    voto_ingresado = input("Ingrese su voto (STARBUCKS, MCDONALDS, ZARA, KFC): ")
    while voto_ingresado != "STARBUCKS" and voto_ingresado != "MCDONALDS" and voto_ingresado != "ZARA" and voto_ingresado != "KFC":
        voto_ingresado = input("Ingrese su voto correctamente (STARBUCKS, MCDONALDS, ZARA, KFC): ")


# a-Nombre y situación laboral de la persona con mayor edad que voto por Zara.

    if voto_ingresado == "ZARA":
        if voto_zara == 0:
            nombre_mayor_zara = nombre_ingresado
            situacion_laboral_mayor_zara = situacion_laboral
            edad_mayor_zara = edad_ingresada

            voto_zara = 1

        elif edad_mayor_zara < edad_ingresada:
            nombre_mayor_zara = nombre_ingresado
            situacion_laboral_mayor_zara = situacion_laboral
            edad_mayor_zara = edad_ingresada
        

        match genero_ingresado:
            case "Femenino":
                contador_femenino_zara += 1
            case "Masculino":
                contador_masculino_zara += 1
            case _:
                contador_otro_zara += 1
    elif voto_ingresado == "STARBUCKS":
            if situacion_laboral == "Desempleado":
                if edad_ingresada >= 30 and edad_ingresada <= 45:
                    contador_desempleados_starbucks += 1

# b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años.
    if genero_ingresado == "Otro":
        if edad_ingresada > 60 and edad_ingresada < 70:
            nombre_otro_mayor = nombre_ingresado
            voto_otro_mayor = voto_ingresado
    

# c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive.
    
# d-Quien de todos los sexos fue el que mas votó por Zara.

    encuestar = input("¿Desea realizar una nueva encuesta?: (si/no) ")

if contador_femenino_zara > contador_masculino_zara and contador_femenino_zara > contador_otro_zara:
    sexo_mas_votos_zara = "Femenino"

elif contador_masculino_zara > contador_femenino_zara and contador_masculino_zara > contador_otro_zara:
    sexo_mas_votos_zara = "Masculino"

else:
    sexo_mas_votos_zara = "Otro"