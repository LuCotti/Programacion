class Libro:
    # Atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    # Métodos
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'Prestaste el libro {self.titulo}.')
        else:
            print(f'El libro {self.titulo} ya está prestado.')
    
    def devolver(self):
        self.disponible = True
        print(f'Devuelto el libro {self.titulo}.')
    
    def esta_disponible(self):
        return self.disponible
    
    def obtener_titulo(self):
        return self.titulo

# Test
# libro1 = Libro('Arte de la guerra', 'Sun Tzu')
# libro1.prestar()
# if libro1.esta_disponible():
#     print(f'El libro {libro1.titulo} está disponible.')
# else:
#     print(f'El libro {libro1.titulo} no está disponible.')
# libro1.devolver()
# if libro1.esta_disponible():
#     print(f'El libro {libro1.titulo} está disponible.')
# else:
#     print(f'El libro {libro1.titulo} no está disponible.')




class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'Libro agregado: {libro.obtener_titulo()}')
    
    def prestar_libro(self, titulo):
        for i in range(len(self.libros)):
            if self.libros[i].obtener_titulo() == titulo:
                if self.libros[i].esta_disponible():
                    self.libros[i].prestar()
                else:
                    print(f'El libro ya fue prestado.')
            else:
                print('El libro no se encuentra en la biblioteca.')
    
    def devolver_libro(self, titulo):
        for i in range(len(self.libros)):
            libro = self.libros[i]
            if libro.obtener_titulo() == titulo:
                if not libro.esta_disponible():
                    libro.devolver()
                else:
                    print('El libro no está prestado.')
                return
        print('El libro no se encuentra en la biblioteca.')
    
    def mostrar_libros(self):
        for i in range(len(self.libros)):
            libro = self.libros[i]
            print(f'Libro {i}: {libro.obtener_titulo()}')
    
    def mostrar_disponibles(self):
        pass

# Test
libro1 = Libro('Arte de la guerra', 'Sun Tzu')
libro2 = Libro('Python Para Todos', 'Anónimo')
biblioteca = Biblioteca()
# Coloco los libros en la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
# Prestar libro
biblioteca.prestar_libro('Python Para Todos')
# Mostrar
biblioteca.mostrar_libros()
