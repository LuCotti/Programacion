'''3. Crear una función que reciba como parámetro un vector de números enteros. La
función debe mostrar los números negativos de forma decreciente y luego los
positivos de forma creciente.
Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de
estructuras repetitivas.'''
vector = [-3, 1, 3, -4, -5, -2, 5, 4, -1, 2]
def ordenar(vector):
    for i in range(len(vector)):
        minimo = vector[i]
        posicion_minimo = i
        for j in range(i + 1, len(vector)):
            if vector[j] < minimo:
                minimo = vector[j]
                posicion_minimo = j
        
        auxiliar = vector[i]
        vector[i] = minimo
        vector[posicion_minimo] = auxiliar
    
    for i in range((len(vector) // 2) - 3):
        if vector[i] < 0:
            auxiliar = vector[i]
            vector[i] = vector[-i - 6]
            vector[-i - 6] = auxiliar
    
    
    return vector

print(ordenar(vector))