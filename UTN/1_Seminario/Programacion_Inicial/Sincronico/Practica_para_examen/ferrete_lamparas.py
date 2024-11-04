# ----------------------------------------------------------------------------------- CONSIGNAS -----------------------------------------------------------------------------------
# TP Condicionales:
# Ferrete Lámparas

# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las 
# lámparas cuestan $800.

# Se aplicará el siguiente descuento:
# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

# Mostrar por pantalla: 

# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

# Luciano Cotti
# ----------------------------------------------------------------------------------- RESPUESTAS -----------------------------------------------------------------------------------

precio_lampara = 800

cantidad_ingresada = int(input('Ingrese la cantidad de lámparas a comprar: '))
marca_ingresada = input('Ingrese la marca de lámaras a comprar: ')

total_sin_descuento = cantidad_ingresada * precio_lampara

if cantidad_ingresada >= 6:
    descuento = 50
elif cantidad_ingresada == 5:
    match marca_ingresada:
        case 'ArgentinaLuz':
            descuento = 40
        case _:
            descuento = 30
elif cantidad_ingresada == 4:
    match cantidad_ingresada:
        case 'ArgentinaLuz':
            descuento = 25
        case 'FelipeLamparas':
            descuento = 25
        case _:
            descuento = 20
elif cantidad_ingresada == 3:
    match cantidad_ingresada:
        case 'ArgentinaLuz':
            descuento = 15
        case 'FelipeLamparas':
            descuento = 10
        case _:
            descuento = 5
else:
    descuento = 0

total_con_descuento = total_sin_descuento * (1 - descuento / 100)

if total_con_descuento > 4000:
    descuento_adicional = 5
    total_con_descuento_adicional = total_con_descuento * (1 - descuento_adicional / 100)



mensaje_sin_descuento = f'''Marca de lámparas: {marca_ingresada}.
Cantidad de lámparas: {cantidad_ingresada}.
Total sin descuento: {total_sin_descuento}.'''

mensaje_con_descuento = f'\nDescuento obtenido: {descuento}%.'

mensaje_con_descuento_adicional = f'\nDescuento adicional: {descuento_adicional}.'