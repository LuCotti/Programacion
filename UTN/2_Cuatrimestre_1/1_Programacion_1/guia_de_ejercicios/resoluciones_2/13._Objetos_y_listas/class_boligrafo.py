class Boligrafo:
    def __init__(self, grosor_punta: str, color: str):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = 80
    
    def escribir(self, texto: str):
        match self.grosor_punta:
            case 'fino':
                if len(texto) <= self.cantidad_tinta:
                    self.cantidad_tinta -= len(texto)
                    print(texto)
                else:
                    print('No alcanza la tinta.')
            case 'grueso':
                if len(texto) * 2 <= self.cantidad_tinta:
                    self.cantidad_tinta -= len(texto) * 2
                    print(texto)
                else:
                    print('No alcanza la tinta.')
            case _:
                print('El grosor fue mal ingresado.')
        
        return self.cantidad_tinta
    
    def recargar(self, cantidad: int):
        self.cantidad_tinta += cantidad
        if self.cantidad_tinta > self.capacidad_tinta_maxima:
            tinta_sobrante = self.cantidad_tinta - self.capacidad_tinta_maxima
            print(f'Se recargó la lapicera {self.color} y sobró {tinta_sobrante} cantidad de tinta.')
            self.cantidad_tinta = self.capacidad_tinta_maxima
        else:
            print(f'Lapicera {self.color} recargada')
        return self.cantidad_tinta
    
    def mostrar_datos(self):
        print(f'Tengo un grosor {self.grosor_punta}, soy de color {self.color} y me queda {self.cantidad_tinta} cantidad de tinta.')

lista_1 = ['manzana', 'pera', 'banana']
lista_2 = []
# print(lista_1)
# print(lista_1.pop(1))
# print(lista_1)
print(lista_1)
print(lista_2)
lista_2.append(lista_1.pop(1))
print(lista_1)
print(lista_2)