################################## CONSIGNA ##################################
'''
Ejercicio: Gestión de Estudiantes y Notas

En una universidad, se desea gestionar la información de un grupo de 
estudiantes. Para ello, se te pide desarrollar un programa en Python que 
utilice arrays paralelos para almacenar la siguiente información de cada 
estudiante:

Nombre del estudiante 
Edad del estudiante 
Nota final del estudiante 

El programa debe realizar las siguientes tareas:

Ingreso de Datos: Solicitar al usuario que ingrese la cantidad de estudiantes 
que va a registrar y luego ingresar para cada uno:
*Nombre
*Edad
*Nota final
Mostrar Información: Imprimir por pantalla la lista de estudiantes con su 
respectiva edad y nota final.
Cálculo de Promedio: Calcular e imprimir el promedio de las notas finales de 
todos los estudiantes.
Buscar Estudiante: Permitir al usuario ingresar el nombre de un estudiante y 
mostrar su edad y nota final. Si el estudiante no existe, mostrar un mensaje 
apropiado.
Estudiante con Mayor Nota: Mostrar el nombre del estudiante con la mayor 
nota.

Menú:

1. Ingresar datos.
2. Mostrar información.
3. Cálculo del promedio.
4. Búsqueda de estudiantes.
5. Estudiante con mayor nota.
6. Salir.
Ingrese la opción 1.
'''

################################# RESOLUCIÓN #################################
# INGRESO Y VALIDACIÓN DE LA CANTIDAD DE ALUMNOS
cantidad_alumnos = int(input('Ingrese la cantidad de alumnos a ingresar: '))
while cantidad_alumnos <= 0:
    cantidad_alumnos = int(input('Dato inválido. Ingrese nuevamente la cantidad de alumnos a ingresar: '))

# DEFINICIÓN DE LISTAS
nombres = [0] * cantidad_alumnos
edades = [0] * cantidad_alumnos
notas = [0] * cantidad_alumnos

# MENÚ
menu = '''Menú:
1. Ingresar datos.
2. Mostrar información.
3. Cálculo del promedio.
4. Búsqueda de estudiantes.
5. Estudiante con mayor nota.
6. Salir.'''

# INGRESO Y VALIDACIÓN DE DATOS
def ingresar_datos():
    for i in range(cantidad_alumnos):
        nombre_ingresado = input('Ingrese su nombre: ')
        while not nombre_ingresado.isalpha():
            nombre_ingresado = input('Dato inválido. Ingrese nuevamente su nombre: ')
        
        edad_ingresada = int(input('Ingrese su edad: '))
        while edad_ingresada < 0 or edad_ingresada > 100:
            edad_ingresada = int(input('Dato inválido. Ingrese nuevamente su edad: '))
        
        nota_ingresada = int(input('Ingrese su nota final (0 - 100): '))
        while nota_ingresada < 0 or nota_ingresada > 100:
            nota_ingresada = int(input('Dato inválido. Ingrese nuevamente su nota final (0 - 100): '))
        
        # CONFECCIÓN DE LISTAS
        nombres[i] = nombre_ingresado
        edades[i] = edad_ingresada
        notas[i] = nota_ingresada

# MOSTRAR INFORMACIÓN
def mostrar_info():
    for i in range(cantidad_alumnos):
        print(f'Legajo: {i}\nNombre: {nombres[i]}\nEdad: {edades[i]}\nNota final: {notas[i]}\n')

# CÁLCULO DEL PROMEDIO
def calcular_promedio(notas):
    contador = 0
    acumulador = 0
    for i in range(len(notas)):
        contador += 1
        acumulador += notas[i]
    
    promedio = acumulador / contador
    print(f'Promedio de todas las notas ingresadas: {promedio}.')

# BUSCADOR DE ALUMNOS
def buscar_alumno(nombres):
    nombre_buscado = input('Ingrese el nombre del alumno que desea buscar: ')
    bandera = 0
    for i in range(len(nombres)):
        if nombre_buscado == nombres[i]:
            bandera = 1
            print(f'Edad: {edades[i]}\nNota: {notas[i]}')
    if bandera == 0:
        print('El alumno buscado no existe.')

# BUSCADOR DE ALUMNO CON MAYOR NOTA
def buscar_alumno_con_mayor_nota(notas):
    mayor_nota = None
    nombre_buscado = None
    for i in range(len(notas)):
        if i == 0:
            mayor_nota = notas[i]
            nombre_buscado = nombres[i]
        elif notas[i] > mayor_nota:
            mayor_nota = notas[i]
            nombre_buscado = nombres[i]
    print(f'{nombre_buscado} es el estudiante con mayor nota.')

def datos_estudiantes():
    print(menu)
    opcion_ingresada = int(input('Ingrese una de las opciones anteriores: '))
    
    while opcion_ingresada < 1 or opcion_ingresada > 6:
        opcion_ingresada = int(input('Dato inválido. Ingrese una de las opciones anteriores: '))
    
    while opcion_ingresada != 1 and nombres == [0] * cantidad_alumnos:
        opcion_ingresada = 3
    
    match opcion_ingresada:
        case 1:
            bandera = 1
            ingresar_datos()
        case 2:
            mostrar_info()
        case 3:
            calcular_promedio(notas)
        case 4:
            buscar_alumno(nombres)
        case 5:
            buscar_alumno_con_mayor_nota(notas)
        case 6:
            return
    datos_estudiantes()

datos_estudiantes()