from datetime import datetime
titulo = 'Karina | J mena | Angela - Sinvergüenza'
# colaboradores = []
# for colaborador in titulo.split('|'):
#     colaboradores.append(colaborador.strip())
# print(colaboradores)

def obtener_colaboradores(titulo):
    partes = titulo.split(' - ')
    colaboradores = partes[0]
    lista_colaboradores = []
    for colaborador in partes[0].split('|'):
        lista_colaboradores.append(colaborador.strip())
    return lista_colaboradores

# Test
# print(obtener_colaboradores(titulo))

def obtener_nombre_tema(titulo):
    partes = titulo.split(' - ')
    return partes[1]

# Test
# print(obtener_nombre_tema(titulo))
#######################################################
def convertir_vistas_numerico(vistas):
    partes = vistas.split(' ')
    return int(float(partes[0])) * 1000000

# Test
vistas = '45.8 millones'
# print(convertir_vistas_numerico(vistas))
##########################################################
duracion = '228'
def convertir_duracion_numerico(duracion):
    return int(duracion)


link = 'https://www.youtube.com/watch?v=AhZvCgk1Ay4'
def obtener_codigo(link):
    return link.split('=')[-1]

# Test
# print(obtener_codigo(link))

################################################################
fecha_lanzamiento = '2023-12-05'
def formatear_fecha(fecha_lanzamiento):
    return datetime.strptime(fecha_lanzamiento, '%Y-%m-%d').date()

# Test
print(type(formatear_fecha(fecha_lanzamiento)))