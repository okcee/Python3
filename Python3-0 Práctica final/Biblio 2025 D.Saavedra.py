'''Práctica Final del curso "Iniciación a la programación con Python (Enero-Marzo 2025)"
Hecho por: David Saavedra Varela - okcee@hotmail.com'''

'''Script formato Python (.py) que permite registrar libros y gestionar préstamos a usuarios.'''

class Libro: # Crea una nueva instancia para la clase Libro (Método constructor).
    """
    Clase Libro
    Atributos:
    - titulo (str)
    - autor (str)
    - isbn (str)
    - disponible (bool, inicialmente True)
    Métodos:
    - agregar() que permita introducir un nuevo libro con sus características.
    - prestar() que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado.
    - devolver() que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible.
    - mostrar() que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos y diga si estás disponible o no.
    - buscar() que busque un libro en concreto por su ISBN y lo muestre en pantalla con todos sus datos y diga si está disponible o no."""
    
    def __init__(self, titulo, autor, isbn, disponible=True): # Inicializa los atributos de la instancia.
        
        self.titulo = titulo # Atributo 1 (str)
        self.autor = autor # Atributo 2 (str)
        self.isbn = isbn # Atributo 3 (str)
        self.disponible = disponible # Atributo 4 (bool: True)
        
        """
        Método agregar: 
        """
        
        """
        Método prestar: cambia el estado de disponible a False si el libro está disponible, y muestra un mensaje si ya está prestado.
        """
        def prestar(self): # Verifica si el libro está disponible (self.disponible == True).
            if self.disponible:
                self.disponible = False # Si está disponible cambia el estado a False.
                print(f"El libro '{self.titulo}' ha sido prestado.")
            else:
                print(f"El libro '{self.titulo}' ya está prestado.")
        
        """
        Método devolver: cambia el estado de disponible a True si estaba prestado, y muestra un mensaje si ya estaba disponible.
        """
        def devolver(self): # Verifica si el libro no está disponible (self.disponible == False).
            if not self.disponible:
                self.disponible = True # Si no está disponible cambia el estado a True.
                print(f"El libro '{self.titulo}' ha sido devuelto.")
            else:
                print(f"El libro '{self.titulo}' ya estaba disponible.")
        
        """
        Método mostrar: devuelve una lista con todos los libros de la biblioteca y los muestra en pantalla con todos sus datos y dice si están disponibles o no (prestado).
        """
        def mostrar(self):
            estado = "disponible" if self.disponible else "prestado" # Usa una expresión condicional (if ... else) para determinar si el libro está disponible o no.
            print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}") # Muestra los datos del libro en un formato claro y legible.
        
        """
        Método buscar: busca un libro en concreto por su ISBN y lo muestra en pantalla con todos sus datos y dice si está disponible o no.
        """
        def buscar(self, isbn):
            if self.isbn == isbn:
                self.mostrar()
            else:
                print(f"No se encontró ningún libro con el ISBN '{isbn}'.")

# Lista para almacenar los objetos de la clase Libro
inventario_libros = []

""" Implementar el bucle de interacción con el usuario y el menú"""

while True: # Este bucle while True se ejecutará continuamente hasta que se encuentre la instrucción break.
    print("\nBienvenido al Sistema de Gestión de Biblioteca") # Se muestra el menú de opciones al usuario.
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar todos los libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        # Lógica para agregar un nuevo libro
        pass  # Las opciones las implementaremos más adelante.
    elif opcion == '2':
        # Lógica para prestar un libro.
        pass
    elif opcion == '3':
        # Lógica para devolver un libro.
        pass
    elif opcion == '4':
        # Lógica para mostrar todos los libros.
        pass
    elif opcion == '5':
        # Lógica para buscar un libro por ISBN.
        pass
    elif opcion == '6':
        print("¡Gracias por usar el Sistema de Gestión de Biblioteca!")
        break  # Sale del bucle y termina el programa.
    else:
        print("Opción inválida. Por favor, elige una opción del menú.")

"""Implementar la lógica para cada opción del menú"""
"""Agregar un nuevo libro (opción '1'):"""

