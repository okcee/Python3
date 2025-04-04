# pelicula.py
class Pelicula:
    def __init__(self, nombre):
        # Atributo privado: se indica con el prefijo __
        self.__nombre = nombre  # Ahora es un atributo privado

    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para el nombre (con validación)
    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre

    def __str__(self):
        return f"Película: {self.__nombre}"
