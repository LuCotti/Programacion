nota = int(input('Ingrese la nota: '))

while nota < 1 or nota > 10:
    nota = int(input('Ingrese nuevamente la nota: '))
print('Datos actualizados.')