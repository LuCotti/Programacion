'''
En una clase de 5 alumnos se han realizado tres exámenes y se requiere determinar el número de:
    • Alumnos que aprobaron todos los exámenes.
    • Alumnos que aprobaron por lo menos un examen.
    • Alumnos que aprobaron únicamente el último examen.

A1  N1 N2 N3
A2  N1 N2 N3
A3  N1 N2 N3
A4  N1 N2 N3
A5  N1 N2 N3
'''

contador_general = 0
contador_todo_aprobado = 0
contador_uno_aprobado = 0
contador_ultimo_aprobado = 0

while contador_general < 5:
    nota1 = int(input('Ingrese la primera nota: '))
    nota2 = int(input('Ingrese la segunda nota: '))
    nota3 = int(input('Ingrese la tercera nota: '))
    
    if nota1 >= 6 and nota2 >= 6 and nota3 >= 6:
        contador_todo_aprobado += 1
    if nota1 >= 6 or nota2 >= 6 or nota3 >= 6:
        contador_uno_aprobado += 1
    if nota1 < 6 and nota2 < 6 and nota3 >= 6:
        contador_ultimo_aprobado += 1
    
    contador_general += 1


mensaje = f'''Alumnos que aprobaron todos los exámenes: {contador_todo_aprobado}
Alumnos que aprobaron por lo menos un examen: {contador_uno_aprobado}
Alumnos que aprobaron únicamente el último examen: {contador_ultimo_aprobado}'''

print(mensaje)