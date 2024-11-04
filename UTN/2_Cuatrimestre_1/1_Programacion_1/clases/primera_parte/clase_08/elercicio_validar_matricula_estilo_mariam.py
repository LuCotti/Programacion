'''Desarrollo de una Función para Validar Matrículas de Automóviles:

Desarrolla una función en Python que valide si una matrícula de automóvil cumple con una política
de formato específica. La función debe recibir una matrícula como argumento y devolver un valor 
que indique si la matrícula es válida o no, de acuerdo con las reglas establecidas.

AB123CD'''


def validar_matricula(matricula): # ARREGLAR FUNCIÓN
    if matricula[:2].isalpha() and matricula[3:5].isnumeric() and matricula[6:7].isalpha():
        return True
    else:
        return False

print(validar_matricula(input('Ingrese la matrícula: ')))