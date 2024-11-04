'''
CASO INVESTIGACIÓN CRIMINAL: CSI UTN
Se ha encontrado una muestra de ADN en el lugar de un crimen,
que contiene la siguiente secuencia de bases nitrogenadas:
“CGTTTAATG”. La investigación ha revelado tres posibles
sospechosos que estaban cerca de la escena del crimen, cada uno
con su propia muestra de ADN:
● Juan Pérez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
● María Rodríguez
Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
● Carlos Sánchez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
Para resolver el caso, nos piden que desarrollemos un programa
que compare las combinaciones de bases nitrogenadas de la
muestra encontrada con las muestras de los sospechosos.
Mostrar el nombre por pantalla en caso de encontrar al asesino, o
la leyenda “SON TODOS INOCENTES”
'''

def csi_utn():

    resultado = "Son todos inocentes"
    nitrogenada_culpable = "CGTTTAATG"
    muestras = ["CGGGGCTAAAATTTTTTACGATCG","AACGTTTAATGTTCTAAGCTGCG","CGGGGCTAAAATTTTTTACGATCG"]
    sospechosos = ["Juan Pérez","María Rodríguez","Carlos Sánchez"]

    for i in range(len(muestras)):
        if contar_subcadenas(nitrogenada_culpable,muestras[i]) > 0:
            resultado = "El culpable es " + sospechosos[i]
    
    print(resultado)

def contar_subcadenas(subcadena,cadena):
    total = 0

    for i in range(len(cadena)):
        if subcadena == cadena[i:i+len(subcadena)]:
            total +=1

    return total

csi_utn()