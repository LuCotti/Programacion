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
# ENTRADA DE DATOS
marca_lamparas = input('Ingrese la marca de lámparas que desea comprar: ')
cantidad_lamparas = int(input('Ingrese la cantidad de lámparas a comprar: '))

# DEFINICIÓN DE VARIABLES
precio_lampara = 800
precio_base_lamparas = cantidad_lamparas * precio_lampara
descuento = 0

# PROCESO
match cantidad_lamparas:
    case 11:
        descuento = 50
    case 10:
        descuento = 50
    case 9:
        descuento = 50
    case 8:
        descuento = 50
    case 7:
        descuento = 50
    case 6:
        descuento = 50
    case 5:
        match marca_lamparas:
            case 'ArgentinaLuz':
                descuento = 40
            case _:
                descuento = 30
    case 4:
        match marca_lamparas:
            case 'ArgentinaLuz':
                descuento = 25
            case 'FelipeLamparas':
                descuento = 25
            case _:
                descuento = 20
    case 3:
        match marca_lamparas:
            case 'ArgentinaLuz':
                descuento = 15
            case 'FelipeLamparas':
                descuento = 10
            case _:
                descuento = 5

precio_con_descuento = precio_base_lamparas * (1 - descuento / 100)

# INFORME DE RESULTADOS
print('Marca de las lámparas compradas:',marca_lamparas)
print('Cantidad de lámparas compradas:',cantidad_lamparas)
print('Precio total sin descuento: $',precio_base_lamparas)
match cantidad_lamparas:
    case 11:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
        descuento_adicional = 5
        precio_con_descuento = precio_base_lamparas * (1 - (descuento + descuento_adicional) / 100)
        print('Descuento adicional obtenido:',descuento_adicional,'%.')
        print('Precio total con descuento adicional: $',precio_con_descuento)
    case 10:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 9:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 8:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 7:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 6:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 5:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 4:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)
    case 3:
        print('Descuento obtenido:',descuento,'%.')
        print('Precio total con descuento: $',precio_con_descuento)