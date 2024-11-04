# Solicitarle al usuario el ingreso de un color primario. Validar que el mismo sea Rojo, Verde o Azul.

# Ejercicio 12
# Luciano Cotti

color = input('Ingrese un color primario: ')

while color != 'Rojo' and color != 'Verde' and color != 'Azul':
    color = input('Rojo, Verde o Azul... ')