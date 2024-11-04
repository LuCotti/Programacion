# Clase
class Perro:
    # Definiendo atributos
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color
    
    # Métodos
    def ladrar(self):
        print('¡GUAU!')

mi_perro = Perro('Max', 5, 'Marrón')
print(mi_perro.nombre)
mi_perro.ladrar()