from class_boligrafo import *

mi_boligrafo_1 = Boligrafo('fino', 'azul')
mi_boligrafo_2 = Boligrafo('grueso', 'rojo')
mi_boligrafo_3 = Boligrafo('fino', 'negro')
mi_boligrafo_4 = Boligrafo('grueso', 'verde')
mi_boligrafo_5 = Boligrafo('fino', 'amarillo')

lista_boligrafos_1 = [mi_boligrafo_1, mi_boligrafo_2, mi_boligrafo_3, mi_boligrafo_4, mi_boligrafo_5]
lista_boligrafos_2 = []

for i in range(len(lista_boligrafos_1)):
    lista_boligrafos_1[i].mostrar_datos()

bandera_sin_tinta = True
while bandera_sin_tinta:
    for i in range(len(lista_boligrafos_1)):
        lista_boligrafos_1[i].escribir('-')
        if lista_boligrafos_1[i].cantidad_tinta == 0:
            lista_boligrafos_2.append(lista_boligrafos_1.pop(i))
            
            for j in range(len(lista_boligrafos_1)):
                if j == 0:
                    posicion_boligrafo_con_menos_tinta = j
                    boligrafo_con_menos_tinta = lista_boligrafos_1[j]
                elif lista_boligrafos_1[j].cantidad_tinta < boligrafo_con_menos_tinta.cantidad_tinta:
                    posicion_boligrafo_con_menos_tinta = j
                    boligrafo_con_menos_tinta = lista_boligrafos_1[j]
            
            lista_boligrafos_2.append(lista_boligrafos_1.pop(posicion_boligrafo_con_menos_tinta))
            
            bandera_sin_tinta = False
            break

print('Lista 1')
for i in range(len(lista_boligrafos_1)):
    print(lista_boligrafos_1[i].color)
print('\nLista 2')
for i in range(len(lista_boligrafos_2)):
    print(lista_boligrafos_2[i].color)

print('\nRecargamos ambos bolígrafos:')
for i in range(len(lista_boligrafos_2)):
    lista_boligrafos_2[i].recargar(100)










# TEST
# print(f'Cantidad de tinta antes de escribir: {mi_boligrafo_1.cantidad_tinta}')
# mi_boligrafo_1.escribir('0123456789012345678901234567890123456789')
# print(f'Cantidad de tinta después de escribir: {mi_boligrafo_1.cantidad_tinta}')
# mi_boligrafo_1.recargar(110)
# print(f'Cantidad de tinta después de recargar: {mi_boligrafo_1.cantidad_tinta}')
# mi_boligrafo_1.mostrar_datos()

# print(f'Cantidad de tinta antes de escribir: {mi_boligrafo_2.cantidad_tinta}')
# mi_boligrafo_2.escribir('0123456789012345678901234567890123456789')
# print(f'Cantidad de tinta después de escribir: {mi_boligrafo_2.cantidad_tinta}')
# mi_boligrafo_2.recargar(110)
# print(f'Cantidad de tinta después de recargar: {mi_boligrafo_2.cantidad_tinta}')
# mi_boligrafo_2.mostrar_datos()