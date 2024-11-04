def penales():
    contador_convertidos = 0
    contador_errados = 0
    for i in range(1, 6):
        resultado = int(input(f'Informe el resultado del penal {i} (gol / fallo): '))
        while resultado != 'gol' and resultado != 'fallo':
            resultado = int(input(f'Dato inválido. Informe nuevamente el resultado del penal {i} (gol / fallo): '))
        if resultado == 'gol':
            contador_convertidos += 1
        else:
            contador_errados += 1
    
    return contador_convertidos, contador_errados

def definir_ganador():
    print('Ingrese los resultados del primer equipo:')
    convertidos1, errados1 = penales()
    print('Ingrese los resultados del segundo equipo:')
    convertidos2, errados2 = penales()


















