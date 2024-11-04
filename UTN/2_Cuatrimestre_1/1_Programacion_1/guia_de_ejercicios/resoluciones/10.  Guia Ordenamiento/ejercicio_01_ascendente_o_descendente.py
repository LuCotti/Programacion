'''1. Crear una función llamada ordenar_vector que reciba como parámetro un vector
de números enteros y lo ordene de forma ascendente. La función debe implementar
como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro
opcional debe recibir un booleano (que por default está en False), que en caso de
ser True ordena el vector en forma descendente.'''
vector = [33, 10, 59, 270, 1, 90, 50]
def ordenar_vector(vector, bool= False):
    if bool == False:
        bandera_cambio = 0
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                auxiliar = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = auxiliar
                bandera_cambio = 1
        if bandera_cambio > 0:
            ordenar_vector(vector)
        else:
            return vector
    else:
        bandera_cambio = 0
        for i in range(len(vector) - 1):
            if vector[i] < vector[i + 1]:
                auxiliar = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = auxiliar
                bandera_cambio = 1
        if bandera_cambio > 0:
            ordenar_vector(vector, bool)
        else:
            return vector


# print(ordenar_vector(vector)) - No funcionaría en este caso porque en el if de la línea 28 no hay return (solo lo hay para el else), por lo tanto todas las veces que
# se cumpla esa condición, la función devolverá None. Como resultado, se imprimiría None en la consola.
ordenar_vector(vector)
print(vector)