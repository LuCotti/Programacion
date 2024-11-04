def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    
    return resultado

print(calcular_potencia(2, 5))