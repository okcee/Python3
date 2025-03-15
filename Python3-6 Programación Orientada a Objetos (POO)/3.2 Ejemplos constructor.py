# En este ejemplo, el constructor __init__ inicializa los atributos marca, modelo y color de la instancia mi_coche.

class Coche:
    # Definición de la clase Coche
    # Esta clase servirá como plantilla para crear objetos de tipo coche

    def __init__(self, marca, modelo, color):
        # Definición del constructor __init__
        # El constructor se llama automáticamente al crear una nueva instancia de la clase Coche
        # 'self' se refiere a la instancia del objeto que se está creando
        # 'marca', 'modelo' y 'color' son los parámetros para inicializar los atributos del coche

        self.marca = marca
        # Asigna el valor del parámetro 'marca' al atributo 'marca' de la instancia
        self.modelo = modelo
        # Asigna el valor del parámetro 'modelo' al atributo 'modelo' de la instancia
        self.color = color
        # Asigna el valor del parámetro 'color' al atributo 'color' de la instancia

    def mostrar_datos(self):
        # Definición del método mostrar_datos
        # Este método imprime los datos del coche (marca, modelo y color)
        # 'self' se refiere a la instancia del objeto

        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")
        # Utiliza un f-string para formatear la cadena de texto con los valores de los atributos

mi_coche = Coche("Toyota", "Corolla", "Azul")
# Creación de una instancia de la clase Coche llamada 'mi_coche'
# Se pasan los valores "Toyota", "Corolla" y "Azul" al constructor para inicializar los atributos

mi_coche.mostrar_datos()
# Llamada al método mostrar_datos del objeto 'mi_coche'
# Esto imprime los datos del coche en la consola

del mi_coche #Eliminamos el objeto mi_coche de la memoria con un destructor.


'''¿Qué es un Constructor con Parámetros?
Un constructor con parámetros es un método __init__ que acepta argumentos (parámetros) cuando se crea una nueva instancia de una clase. Esto permite inicializar los atributos de la instancia con valores específicos proporcionados al momento de la creación.'''

class Coche:
    # Definición de la clase Coche

    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
        # Definición del constructor __init__ con parámetros
        # 'self' se refiere a la instancia del objeto que se está creando
        # 'largo', 'ancho', 'ruedas', 'peso', 'color', 'is_enMarcha' son los parámetros para inicializar los atributos

        self.largo = largo
        # Asigna el valor del parámetro 'largo' al atributo 'largo' de la instancia
        self.ancho = ancho
        # Asigna el valor del parámetro 'ancho' al atributo 'ancho' de la instancia
        self.ruedas = ruedas
        # Asigna el valor del parámetro 'ruedas' al atributo 'ruedas' de la instancia
        self.peso = peso
        # Asigna el valor del parámetro 'peso' al atributo 'peso' de la instancia
        self.color = color
        # Asigna el valor del parámetro 'color' al atributo 'color' de la instancia
        self.is_enMarcha = is_enMarcha
        # Asigna el valor del parámetro 'is_enMarcha' al atributo 'is_enMarcha' de la instancia

    # Declaración de dos instancias de clase pasándoles los parámetros requeridos en el constructor.
    coche_1 = Coche(400, 160, 4, 1200, "amarillo", True)
    # Se crea una instancia de la clase Coche llamada 'coche_1'
    # Se pasan los valores 400, 160, 4, 1200, "amarillo", True al constructor para inicializar los atributos

    coche_2 = Coche(420, 150, 4, 1500, "verde", False)
    # Se crea una instancia de la clase Coche llamada 'coche_2'
    # Se pasan los valores 420, 150, 4, 1500, "verde", False al constructor para inicializar los atributos

    print(f"Coche 1: Largo={coche_1.largo}, Color={coche_1.color}, En marcha={coche_1.is_enMarcha}")
    print(f"Coche 2: Largo={coche_2.largo}, Color={coche_2.color}, En marcha={coche_2.is_enMarcha}")

'''
Explicación Detallada:

Definición del Constructor (__init__):

El constructor __init__ ahora acepta los parámetros largo, ancho, ruedas, peso, color y is_enMarcha.
Dentro del constructor, se asignan los valores de estos parámetros a los atributos correspondientes de la instancia utilizando self.
Creación de Instancias (coche_1, coche_2):

Al crear las instancias coche_1 y coche_2, se pasan los valores específicos para cada parámetro al constructor.
Esto permite crear coches con diferentes características iniciales.
Acceso a los Atributos:

Después de crear las instancias, se puede acceder a los atributos de cada coche utilizando la notación de punto (por ejemplo, coche_1.largo).
'''