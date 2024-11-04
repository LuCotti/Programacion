# ------------------------------------------------------------------------ FORMULARIO ------------------------------------------------------------------------
# Universidad Tecnológica Nacional
# Facultad Regional Avellaneda
# Materia: Programación inicial
# Pertenece a: Seminario de Nivelación TEMA A - TN
# Apellido(1): Cotti
# Nombre/s(1): Luciano Ariel
# División(1): 306
# DNI(1): 43.873.697
# Fecha: 31-07-24
# Docente/s(2):
# Nota(2):
# Firma(2):
# Instancia(2)(3): P1

# ------------------------------------------------------------------------ CONSIGNAS ------------------------------------------------------------------------
# Usuarios vendedores de MercadoLibre
# Cargar 10 usuarios/vendedores de MercadoLibre con sus respectivas publicaciones.
# ● Los datos que se cargarán son:
# ● Nombre de usuario
# ● Edad (validar)
# ● Cantidad de productos (validar-número entero positivo).
# ● Número de publicaciones (validar-número entero positivo, hasta 1000).
# ● Tipo de publicación ("producto", "servicio", "subasta")
# ● Cuenta activa ("si", "no")

# Se necesita saber
# Tema A:
# 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive.
# 2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
# 3. Porcentaje de publicaciones de tipo subasta.
# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”.
# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.

# ------------------------------------------------------------------------ RESOLUCIÓN ------------------------------------------------------------------------

# DEFINICIÓN DE CONTADORES Y ACUMULADORES
contador_vendedores = 0

# 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive.
contador_usuarios_activos_producto = 0

# 2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
bandera_500_publicaciones = 0

# 3. Porcentaje de publicaciones de tipo subasta.
acumulador_publicaciones_general = 0
acumulador_publicaciones_subasta = 0

# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”.
contador_edades_producto = 0
acumulador_edades_producto = 0

# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
acumulador_publicaciones_subasta_activas = 0
acumulador_publicaciones_producto_activas = 0
acumulador_publicaciones_servicio_activas = 0



# INGRESO Y VALIDACIÓN DE DATOS
while contador_vendedores < 10:
    nombre_ingresado = input('Ingrese su nombre: ')
    
    edad_ingresada = int(input('Ingrese su edad: '))
    while edad_ingresada < 18:
        edad_ingresada = int(input('No se aceptan menores de 18 años. Ingrese su edad nuevamente: '))
    
    cantidad_de_productos_ingresada = int(input('Ingrese la cantidad de productos: '))
    while cantidad_de_productos_ingresada < 0:
        cantidad_de_productos_ingresada = int(input('Dato inválido. Ingrese la cantidad de productos nuevamente: '))
    
    numero_de_publicaciones_ingresado = int(input('Ingrese el número de publicaciones: '))
    while numero_de_publicaciones_ingresado < 0 or numero_de_publicaciones_ingresado > 1000:
        numero_de_publicaciones_ingresado = int(input('Dato inválido. Ingrese el número de publicaciones nuevamente: '))
    
    tipo_de_publicacion_ingresado = input('Ingrese el tipo de publicación ("producto", "servicio", "subasta"): ')
    while tipo_de_publicacion_ingresado != 'producto' and tipo_de_publicacion_ingresado != 'servicio' and tipo_de_publicacion_ingresado != 'subasta':
        tipo_de_publicacion_ingresado = input('Dato inválido. Ingrese el tipo de publicación nuevamente ("producto", "servicio", "subasta"): ')
    
    cuenta_activa = input('¿Posee usted una cuenta activa? ("si", "no"): ')
    while cuenta_activa != 'si' and cuenta_activa != 'no':
        cuenta_activa = input('Dato inválido. ¿Posee usted una cuenta activa? ("si", "no"): ')
    
    
    
    # CONDICIONALES
    # 1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive.
    if cuenta_activa == 'si':
        if tipo_de_publicacion_ingresado == 'producto':
            if edad_ingresada >= 25 and edad_ingresada <= 35:
                contador_usuarios_activos_producto += 1
    
    # 2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
    if numero_de_publicaciones_ingresado > 500:
        if bandera_500_publicaciones == 0:
            menor_edad = edad_ingresada
            nombre_500_publicaciones = nombre_ingresado
            tipo_500_publicaciones = tipo_de_publicacion_ingresado
            bandera_500_publicaciones = 1
        
        elif edad_ingresada < menor_edad:
            menor_edad = edad_ingresada
            nombre_500_publicaciones = nombre_ingresado
            tipo_500_publicaciones = tipo_de_publicacion_ingresado
    
    
    # 3. Porcentaje de publicaciones de tipo subasta.
    if tipo_de_publicacion_ingresado == 'subasta':
        acumulador_publicaciones_general += numero_de_publicaciones_ingresado
        acumulador_publicaciones_subasta += numero_de_publicaciones_ingresado
        
        # 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
        if cuenta_activa == 'si':
            acumulador_publicaciones_subasta_activas += numero_de_publicaciones_ingresado
    
    # 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”.
    elif tipo_de_publicacion_ingresado == 'producto':
        contador_edades_producto += 1
        acumulador_edades_producto += edad_ingresada
        
        # 3. Porcentaje de publicaciones de tipo subasta.
        acumulador_publicaciones_general += numero_de_publicaciones_ingresado
        
        # 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
        if cuenta_activa == 'si':
            acumulador_publicaciones_producto_activas += numero_de_publicaciones_ingresado
    else:
        # 3. Porcentaje de publicaciones de tipo subasta.
        acumulador_publicaciones_general += numero_de_publicaciones_ingresado
        
        # 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
        if cuenta_activa == 'si':
            acumulador_publicaciones_servicio_activas += numero_de_publicaciones_ingresado
    
    
    contador_vendedores += 1


# CÁLCULOS ADICIONALES
# 3. Porcentaje de publicaciones de tipo subasta.
porcentaje_subasta = acumulador_publicaciones_subasta * 100 / acumulador_publicaciones_general

# 4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”.
promedio_edades_producto = acumulador_edades_producto / contador_edades_producto

# 5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre “activa”.
if acumulador_publicaciones_subasta_activas > acumulador_publicaciones_producto_activas and acumulador_publicaciones_subasta_activas > acumulador_publicaciones_servicio_activas:
    tipo_con_mas_publicaciones = 'subasta'
elif acumulador_publicaciones_producto_activas > acumulador_publicaciones_subasta_activas and acumulador_publicaciones_producto_activas > acumulador_publicaciones_servicio_activas:
    tipo_con_mas_publicaciones = 'producto'
else:
    tipo_con_mas_publicaciones = 'servicio'


# INFORME DE RESULTADOS
mensaje = f'''\nCantidad de usuarios con la cuenta activa cuyo producto sea del tipo “producto”, cuya edad esté entre 25 y 35 años inclusive: {contador_usuarios_activos_producto}.
{nombre_500_publicaciones}, de tipo {tipo_500_publicaciones}, es el usuario de menor edad con más de 500 publicaciones.
Porcentaje de publicaciones de tipo subasta: {porcentaje_subasta}%.
Promedio de edad de los usuarios cuyas publicaciones fueron del tipo “producto”: {promedio_edades_producto} años.
El tipo con mayor cantidad de publicaciones, cuya cuenta se encuentra “activa” es: {tipo_con_mas_publicaciones}.'''


print(mensaje)