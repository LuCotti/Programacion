class Persona:
    # Atributos
    def __init__(self, altura: float, peso: float, nombre: str, edad: int, fecha_nacimiento):
        self.altura = altura
        self.peso = peso
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
    
    # Métodos
    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}.')

ana = Persona(1.65, 53.6, 'Ana', 34, '19901025')
print(ana.nombre)
ana.saludar()

# lista = [1, 2, 3, 4, 5, 6]
# lista.

