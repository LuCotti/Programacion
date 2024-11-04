# TP Validaciones.
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos para luego mostrarlos por pantalla. 
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Luciano Cotti

# INGRESO Y VALIDACIÓN DE DATOS
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
while edad < 18 or edad > 90:
    print('Dato inválido. La edad debe estar comprendida entre 18 y 90 años.')
    edad = int(input('Ingrese su edad nuevamente: '))
estado_civil = input('Ingrese su estado civil: ')
while estado_civil != 'Soltero/a' and estado_civil != 'Casado/a' and estado_civil != 'Divorciado/a' and estado_civil != 'Viudo/a':
    print('Dato inválido. Las opciones son: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.')
    estado_civil = input('Ingrese su estado civil nuevamente: ')
numero_legajo = int(input('Ingrese su número de legajo: '))
while numero_legajo < 1000 or numero_legajo > 9999:
    print('Dato inválido. Debe ingresar un valor numérico de 4 cifras, sin ceros a la izquierda.')
    numero_legajo = int(input('Ingrese su número de legajo nuevamente: '))

# INFORME DE RESULTADOS
print('Apellido registrado:',apellido)
print('Edad registrada:',edad)
print('Estado civil registrado:',estado_civil)
print('Número de legajo registrado:',numero_legajo)