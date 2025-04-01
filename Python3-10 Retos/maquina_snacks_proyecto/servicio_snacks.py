import os.path

from snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = "snacks.txt" # Definimos una variable constante y su valor inicial es la información de un archivo.
    
    def __init__(self): # Constructor, sin parámetros para crear una lista de snacks
        self.snacks = []
    
        # Revisar si ya existe el archivo snacks
        # Si ya existe, obtenemos los snacks del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO): # Accedemos al paquede O.S. mediante la variable path usando el método isfile()
            self.snacks = self.obtener_snacks()
        # Si no existe, cargamos algunos snacks iniciales
        else:
            self.cargar_snacks_iniciales()
    
    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack("Patatas", 70),
            Snack("Refresco", 50),
            Snack("Sandwich", 120)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
    
    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, "a ") as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f"Error al guardar los snacks en el archivo: {e}")

    
    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, "r") as archivo:
                for linea in archivo:
                    # Formato ID, "Nombre", Precio
                    id_snack, nombre, precio = linea.strip().split(",") # Se genera una tupla con los 3 valores del formato explicado
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
            return snacks
        except Exception as e:
            print(f"Error al obtener los snacks del archivo: {e}")
        return snacks
    
    def agreagar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack]) # Convierte 
    
    def mostrar_snacks(self):
        print("--- Lista de snacks en el inventario ---")
        for snack in self.snacks:
            print(snack)
    
    def get_snacks(self):
        return self.snacks
    
    