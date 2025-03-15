'''
Ejemplo Herencia
En esta ocasión vamos a crear una clase Vehículo de la que heredará una clase Moto y que a su vez será padre de una clase Kwad, es decir, gráficamente sería algo como:
'''
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "negro"
        self.arrancado = Falseself.parado = True
        
    def arrancar(self):
        self.arrancado = True
        self.parado = False
    def parar(self):
        self.parado = True
        self.arrancado = False
    def resumen(self):
        print("El modelo es un coche", "\n", "Marca:", self.marca, "\n", "Modelo:", self.modelo, "\n",
              "Color:", self.color, "\n", "Está arrancado:", self.arrancado,"\n", "Está parado:", self.parado
)
miCoche = Vehiculo("Renault", "Megane")
miCoche.arrancar()
miCoche.resumen()
class Moto(Vehiculo):
    is_carenado = False
#Método propio de la clase Moto, no heredado del padre.
def poner_carenado(self):
    self.is_carenado = True
#La clase Moto sobrescribe el método resumen() heredado del padre
def resumen(self):
    print("El modelo es una moto", "\n", "Marca:", self.marca, "\n", "Modelo:", self.modelo, "\n",
          "Color:", self.color, "\n", "Está arrancado:", self.arrancado,"\n", "Está parado:",
          self.parado, "\n", "Tiene carenado:", self.is_carenado)
miMoto = Moto("Kawasaki", "Ninja")
miMoto.resumen()
class kwad(Moto):
    pass
miKwad = kwad("Linhai", "LH 500")
miKwad.resumen()

'''
Super()
'''
class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas) #Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)

'''
Ejemplo de encapsulación simulada de Python

En el siguiente ejemplo hemos creado una clase Coche con una serie de atributos privados: largo, ancho, ruedas, peso, color, is_enMarcha. En otro lenguaje de programación con encapsulación real no podríamos cambiar los valores de dichos atributos
'''
class Coche: # Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False
# Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"
# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = Coche()
miCoche.__ruedas = 9
print("Mi coche tiene", miCoche.__ruedas, "ruedas.")

'''
Ejemplo de Poliformismo
En este ejemplo estamos, primero definiendo la clase
Cuadrado, que hereda de Poligono. Creamos una
tupla con dos Triangulo y un Cuadrado y
recorriéndola con un bucle for. Como vemos,
llamamos al método show de cada elemento de la
tupla. Como es lógico, cada llamada produce el
resultado específico para el tipo de polígono al que
pertenece. Notad que esto en Python es trivial ya
que siempre tratamos directamente con referencias
a objetos, así que la llamada a show es siempre la
correspondiente a la del objeto referenciado.
'''
class Cuadrado(Poligono):
    def __init__(self, lado, color=None):
        Poligono.__init__(self,4,color)
        self.lado = lado
    def show(self):
        super().show()
        print('lado:', self.lado)
c1 = Cuadrado(2, 'verde') #Declaramos un cuadrado
poligonos = t1, t2, c1 #Tupla con dos Trinagulos y un Cuadrado
for poligono in poligonos:
    poligono.show()
    print()