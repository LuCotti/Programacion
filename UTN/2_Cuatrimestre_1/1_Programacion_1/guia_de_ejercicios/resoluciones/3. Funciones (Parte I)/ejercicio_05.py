# 5. Define una función que encuentre el máximo de tres números. La función
# debe aceptar tres argumentos y devolver el número más grande.

def maximo(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    else:
        mayor = num3
    return mayor

print(maximo(-1,0,1))