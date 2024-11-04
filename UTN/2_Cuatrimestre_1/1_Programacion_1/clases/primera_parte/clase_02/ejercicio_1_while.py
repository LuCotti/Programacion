'''
Seleccionar un tipo de vehículo e indicar el peaje a pagar según su valor numérico:
• 1 - Turismo, peaje = $1700
• 2 - Autobús, peaje = $4000
• 3 - Motocicleta, peaje = $1000
Caso contrario: vehículo no autorizado
5 vehículos.

Informe la recaudación
'''

contador = 1
total = 0

while contador <= 5:
    vehiculo = int(input('Ingrese el tipo de vehículo (1 para turismo, 2 para autobús, 3 para motocicleta): '))
    match vehiculo:
        case 1:
            total += 1700
        case 2:
            total += 4000
        case 3:
            total += 1000
        case _:
            print('Vehículo no autorizado.')
    
    contador += 1

print(f'La tarifa total es de ${total}.')

# HACER CON FOR