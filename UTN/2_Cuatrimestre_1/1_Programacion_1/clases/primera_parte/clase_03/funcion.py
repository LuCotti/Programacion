def calcular_precio_con_iva(valor_sin_iva, iva=21):
    '''Documentación'''
    resultado = valor_sin_iva * (1 + (iva / 100))
    return resultado