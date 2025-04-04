# servicio_peliculas.py
import os
from catalogo_peliculas.pelicula import Pelicula

class ServicioPeliculas:
    def __init__(self, nombre_archivo="peliculas.txt"):
        self.__nombre_archivo = nombre_archivo  # Atributo privado
        self.__peliculas = []  # Atributo privado
        self.__cargar_peliculas()

    def __cargar_peliculas(self):
        try:
            with open(self.__nombre_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    pelicula = Pelicula(nombre)
                    self.__peliculas.append(pelicula)
        except FileNotFoundError:
            print("No se encontró el archivo de películas. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar las películas: {e}")

    def agregar_pelicula(self, pelicula):
        if not isinstance(pelicula, Pelicula):
            raise TypeError("Solo se pueden agregar objetos de tipo Pelicula.")
        self.__peliculas.append(pelicula)
        self.__guardar_peliculas()

    def listar_peliculas(self):
        if not self.__peliculas:
            print("No hay películas en el catálogo.")
        else:
            for pelicula in self.__peliculas:
                print(pelicula)

    def eliminar_archivo_peliculas(self):
        try:
            os.remove(self.__nombre_archivo)
            self.__peliculas = []
            print(f"Archivo {self.__nombre_archivo} eliminado.")
        except FileNotFoundError:
            print(f"El archivo {self.__nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al eliminar el archivo: {e}")

    def __guardar_peliculas(self):
        try:
            with open(self.__nombre_archivo, "w", encoding="utf-8") as archivo:
                for pelicula in self.__peliculas:
                    archivo.write(pelicula.get_nombre() + "\n")
        except Exception as e:
            print(f"Error al guardar las películas: {e}")

    # Getter para obtener una copia de la lista de películas
    def get_peliculas(self):
        return self.__peliculas[:]  # Devuelve una copia para evitar modificaciones externas
