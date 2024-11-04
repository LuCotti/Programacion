'''Desarrollo de una Función para Validar Matrículas de Automóviles:

Desarrolla una función en Python que valide si una matrícula de automóvil cumple con una política
de formato específica. La función debe recibir una matrícula como argumento y devolver un valor 
que indique si la matrícula es válida o no, de acuerdo con las reglas establecidas.

AB123CD'''

def validar_matricula(matricula):
    # Se valida que cumpla con la cantidad de caracteres.
    if len(matricula) == 7:
        # Definición del contador en 0.
        contador = 0
        
        for i in range(len(matricula)):
            # Se valida que los primeros y últimos dos caracteres sean letras.
            if i <= 1 or i >= 5:
                if matricula[i].isalpha():
                    contador += 1
            
            # Se valida que los caracteres del 4 al 6 sean números.
            elif i >= 2 and i <= 4:
                if matricula[i].isnumeric():
                    contador += 1
        
        
        if contador == 7:
            return True
        else:
            return False
    else:
        return False

print(validar_matricula(input('Ingrese la matrícula: ')))