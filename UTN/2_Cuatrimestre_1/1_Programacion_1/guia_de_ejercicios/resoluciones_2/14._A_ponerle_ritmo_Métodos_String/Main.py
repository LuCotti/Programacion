# Paquetes importados
from datetime import datetime

# Datos
tema = 'Karina | J mena | Angela - Sinvergüenza'
vistas = '45.8 millones'
duración = '228'
link = 'https://www.youtube.com/watch?v=AhZvCgk1Ay4'
fecha_lanzamiento = '2023-12-05'

# Desarrollo de funciones
# 1. obtener_colaboradores(str) -> list: recibe como parámetro el
#    título del tema y retorna una lista con todos los colaboradores.
def obtener_colaboradores(titulo: str) -> list:
    colaboradores = titulo.split('-')[0]
    print(colaboradores)
# # Test
# obtener_colaboradores(tema)



# 2. obtener_nombre_tema(str) -> str: retorna el nombre del tema.
def obtener_nombre_tema(titulo: str) -> str:
    colaboradores = titulo.split('-')[1].strip()
    print(colaboradores)
# # Test
# obtener_nombre_tema(tema)



# 3. convertir_vistas_numerico(str)->int: convertirá la cantidad de
#    vistas a un número entero expresado en millones.
def convertir_vistas_numerico(vistas: str) -> int:
    vistas = float(vistas.split(' ')[0]) * 1000000
    vistas = int(vistas)
    return vistas
# # Test
# print(convertir_vistas_numerico(vistas))



# 4. convertir_duracion_numerico(str)->int: convertirá la duración a
#    un número entero.
def convertir_duracion_numerico(duracion: str) -> int:
    duracion = int(duracion)
    return duracion
# # Test
# print(type(convertir_duracion_numerico(duración)))



# 5. obtener_codigo(str)->str: retorna el código de la url recibida
#    como parámetro.
def obtener_codigo(link: str) -> str:
    return link
# # Test
# print(obtener_codigo(link))



# 6. formatear_fecha(str): retorna la fecha recibida por parámetro
#    como un objeto de tipo fecha
def formatear_fecha(fecha: str) -> datetime:
    fecha = fecha.replace('-', '')
    año, mes, dia = int(fecha[0:4]), int(fecha[4:6]), int(fecha[6:8])
    fecha = datetime(año, mes, dia)
    return fecha

# # Test
# print(formatear_fecha(fecha_lanzamiento))
