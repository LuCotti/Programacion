# --------------------------------------------------------------------- CONSIGNA ---------------------------------------------------------------------
# Integrador E/S

# La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

# CONFECCIÓN DE UN COMETA: 

# Medidas:
# AB = Diágonal mayor
# DC = Diágonal menor
# BD y BC = lados menores
# AD y AC = lados mayores




# El usuario ingresará las medidas  BC, CD y DA.

# Detalles de construcción

# Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
# El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
# Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

# Ejercicio 10
# Luciano Cotti



# --------------------------------------------------------------------- RESOLUCIÓN ---------------------------------------------------------------------
#INGRESO DE DATOS
BC = float(input('Ingrese la longitud del lado menor [cm]: '))
CD = float(input('Ingrese la longitud de la diagonal menor [cm]: '))
DA = float(input('Ingrese la longitud del lado mayor [cm]: '))

# CÁLCULOS PARA VARILLAS
AB1 = ((CD / 2)**2 + DA**2)**0.5 # Parte inferior de la diagonal mayor.
AB2 = ((CD / 2)**2 + BC**2)**0.5 # Parte superior de la diagonal mayor.
AB = AB1 + AB2 # Total de la diagonal mayor.

total_varillas = (AB + CD + BC * 2 + DA * 2) * 10 # Total de las varillas expresado en cm.
total_varillas_m = total_varillas / 100 # Total de las varillas expresado en m.

# CÁLCULOS PARA PAPEL
area1 = ((CD / 2) * AB2) / 2 # Parte superior del área.
area2 = ((CD / 2) * AB1) / 2 # Parte inferior del área.
area_total = area1 + area2 # Total del área.
total_papel = area_total * 10 # Total de papel expresado en cm.
total_papel_m = total_papel / 100 # Total de papel expresado en m.
total_papel_m *= 1.1 # 10% adicional para la cola del cometa

# MOSTRAR RESULTADOS
mensaje = f'Para la construcción de 10 cometas, serán necesarios {total_varillas_m} metros de varillas de plástico y {total_papel_m} metros de papel.'
print(mensaje)