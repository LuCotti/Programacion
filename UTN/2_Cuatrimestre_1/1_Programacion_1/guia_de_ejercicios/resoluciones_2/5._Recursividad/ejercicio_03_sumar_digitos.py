def sumar_digitos(numero: int)-> int:
    if numero < 10:
        resultado = numero
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)
    
    return resultado

print(sumar_digitos(12345))
