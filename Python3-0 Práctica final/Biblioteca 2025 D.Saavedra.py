'''Práctica Final del curso "Iniciación a la programación con Python (Enero-Marzo 2025)"
Hecho por: David Saavedra Varela - okcee@hotmail.com'''

'''Script formato Python (.py) que permite registrar libros y gestionar préstamos a usuarios.'''
'''Estructura del Código:
Toda la gestión se realiza dentro de una sola clase, Libro, con atributos de clase y métodos de clase. Además, se tiene en cuenta que el atributo "biblioteca" debe estar declarado y gestionado en la propia clase Libro.

    - Clase Libro:
        -Atributos de instancia: titulo, autor, isbn, disponible.
        - Atributo de clase: biblioteca (lista vacía inicialmente).
        - Métodos de instancia:
            • __init__(self, titulo, autor, isbn): Constructor que inicializa los atributos y agrega el libro a la biblioteca.
            • prestar(self): Cambia el estado disponible a False.
            • devolver(self): Cambia el estado disponible a True.
            • mostrar(self): Muestra la información del libro.
        - Métodos de clase: Un método de clase que pertenece a la clase en lugar de a una instancia específica de la clase. Operan sobre la clase en sí misma.
            • agregar(cls, titulo, autor, isbn, disponible=True): Crea una instancia de Libro y la agrega a biblioteca (aunque el constructor ya lo hace). Se puede usar como alternativa o para validaciones, dando más flexibilidad al código.
            • mostrar_todos(cls): Muestra todos los libros en biblioteca.
            • buscar(cls, isbn): Busca un libro en biblioteca por su ISBN.
    - Programa Principal:
        - Bucle while para el menú.
        - Llamadas a los métodos de clase de Libro para gestionar el inventario.
        - Validaciones y manejo de errores.
        - Se instanciarán objetos de la clase Libro a través de la opción de "Agregar libro".
'''

class Libro:
    """
    Clase Libro: Gestiona los libros de la biblioteca.
    """
    biblioteca = []  # Atributo de clase: lista para almacenar los libros. Inicialmente estará vacía.

    def __init__(self, titulo, autor, isbn, disponible=True):
        """
        Constructor: Inicializa los atributos del libro y lo agrega a la biblioteca.
        """
        self.titulo = titulo # (str): El título del libro.
        self.autor = autor # (str): El autor del libro.
        self.isbn = isbn #(str): El ISBN del libro.
        self.disponible = disponible  # (bool): Indica si el libro está disponible para préstamo (inicialmente True).
        Libro.biblioteca.append(self)  # Agrega el libro a la lista de la biblioteca.

    def prestar(self):
        """
        Cambia el estado de disponibilidad a False si está disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para prestar.")

    def devolver(self):
        """
        Cambia el estado de disponibilidad a True si está prestado.
        """
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def mostrar(self):
        """
        Muestra los datos del libro y su estado de disponibilidad.
        """
        estado = "Sí" if self.disponible else "No"
        print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}")

    @classmethod
    def agregar(cls, titulo, autor, isbn, disponible=True):  # Se incluye el atributo disponible
        """
        Método de clase: Crea un nuevo libro y lo añade a la biblioteca.
        """
        nuevo_libro = cls(titulo, autor, isbn, disponible) # Se crea una nueva instancia de la clase Libro.
        #Se podría añadir más código para realizar validaciones.
        return nuevo_libro

    @classmethod
    def mostrar_todos(cls):
        """
        Método de clase: Muestra todos los libros en la biblioteca.
        """
        if not cls.biblioteca:
            print("No hay libros en la biblioteca.")
        else:
            for libro in cls.biblioteca:
                print(libro.mostrar())  # Llamamos a print con el valor devuelto por mostrar()

    @classmethod
    def buscar(cls, isbn):
        """
        Método de clase: Busca un libro por ISBN y lo muestra.
        """
        for libro in cls.biblioteca:
            if libro.isbn == isbn:
                libro.mostrar()
                return libro #Devuelve el libro encontrado para poder usarlo
        print(f"No se encontró ningún libro con el ISBN '{isbn}'.")
        return None #Devuelve None si no se ha encontrado ningún libro


# Programa Principal
while True:
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar todos los libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        Libro.agregar(titulo, autor, isbn)
        print(f"Libro '{titulo}' agregado con éxito.")
    elif opcion == '2':
        isbn = input("Ingresa el ISBN: ")
        libro_encontrado=Libro.buscar(isbn)
        if libro_encontrado:
            libro_encontrado.prestar()
        else:
            print("No se puede prestar el libro porque no se encontró.")
    elif opcion == '3':
        isbn = input("Ingresa el ISBN: ")
        libro_encontrado=Libro.buscar(isbn)
        if libro_encontrado:
            libro_encontrado.devolver()
        else:
            print("No se puede devolver el libro porque no se encontró.")
    elif opcion == '4':
        Libro.mostrar_todos()
    elif opcion == '5':
        isbn = input("Ingresa el ISBN: ")
        Libro.buscar(isbn)
    elif opcion == '6':
        print("¡Gracias por usar el Sistema de Gestión de Biblioteca!")
        break
    else:
        print("Opción inválida. Por favor, elige una opción del menú.")
