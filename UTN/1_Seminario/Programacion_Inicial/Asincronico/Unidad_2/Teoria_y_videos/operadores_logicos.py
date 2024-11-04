edad_minima = 21

edad = int(input('Edad: '))
categoria = input('Categoría (A, B, C, D, E, F, G): ')

if edad >= edad_minima and edad < 65 and (categoria == 'D' or categoria == 'd'):
    print('Podés manejar ambulancias.')
elif edad >= 65:
    print('Andá a cuidar a los nietos.')
else:
    print('Triturando registro...')
    print('Trituración completa. La próxima vez haga las cosas bien.')