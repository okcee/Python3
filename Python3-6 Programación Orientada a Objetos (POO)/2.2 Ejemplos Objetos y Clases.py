# Un pequeño ejemplo en codigo:

class Perro:
    def __init__(self, raza, edad, color):
        self.raza = raza
        self.edad = edad
        self.color = color

    def ladrar(self):
        print("¡Guau, guau!")

mi_perro = Perro("Labrador", 3, "Dorado")

print(f"Mi perro es un {mi_perro.raza} de {mi_perro.edad} años y color {mi_perro.color}.")
mi_perro.ladrar()

'''En este ejemplo, Perro es una clase (que veremos en profundidad después), y mi_perro es un objeto de esa clase. El objeto mi_perro tiene atributos (raza, edad, color) y un método (ladrar).'''


'''
Ejemplo de creación de clase e instanciación de objetos de en la siguiente clase.
1. Crearemos una clase Usuario que tendrá los siguientes atributos:
• nombre : string
• edad : number
• login : string
• password : string
• email : string
• telefono : number
2. Y los siguientes métodos:
• Resumen(): Sacará un resumen de los datos del usuario
• cambiaEdad(): Nos dará la posibilidad de pedir al usuario que introduzca una nueva edad.
• muestraEdad(): Nos mostrará la edad del usuario
Por último, crearemos una instancia de la clase Usuario a la que llamaremos administrador y llamaremos a los métodos de la clase Usuario para este administrador usando la nomenclatura del punto.
'''

# CREACIÓN DE LA CLASE USUARIO
class Usuario():
    # Declaración de atributos (variables de instancia)
    # Estos atributos almacenan los datos de cada objeto Usuario
    nombre = "Angel"  # Atributo para el nombre del usuario (cadena de texto)
    edad = 47          # Atributo para la edad del usuario (número entero)
    login = "admin"    # Atributo para el nombre de usuario (cadena de texto)
    password = "1234"  # Atributo para la contraseña del usuario (cadena de texto)
    email = "angel@loquesea.com" # Atributo para el correo electrónico del usuario (cadena de texto)
    telefono = 666666666 # Atributo para el teléfono del usuario (número entero)

    # Declaración de métodos (funciones de la clase)
    # Estos métodos definen las acciones que los objetos Usuario pueden realizar

    def resumen(self):  # Método para mostrar un resumen de la información del usuario
        # 'self' es una referencia a la instancia actual del objeto Usuario
        # Permite acceder a los atributos del objeto dentro del método
        print(f'Los datos del usuario son:\n'
              f'Nombre: {self.nombre}\n'
              f'Edad: {self.edad}\n'
              f'Login: {self.login}\n'
              f'Password: {self.password}\n'
              f'Email: {self.email}\n'
              f'Teléfono: {self.telefono}')

    def cambiaEdad(self):  # Método para cambiar la edad del usuario
        # Solicita al usuario que introduzca una nueva edad
        edadIntroducida = int(input("Introduce edad entre 18-100:"))
        # Valida que la edad introducida esté dentro del rango permitido
        if 18 < edadIntroducida < 100:
            self.edad = edadIntroducida  # Actualiza el atributo 'edad' con el nuevo valor
            print("Edad introducida correcta")
            return "" #retorna un string vacio.
        else:
            print("La edad introducida no es correcta.")
            self.cambiaEdad() #llama de manera recursiva a la funcion cambiaEdad hasta que se introduzca un valor correcto.
            return "" #retorna un string vacio.

    def muestraEdad(self):  # Método para mostrar la edad actual del usuario
        print('La edad del usuario es:', self.edad, 'años.')
        return "" #retorna un string vacio.

# Creación de una instancia de la clase Usuario
# 'administrador' es un objeto (instancia) de la clase Usuario
administrador = Usuario()

# Una vez creado el objeto administrador,
# hacemos uso del método “resumen()” perteneciente a la clase Usuario
administrador.resumen()

# Usamos los métodos cambiaEdad() y muestraEdad() de la clase Usuario.
print(administrador.cambiaEdad())
print(administrador.muestraEdad())

# Si ejecutamos el programa, primero nos mostrará los datos del usuario,
# luego nos pedirá que introduzcamos la nueva edad y finalmente nos mostrará la edad introducida.