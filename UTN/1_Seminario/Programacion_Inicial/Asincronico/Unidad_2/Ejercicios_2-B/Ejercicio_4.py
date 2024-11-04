# Crear un programa que solicite al usuario que ingrese una letra. Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas). En caso de no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.
letra = input('DECIME "U", "T", O "N": ')

while letra != 'U' and letra != 'T' and letra != 'N':
    letra = input('NO ENTENDEEEEES: ')

print('¡Gracias, vuelva pronto!')