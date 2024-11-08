# Lista de reproducción
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

# Funciones
def normalizar_datos(lista: list) -> None:
    for i in range(len(lista)):
        print(lista[i])

def obtener_nombre_tema(titulo: str) -> str:
    contiene_guion = False
    for i in range(len(titulo)):
        if titulo[i] == '-':
            contiene_guion = True
    
    if contiene_guion:
        nombre_tema = titulo.split('-')[1].strip()
    else:
        nombre_tema = titulo
    print(nombre_tema)

# Menú
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
# while True:
#     print(menu)
#     opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
#     match opcion_ingresada:
#         case 'A':
#             normalizar_datos(temas)
#         case 'B':
#             for i in range(len(temas)):
#                 obtener_nombre_tema(temas[i]['tema'])
#         case 'C':
#             pass
#         case 'D':
#             pass
#         case 'E':
#             pass
#         case 'F':
#             pass
#         case 'G':
#             pass
#         case 'H':
#             pass
#         case 'I':
#             pass
#         case 'J':
#             break
#         case _:
#             print('La opción ingresada no existe.')


