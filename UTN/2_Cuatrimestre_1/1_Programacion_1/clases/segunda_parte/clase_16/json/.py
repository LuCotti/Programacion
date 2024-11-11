'''
Cargar un archivo JSON
Guardar una estructura de datos de python a JSON
Acutalizar datos en un archivo JSON
Eliminar datos en un archivo JSON
Agregar datos a un JSON existente
'''
import json

# # Cargar un archivo JSON
# archivo = open('configuracion.json', 'r')
# datos = json.load(archivo) # Diccionario
# archivo.close()

# print(type(datos))
# print(datos)


# # Guardar una estructura de datos de python a JSON
# datos = {
#     "usuario": "root",
#     "modo_oscuro": False,
#     "idiomas": ["es"]
# }

# archivo = open('configuracion.json', 'w')
# json.dump(datos, archivo, indent=4)
# archivo.close()



# # Actualizar datos en un archivo JSON
# archivo = open('configuracion.json', 'r')
# datos = json.load(archivo)
# archivo.close()
# # Actualizar los datos
# datos["usuario"] = "usuario1"
# datos["idiomas"].append("de")
# # Guardar los datos
# with open("configuracion.json", "w") as archivo: # Nos ayuda a no llamar a la función archivo.close().
#     json.dump(datos, archivo, indent=4)



# # Eliminar datos en un archivo JSON
# with open('configuracion.json', 'r') as archivo:
#     datos = json.load(archivo)

# # Eliminar la clave 'modo_oscuro'.
# if 'modo_oscuro' in datos:
#     del datos['modo_oscuro'] # Elimino la clave-valor 'modo_oscuro'

# # Guardamos el resultado después del procesamiento
# with open('configuracion.json', 'w') as archivo: # Eliminar todo lo que tiene y recrearlo.
#     json.dump(datos, archivo, indent=4)




# Agregar datos a un JSON existente
with open('configuracion.json', 'r') as archivo:
    datos = json.load(archivo)

# Agregamos una nueva clave
datos['tema'] = 'oscuro'
# Guarda los datos actualizados en el archivo JSON.
with open('configuracion.json', 'w') as archivo:
    json.dump(datos, archivo, indent=4)

