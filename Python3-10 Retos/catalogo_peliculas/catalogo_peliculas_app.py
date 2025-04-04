from catalogo_peliculas.pelicula import Pelicula
from catalogo_peliculas.servicio_peliculas import ServicioPeliculas

class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('*** App Catálogo Películas ***')
        while True:
            try:
                print(f'''Opciones:
                1. Agregar Película
                2. Listar Películas
                3. Eliminar catálogo de películas
                4. Salir''')
                opcion = int(input('Escribe tu opción (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Introduce el nombre de la película: ')
                    # Usamos el setter para crear la pelicula
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Salimos del programa...')
                    break
                else:
                    print('Opción inválida, Introduce un valor entre 1 y 4.')
            except ValueError:
                print('Error: Introduce un número válido.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')

if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()

'''
Función del bloque de código de if __name__ == '__main__':
Punto de Entrada: Define el punto de entrada principal de la aplicación. Cuando ejecutas python catalogo_peliculas_app.py, este es el código que se ejecuta primero.
Inicialización: Crea una instancia de la aplicación (app). Esto implica la creación de un objeto ServicioPeliculas dentro de la instancia de AppCatalogoPeliculas.
Inicio de la Interfaz: Llama al método mostrar_menu(), que inicia la interfaz de usuario de la aplicación, mostrando el menú y permitiendo al usuario interactuar con el catálogo de películas.
Protección de Ejecución: Asegura que la aplicación solo se inicie cuando se ejecuta directamente el archivo. Si se importara la clase AppCatalogoPeliculas en otro archivo, la aplicación no se iniciaría automáticamente. Esto permite reutilizar la clase en otros proyectos sin que se ejecute la interfaz de usuario.

En resumen:
El bloque if __name__ == '__main__': es una práctica común en Python para organizar el código y definir el punto de entrada de un script. En este caso, asegura que la aplicación del catálogo de películas se inicie correctamente cuando se ejecuta el archivo catalogo_peliculas_app.py directamente, creando la instancia de la aplicación y mostrando el menú al usuario. Espero que esta explicación detallada te haya aclarado la función de este bloque de código.
'''