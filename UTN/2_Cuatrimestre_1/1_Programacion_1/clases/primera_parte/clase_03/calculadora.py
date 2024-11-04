# Funciones
def sumar(numero1, numero2):
    calculo = numero1 + numero2
    return calculo

def restar(numero1, numero2):
    calculo = numero1 - numero2
    return calculo

def multiplicar(numero1, numero2):
    calculo = numero1 * numero2
    return calculo

def dividir(numero1, numero2):
    calculo = numero1 / numero2
    return calculo


# Bucle
continuar = 'si'

while continuar != 'F':
    print('Calculadora básica.')
    operador = input('Ingrese el operador (+, -, *, /): ')
    operando1 = float(input('Ingrese el primer operando: '))
    operando2 = float(input('Ingrese el segundo operando: '))
    
    match operador:
        case '+':
            calculo = sumar(operando1, operando2)
        case '-':
            calculo = restar(operando1, operando2)
        case '*':
            calculo = multiplicar(operando1, operando2)
        case '/':
            calculo = dividir(operando1, operando2)
        case _:
            print('Operador inválido.')
    
    print(calculo)
    
    continuar = input('¿Desea continuar operando? (F para finalizar) ')

