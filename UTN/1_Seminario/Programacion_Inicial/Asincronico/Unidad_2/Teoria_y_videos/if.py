num1 = int(input('Ingrese un número: '))

if num1 == 0:
    print(f'El número {num1} es neutro')
    num2 = int(input('Ingrese un número del 1 al 3: '))
    match num2:
        case 1:
            print('Desaprobado')
        case 2:
            print('Cagando')
        case 3:
            print('Aprobado')
        case _:
            print('¡¡¡DIJE QUE DEL 1 AL 3!!!')
elif num1 >= 0:
    print(f'El número {num1} es positivo')
else:
    print(f'El número {num1} es negativo')