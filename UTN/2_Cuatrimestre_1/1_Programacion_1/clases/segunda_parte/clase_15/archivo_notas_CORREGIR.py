'''
Implementar un programa simple que maneje un archivo de notas.
Este programa debe permitir al usuario agregar, leer y eliminar
notas de un archivo de texto.
'''
# from Package_Input.Input import *
# from Package_Input.Validate import *
def mostrar_menu():
    print('\n---- Gestor de notas ----')
    print('1. Agregar nota.')
    print('2. Leer notas.')
    print('3. Eliminar nota.')
    print('4. Salir.')

def agregar_nota():
    nota_ingresada = input('Ingrese la nota: ')
    archivo = open('notas_2.txt', 'a')
    archivo.write(nota_ingresada + '\n')
    print('La nota ha sido agregada con éxito.')
    archivo.close()

def leer_notas():
    print('---- Notas ----\n')
    archivo = open('notas_2.txt', 'r')
    notas = archivo.readlines() # Lista de notas
    if len(notas) == 0:
        print('No hay notas en el archivo.')
    else:
        for i in range(len(notas)):
            print(f'{i + 1}: {notas[i]}')
    archivo.close()

def eliminar_nota():
    leer_notas() # Muestro todas las notas para que elija cuál va a eliminar.
    num_nota = int(input('Ingrese el número de nota a eliminar: '))
    archivo = open('notas_2.txt', 'w+')
    notas = archivo.readlines()
    
    if 1 <= num_nota <= len(notas):
        del notas[num_nota - 1]
        archivo.writelines(notas)
    else:
        print('Número de nota inválido.')




while True:
    mostrar_menu()
    opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
    
    match opcion_ingresada:
        case '1':
            agregar_nota()
        case '2':
            leer_notas()
        case '3':
            eliminar_nota()
        case '4':
            break
        case _:
            print('La opción ingresada no existe.')