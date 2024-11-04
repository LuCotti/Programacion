'''Desarrollo de una función para Validar Políticas de Contraseñas:

Desarrolla una función en Python que valide si una contraseña cumple con una
política de seguridad específica. La función debe recibir una contraseña como
argumento y devolver un valor que indique si la contraseña cumple o no con las
políticas definidas.

Política de Contraseñas:
La contraseña debe cumplir con los siguientes requisitos:
    • Tener al menos 8 caracteres.
    • Contener al menos una letra mayúscula.
    • Contener al menos una letra minúscula.
    • Contener al menos un número.'''

def validar_contraseña(contraseña):
    # La contraseña debe Tener al menos 8 caracteres.
    if len(contraseña) >= 8:
        # Definición de contadores en 0.
        contador_mayusculas = 0
        contador_minusculas = 0
        contador_numeros = 0
        for i in range(len(contraseña)):
            # La contraseña debe contener al menos una letra mayúscula.
            if contraseña[i].isupper():
                contador_mayusculas += 1
            
            # La contraseña debe contener al menos una letra minúscula.
            if contraseña[i].islower():
                contador_minusculas += 1
            
            # La contraseña debe contener al menos un número.
            if contraseña[i].isdigit():
                contador_numeros += 1
        
        if contador_mayusculas > 0 and contador_minusculas > 0 and contador_numeros > 0:
            return True
        else:
            return False
    else:
        return False


print(validar_contraseña(input('ingrese la contraseña: ')))