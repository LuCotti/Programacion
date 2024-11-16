# IMPORTACIONES NECESARIAS
from Package_Input.Input import *
from Package_ordenamiento.ordenamiento import *
from datetime import datetime



# LISTA DE REPRODUCCIÓN
temas = [
{"tema": "El Temblor", "fecha_lanzamiento": "2017-03-12", "vistas":
"45.8 millones", "duracion": "235", "link":
"https://www.youtube.com/watch?v=A1B2C3D4E5"},
{"tema": "Mi Libertad", "fecha_lanzamiento": "2017-07-25",
"vistas": "37.4 millones", "duracion": "210", "link":
"https://www.youtube.com/watch?v=F6G7H8I9J0"},
{"tema": "Tu Mejor Estudiante", "fecha_lanzamiento": "2018-05-14",
"vistas": "52.6 millones", "duracion": "248", "link":
"https://www.youtube.com/watch?v=K1L2M3N4O5"},
{"tema": "FMK | Estani | Rusherking - Bandido", "fecha_lanzamiento":
"2022-09-10", "vistas": "64.2 millones", "duracion":
"320", "link": "https://www.youtube.com/watch?v=P6Q7R8S9T0"},
{"tema": "Karina - No Me Digas que No", "fecha_lanzamiento":
"2022-11-21", "vistas": "58.3 millones", "duracion": "298", "link":
"https://www.youtube.com/watch?v=U1V2W3X4Y5"},
{"tema": "Mario Luis - Whisky", "fecha_lanzamiento": "2022-08-15",
"vistas": "41.7 millones", "duracion": "245", "link":
"https://www.youtube.com/watch?v=Z6A7B8C9D0"},
{"tema": "FMK - Tu 50", "fecha_lanzamiento": "2022-06-05",
"vistas": "49.9 millones", "duracion": "260", "link":
"https://www.youtube.com/watch?v=E1F2G3H4I5"},
{"tema": "Tengo en Venta el Corazón", "fecha_lanzamiento":
"2023-02-18", "vistas": "32.1 millones", "duracion": "275", "link":
"https://www.youtube.com/watch?v=J6K7L8M9N0"},
{"tema": "Esa Morocha", "fecha_lanzamiento": "2023-04-12",
"vistas": "27.5 millones", "duracion": "230", "link":
"https://www.youtube.com/watch?v=O1P2Q3R4S5"},
{"tema": "Ulises Bueno | Los Palmeras | Migrantes - Atorrante",
"fecha_lanzamiento": "2023-07-19", "vistas": "78.4 millones",
"duracion": "360", "link":
"https://www.youtube.com/watch?v=T6U7V8W9X0"},
{"tema": "La Konga | Antonio Ríos - Adicto", "fecha_lanzamiento":
"2023-09-09", "vistas": "53.9 millones", "duracion": "310", "link":
"https://www.youtube.com/watch?v=Y1Z2A3B4C5"},
{"tema": "J mena | Karina | Angela Torres - Sinvergüenza", "fecha_lanzamiento":
"2023-11-22", "vistas": "60.7 millones", "duracion":
"295", "link": "https://www.youtube.com/watch?v=D6E7F8G9H0"},
{"tema": "Angel López | Rusherking - A Puro Dolor", "fecha_lanzamiento":
"2024-01-15", "vistas": "34.8 millones", "duracion":
"305", "link": "https://www.youtube.com/watch?v=I1J2K3L4M5"},
{"tema": "BM | Mario Luis | Onda Sabanera - Ladrona", "fecha_lanzamiento":
"2024-03-10", "vistas": "29.6 millones", "duracion":
"280", "link": "https://www.youtube.com/watch?v=N6O7P8Q9R0"},
{"tema": "Chernobyl", "fecha_lanzamiento": "2019-06-08", "vistas":
"15.2 millones", "duracion": "215", "link":
"https://www.youtube.com/watch?v=S1T2U3V4W5"},
{"tema": "Pastillitas", "fecha_lanzamiento": "2020-10-30",
"vistas": "18.7 millones", "duracion": "220", "link":
"https://www.youtube.com/watch?v=X6Y7Z8A9B0"},
{"tema": "Como Vos Lo Haces", "fecha_lanzamiento": "2021-02-13",
"vistas": "21.5 millones", "duracion": "265", "link":
"https://www.youtube.com/watch?v=C1D2E3F4G5"},
{"tema": "Estani - Sola", "fecha_lanzamiento": "2021-08-29",
"vistas": "25.3 millones", "duracion": "255", "link":
"https://www.youtube.com/watch?v=H6I7J8K9L0"},
{"tema": "Rusherking - Porque Puedo", "fecha_lanzamiento":
"2022-03-07", "vistas": "36.8 millones", "duracion": "310", "link":
"https://www.youtube.com/watch?v=M1N2O3P4Q5"},
{"tema": "Quien es Quien", "fecha_lanzamiento": "2022-12-12",
"vistas": "33.9 millones", "duracion": "245", "link":
"https://www.youtube.com/watch?v=R6S7T8U9V0"},
{"tema": "La Konga | Karina - Manicomio", "fecha_lanzamiento":
"2023-05-17", "vistas": "40.4 millones", "duracion": "295", "link":
"https://www.youtube.com/watch?v=W1X2Y3Z4A5"},
{"tema": "Karina | Angela - WTF", "fecha_lanzamiento":
"2023-10-05", "vistas": "23.0 millones", "duracion": "225", "link":
"https://www.youtube.com/watch?v=B6C7D8E9F0"}
]



# FUNCIONES DEL EJERCICIO ANTERIOR (ADAPTADAS)
def obtener_tema(titulo: str) -> list:
    print(f'Tema: {titulo}')
    return titulo

# Test
# for i in range(len(temas)):
#     obtener_tema(temas[i]['tema'])

def formatear_fecha(fecha: str) -> datetime:
    fecha = fecha.replace('-', '')
    año, mes, dia = int(fecha[0:4]), int(fecha[4:6]), int(fecha[6:8])
    fecha = datetime(año, mes, dia)
    print(f'Fecha de lanzamiento: {fecha}')
    return fecha

# Test
# for i in range(len(temas)):
#     formatear_fecha(temas[i]['fecha_lanzamiento'])


def normalizar_vistas(vistas: str) -> None:
    print(f'Vistas: {vistas}')
    return None

# Test
# for i in range(len(temas)):
#     convertir_vistas_numerico(temas[i]['vistas'])

def normalizar_duracion(duracion: str) -> int:
    if validate_number(duracion):
        duracion = int(duracion)
        duracion_min = str(duracion // 60)
        duracion_seg = duracion % 60
        if duracion_seg < 10:
            duracion_seg = str(duracion_seg)
            duracion_normalizada = duracion_min + ':0' + duracion_seg
        else:
            duracion_seg = str(duracion_seg)
            duracion_normalizada = duracion_min + ':' + duracion_seg
        
        print(f'Duración: {duracion_normalizada}')
        return duracion_normalizada
    else:
        print('El dato ingresado es inválido.')
        return None

# Test
# for i in range(len(temas)):
#     normalizar_duracion(temas[i]['duracion'])

def obtener_codigo(link: str) -> str:
    print(f'Link: {link}')
    return link

# Test
# for i in range(len(temas)):
#     obtener_codigo(temas[i]['link'])



# FUNCIONES PRINCIPALES
# 1. Normalizar datos
def normalizar_datos(lista: list) -> None:
    for i in range(len(lista)):
        print('')
        print(f'TEMA {i + 1}')
        obtener_tema(lista[i]['tema'])
        formatear_fecha(lista[i]['fecha_lanzamiento'])
        normalizar_vistas(lista[i]['vistas'])
        normalizar_duracion(lista[i]['duracion'])
        obtener_codigo(lista[i]['link'])
    return None

# 2. Mostrar temas
def mostrar_temas(lista: list) -> None:
    for i in range(len(lista)):
        contiene_guion = False
        for j in range(len(lista[i]['tema'])):
            if lista[i]['tema'][j] == '-':
                contiene_guion = True
        
        if contiene_guion:
            nombre_tema = lista[i]['tema'].split('-')[1].strip()
        else:
            nombre_tema = lista[i]['tema']
        print(f'Tema {i + 1}: {nombre_tema}')
    return None

# 3. Ordenar temas
def ordenar_temas(lista: list) -> list:
    lista_temas_duracion = [] # Genero una lista vacía que solo contendrá la duración de cada tema
    for i in range(len(lista)):
        lista_temas_duracion.append(int(lista[i]['duracion']))
    lista_temas_duracion = quick_sort(lista_temas_duracion, 'DES') # Ordeno la lista de mayor a menor
    lista_temas_ordenados = [] # Genero una lista vacía que contendrá toda la información ordenada
    for i in range(len(lista_temas_duracion)):
        for j in range(len(lista)):
            if lista_temas_duracion[i] == int(lista[j]['duracion']):
                lista_temas_ordenados.append(lista.pop(j))
                break
    return lista_temas_ordenados

# 4. Promedio de vistas
def convertir_vistas_numerico(vistas: str) -> int:
    vistas = float(vistas.split(' ')[0]) * 1000
    vistas = int(vistas)
    return vistas

def mostrar_promedio_vistas(lista: list) -> None:
    acumulador = 0
    contador = 0
    for i in range(len(lista)): # Bucle for para cargar las variables acumulador y contador.
        acumulador += convertir_vistas_numerico(lista[i]['vistas'])
        contador += 1
    
    promedio = acumulador // contador
    print(f'Promedio de vistas: {promedio} k.')
    return None

# 5. Máxima reproducción
def mostrar_maxima_reproduccion(lista):
    videos_con_mayor_reproduccion = [] # Defino una lista que contendrá las posiciones de los videos con mayor reproducción.
    maxima_reproduccion = 0 # Defino una variable que contendrá la cantidad de vistas del video con el máximo de estas.
    for i in range(len(lista)):
        if i == 0:
            maxima_reproduccion = convertir_vistas_numerico(lista[i]['vistas'])
            videos_con_mayor_reproduccion.append(i)
        elif convertir_vistas_numerico(lista[i]['vistas']) > maxima_reproduccion:
            videos_con_mayor_reproduccion.clear()
            maxima_reproduccion = convertir_vistas_numerico(lista[i]['vistas'])
            videos_con_mayor_reproduccion.append(i)
        elif convertir_vistas_numerico(lista[i]['vistas']) == maxima_reproduccion:
            videos_con_mayor_reproduccion.append(i)
    
    lista_nueva = [] # Creo una lista de reproducción que solo contenga los ítems de mayor vistas.
    for i in range(len(videos_con_mayor_reproduccion)):
        lista_nueva.append(lista[videos_con_mayor_reproduccion[i]])
    
    normalizar_datos(lista_nueva) # Despliego los datos normalizados de la nueva lista.

# 6. Mínima reproducción
def mostrar_minima_reproduccion(lista):
    videos_con_minima_reproduccion = [] # Defino una lista que contendrá las posiciones de los videos con mínima reproducción.
    minima_reproduccion = 0 # Defino una variable que contendrá la cantidad de vistas del video con el mínimo de estas.
    for i in range(len(lista)):
        if i == 0:
            minima_reproduccion = convertir_vistas_numerico(lista[i]['vistas'])
            videos_con_minima_reproduccion.append(i)
        elif convertir_vistas_numerico(lista[i]['vistas']) < minima_reproduccion:
            videos_con_minima_reproduccion.clear()
            minima_reproduccion = convertir_vistas_numerico(lista[i]['vistas'])
            videos_con_minima_reproduccion.append(i)
        elif convertir_vistas_numerico(lista[i]['vistas']) == minima_reproduccion:
            videos_con_minima_reproduccion.append(i)
    
    lista_nueva = [] # Creo una lista de reproducción que solo contenga los ítems de menor vistas.
    for i in range(len(videos_con_minima_reproduccion)):
        lista_nueva.append(lista[videos_con_minima_reproduccion[i]])
    
    normalizar_datos(lista_nueva) # Despliego los datos normalizados de la nueva lista.

# 7. Búsqueda por código (posición en la lista temas)
def buscar_por_codigo(lista: list) -> None:
    codigo = get_int('Ingrese el código del video (1 - 22): ', 'Error.', 1, len(lista), 3)
    codigo -= 1
    lista_nueva = [] # Debo crear una lista con un único elemento ya que la función normalizar_datos debe recibir una lista como parámetro.
    for i in range(len(lista)):
        if codigo == i:
            lista_nueva.append(lista[i])
    normalizar_datos(lista_nueva)

# 8. Listar por colaborador
def buscar_subcadenas(cadena: str, subcadena: str) -> int:
    contador_subcadena = 0
    for i in range(len(cadena)):
        contador_auxiliar = 0
        if cadena[i] == subcadena[0]:
            try:
                for j in range(1, len(subcadena)):
                    if cadena[i + j] == subcadena[j]:
                        contador_auxiliar += 1
                if contador_auxiliar == len(subcadena) - 1:
                    contador_subcadena += 1
                else:
                    continue
            except IndexError:
                continue
    
    return contador_subcadena

def listar_por_colaborador(lista: list) -> None:
    # Pido por consola el dato.
    colaborador_ingresado = input('Ingrese el colaborador: ')
    # Creo la lista
    lista_nueva = []
    
    for i in range(len(lista)):
        if buscar_subcadenas(lista[i]['tema'], colaborador_ingresado) != 0:
            lista_nueva.append(lista[i])
    
    normalizar_datos(lista_nueva)
    return None

# 9. Listar por mes (ACÁ ME QUEDÉ)############################################################################################################################################################################################################################


# Menú y bucle
menu = '''
A. NORMALIZAR DATOS.
B. MOSTRAR TEMAS.
C. ORDENAR TEMAS.
D. PROMEDIO DE VISTAS.
E. MÁXIMA REPRODUCCIÓN.
F. MÍNIMA REPRODUCCIÓN.
G. BÚSQUEDA POR CÓDIGO.
H. LISTAR POR COLABORADOR.
I. LISTAR POR MES.
J. SALIR.
'''
flag_datos_normalizados = False
while True:
    print(menu)
    opcion_ingresada = get_string('Ingrese una de las opciones anteriores: ', 'Error.', 1, 3)
    opcion_ingresada = opcion_ingresada.upper()
    match opcion_ingresada:
        case 'A':
            normalizar_datos(temas)
            flag_datos_normalizados = True
        case 'B':
            if flag_datos_normalizados:
                mostrar_temas(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'C':
            if flag_datos_normalizados:
                temas = ordenar_temas(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'D':
            if flag_datos_normalizados:
                mostrar_promedio_vistas(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'E':
            if flag_datos_normalizados:
                mostrar_maxima_reproduccion(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'F':
            if flag_datos_normalizados:
                mostrar_minima_reproduccion(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'G':
            if flag_datos_normalizados:
                buscar_por_codigo(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'H':
            if flag_datos_normalizados:
                listar_por_colaborador(temas)
            else:
                print('Primero se deben normalizar los datos.')
        case 'I':
            pass
        case 'J':
            break
        case _:
            print('La opción ingresada no existe.')
