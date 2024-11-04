################################## CONSIGNA ##################################
'''Realizar un menú de opciones en donde el usuario pueda realizar las
siguientes operaciones:

a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Listar todos los números ingresados.
f. Listar todos los números pares.
g. Listar los números de las posiciones impares.
h. Salir

Notas:
● Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario
haya ingresado los datos solicitados.
● Todas las opciones deberán ser programadas en funciones: habrá funciones
específicas (por ejemplo para determinar si un número es positivo o negativo)
y funciones de nivel general (por ejemplo una función que liste los números
pares). Tener en cuenta las características de la programación funcional.
● Las funciones específicas deberán estar en el módulo “Especificas.py”,
mientras que las generales en el módulo “Array_Generales.py”. Todos estos
módulos deben estar integrados en el paquete Package_Arrays.
● Utilizar las funciones input del paquete Package_Input.

Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego,
armar los módulos y paquetes.'''
################################# RESOLUCIÓN #################################
# from Package_Arrays.Array_Generales import ingresar_numeros
# from Package_Arrays.Package_Input.Input import *
# import Package_Arrays
# import Package_Arrays.Array_Generales
from Array_Generales import *
from Package_Input.Input import *
menu = '''a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Listar todos los números ingresados.
f. Listar todos los números pares.
g. Listar los números de las posiciones impares.
h. Salir'''

lista_numeros_ingresados = []
seguir = 'S'

while seguir == 'S':
    print(menu)
    opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
    
    if len(lista_numeros_ingresados) == 0 and opcion_ingresada != 'a' and opcion_ingresada != 'h':
        print('Primero debe cargar los datos.')
    else:
        match opcion_ingresada:
            case 'a':
                ingresar_numeros(lista_numeros_ingresados)
            case 'b':
                mostrar_positivos_y_negativos(lista_numeros_ingresados)
            case 'c':
                mostrar_suma_pares(lista_numeros_ingresados)
            case 'd':
                mostrar_impar_mayor(lista_numeros_ingresados)
            case 'e':
                listar_numeros(lista_numeros_ingresados)
            case 'f':
                listar_pares(lista_numeros_ingresados)
            case 'g':
                listar_posiciones_impares(lista_numeros_ingresados)
            case 'h':
                seguir = 'N'

