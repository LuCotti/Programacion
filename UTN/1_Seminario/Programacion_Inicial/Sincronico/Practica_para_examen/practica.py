# -------------------------------------------------------------------------------- FORMULARIO --------------------------------------------------------------------------------
# Universidad Tecnológica Nacional
# Facultad Regional Avellaneda
# Apellido(1): Cotti
# Fecha: 8 jul 2024
# Nombre/s(1): Luciano Ariel
# Docente/s(2): Giovanni Lucchetta
# División(1): 306
# Nota(2):
# DNI(1): 43.873.697
# Firma(2):
# Instancia(2)(3): P1
# (1) Campos a completar solo por el alumno.
# (2) Campos a completar solo por el docente.
# (3) Las instancias válidas son: 1º Parcial (P1), Recuperatorio de 1º Parcial (RP1), 2º Parcial (P2), Recuperatorio de 2º Parcial (RP2),
# Final (F), Recuperatorio de Final (RF - Solo válido para seminario de nivelación). Marcar lo que corresponda con una cruz.

# -------------------------------------------------------------------------------- CONSIGNAS --------------------------------------------------------------------------------
# Enunciado/s:
# En un gimnasio se necesita un programa que permita ingresar datos de 20 socios Por cada socio, se ingresa:
# • Nombre completo.
# • Tarifa Base (10000, no se podrá ingresar otro valor)
# • Altura (en centímetros, mayor a 100 y menor a 250).
# • Peso (en kilogramos, mayor a 30 y menor a 200).
# • Rutina de entrenamiento: Debe elegir entre las opciones "Cardio", "Musculación" o "Funcional".
# Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por
# print):
# Los socios que realicen:
# ● Musculación, tendrán un incremento del 10%.
# ● Cardio, tendrán incremento del 10%.
# ● Funcional, un descuento del 10%
# A. Por el número de DNI del alumno:
#     4. Terminados en 6 o 7:
#     ● Informar la cantidad total de socios que realizan “Musculación” y su altura es inferior a “165”.
#     ● El promedio total recaudado de los socios que realizan “Cardio” y su peso es superior a “80”.
#     ● El nombre y la altura del socio que realiza “Funcional” de mayor peso.
# B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
# C. Los porcentajes de cada tipo de rutina de entrenamiento. Ejemplo: [30% Cardio, 40% Funcional, 30% Musculación]

# -------------------------------------------------------------------------------- RESOLUCIÓN --------------------------------------------------------------------------------
contador_socios = 0

# A. Por el número de DNI del alumno:
#     4. Terminados en 6 o 7:
#     ● Informar la cantidad total de socios que realizan “Musculación” y su altura es inferior a “165”.
contador_musculacion = 0

# A. Por el número de DNI del alumno:
#     4. Terminados en 6 o 7:
#     ● El promedio total recaudado de los socios que realizan “Cardio” y su peso es superior a “80”.
acumulador_cardio = 0

# A. Por el número de DNI del alumno:
#     4. Terminados en 6 o 7:
#     ● El nombre y la altura del socio que realiza “Funcional” de mayor peso.
bandera_funcional = 0

# B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
contador_musculacion_general = 0
contador_cardio_general = 0
contador_funcional_general = 0


# INGRESO DE DATOS
while contador_socios < 20:
    nombre_ingresado = input('Ingrese su nombre completo: ')
    
    tarifa_ingresada = int(input('Ingrese la tarifa base ($10.000): $'))
    while tarifa_ingresada != 10000:
        tarifa_ingresada = int(input('Dato inválido. Ingrese la tarifa base nuevamente ($10.000): $'))
    
    altura_ingresada = int(input('Ingrese su altura (en centímetros, mayor a 100 y menor a 250): '))
    while altura_ingresada < 100 or altura_ingresada > 250:
        altura_ingresada = int(input('Dato inválido. Ingrese su altura nuevamente (en centímetros, mayor a 100 y menor a 250): '))
    
    peso_ingresado = int(input('Ingrese su peso (en kilogramos, mayor a 30 y menor a 200): '))
    while peso_ingresado < 30 or peso_ingresado > 200:
        peso_ingresado = int(input('Dato inválido. Ingrese su peso nuevamente (en kilogramos, mayor a 30 y menor a 200): '))
    
    rutina_ingresada = input('Ingrese su rutina de entrenamiento ("Cardio", "Musculación" o "Funcional"): ')
    while rutina_ingresada != 'Cardio' and rutina_ingresada != 'Musculación' and rutina_ingresada != 'Funcional':
        rutina_ingresada = input('Dato inválido. Ingrese su rutina de entrenamiento nuevamente ("Cardio", "Musculación" o "Funcional"): ')
    
    # A. Por el número de DNI del alumno:
    #     4. Terminados en 6 o 7:
    #     ● Informar la cantidad total de socios que realizan “Musculación” y su altura es inferior a “165”.
    match rutina_ingresada:
        case 'Musculación':
            if altura_ingresada < 165:
                contador_musculacion += 1
            
            # B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
            contador_musculacion_general += 1
        
        # A. Por el número de DNI del alumno:
        #     4. Terminados en 6 o 7:
        #     ● El promedio total recaudado de los socios que realizan “Cardio” y su peso es superior a “80”.
        case 'Cardio':
            if peso_ingresado > 80:
                acumulador_cardio += tarifa_ingresada
            
            # B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
            contador_cardio_general += 1
        
        # A. Por el número de DNI del alumno:
        #     4. Terminados en 6 o 7:
        #     ● El nombre y la altura del socio que realiza “Funcional” de mayor peso.
        case _:
            if bandera_funcional == 0:
                peso_mayor_peso = peso_ingresado
                nombre_mayor_peso = nombre_ingresado
                altura_mayor_peso = altura_ingresada
                bandera_funcional = 1
            
            elif peso_ingresado > peso_mayor_peso:
                peso_mayor_peso = peso_ingresado
                nombre_mayor_peso = nombre_ingresado
                altura_mayor_peso = altura_ingresada
            
            # B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
            contador_funcional_general += 1
    
    
    contador_socios += 1



# CÁLCULOS ADICIONALES
# A. Por el número de DNI del alumno:
#     4. Terminados en 6 o 7:
#     ● El promedio total recaudado de los socios que realizan “Cardio” y su peso es superior a “80”.
promedio_cardio = acumulador_cardio / 20


# B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
if contador_musculacion_general > contador_cardio_general and contador_musculacion_general > contador_funcional_general:
    rutina_mas_elegida = 'Musculación'
elif contador_cardio_general > contador_musculacion_general and contador_cardio_general > contador_funcional_general:
    rutina_mas_elegida = 'Cardio'
else:
    rutina_mas_elegida = 'Funcional'


# C. Los porcentajes de cada tipo de rutina de entrenamiento. Ejemplo: [30% Cardio, 40% Funcional, 30% Musculación]
porcentaje_musculacion = contador_musculacion_general * 100 / 20
porcentaje_cardio = contador_cardio_general * 100 / 20
porcentaje_funcional = contador_funcional_general * 100 / 20



# INFORME DE RESULTADOS
mensaje = f'''Cantidad total de socios que realizan “Musculación” y su altura es inferior a “165”: {contador_musculacion}.
Promedio total recaudado de los socios que realizan “Cardio” y su peso es superior a “80”: ${promedio_cardio}.
{nombre_mayor_peso}, de {altura_mayor_peso} cm de altura es el socio de mayor peso que realiza "Funcional".
El tipo de rutina de entrenamiento más elegida fue: {rutina_mas_elegida}.
Porcentajes de cada tipo de rutina de entrenamiento: {porcentaje_musculacion}% Musculación, {porcentaje_cardio}% Cardio, {porcentaje_funcional}% Funcional.'''

print(mensaje)