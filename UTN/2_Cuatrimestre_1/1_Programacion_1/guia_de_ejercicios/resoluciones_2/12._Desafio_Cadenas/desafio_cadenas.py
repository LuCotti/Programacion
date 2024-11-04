lugar_del_crimen = 'CGTTTAATG'
sospechoso_1 = ['Juan Pérez', 'CGGGGCTAAAATTTTTTACGATCG']
sospechoso_2 = ['María Rodríguez', 'AACGTTTAATGTTCTAAGCTGCG']
sospechoso_3 = ['Carlos Sánchez', 'CGGGGCTAAAATTTTTTACGATCG']

def comparar_cadenas(cadena_1: str, cadena_2: str) -> bool:
    son_iguales = True
    if len(cadena_1) != len(cadena_2):
        son_iguales = False
        return son_iguales
    else:
        for i in range(len(cadena_1)):
            if cadena_1[i] != cadena_2[i]:
                son_iguales = False
        
        return son_iguales

# Compararamos las combinaciones de bases nitrogenadas de la muestra encontrada
# con las muestras de los sospechosos.

# sospechoso_1 = comparar_cadenas(lugar_del_crimen, juan_perez)
# sospechoso_2 = comparar_cadenas(lugar_del_crimen, maria_rodriguez)
# sospechoso_3 = comparar_cadenas(lugar_del_crimen, carlos_sanchez)

culpabilidad_1 = comparar_cadenas(lugar_del_crimen, sospechoso_1[1])
culpabilidad_2 = comparar_cadenas(lugar_del_crimen, sospechoso_2[1])
culpabilidad_3 = comparar_cadenas(lugar_del_crimen, sospechoso_3[1])
if not culpabilidad_1 and not culpabilidad_2 and not culpabilidad_3:
    print('SON TODOS INOCENTES.')
else:
    if culpabilidad_1:
        print(sospechoso_1[0])
    elif culpabilidad_2:
        print(sospechoso_2[0])
    elif culpabilidad_3:
        print(sospechoso_3[0])
    else:
        print('ERROR')