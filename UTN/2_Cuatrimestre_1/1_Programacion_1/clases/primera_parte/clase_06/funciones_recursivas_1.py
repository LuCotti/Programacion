# ´MI CÓDIGO
# def potencia(base, exponente):
#     potencia = base
    
    
    
    
    
    
    
    
    
    
    





# CÓDIGO DE MARTIN DELLA MONICA (NO ES RECURSIVA)
def potencia_de_numero (base, exponente):
    potencia = 1
    for i in range (1, exponente + 1):
        potencia *= base
    return potencia

print(potencia_de_numero(2, 3))





# CÓDIGO DE PABLO CONDE (BUEN CÓDIGO)
def calcular_potencia(base:int,exponente:int)->int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

print(calcular_potencia(2, 4))