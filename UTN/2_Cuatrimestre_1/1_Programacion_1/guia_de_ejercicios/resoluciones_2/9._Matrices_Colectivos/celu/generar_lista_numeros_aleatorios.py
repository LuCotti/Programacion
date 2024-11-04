import random
def generar_legajos(cantidad_legajos):
    lista_legajos = []
    for i in range(cantidad_legajos):
        lista_legajos += [random.randint(1, 99)]
    
    return lista_legajos

print(generar_legajos(15))