class Snack: # Definimos la clase Snack
    contador_snacks = 0 # Atributo de clase con valor inicial de 0
    
    def __init__(self, nombre="", precio=0.0): # Método constructor con parámetros con valores iniciales por defecto para que estos valores sean opcionales
        Snack.contador_snacks += 1 # Incrementamos el contador de snacks
        self.id_snack = Snack.contador_snacks # Accedemos a la variable de clase contador snacks
        self.nombre = nombre # Atributo de nombre (se podría aplicar encapsulamiento)
        self.precio = precio # Atributo de precio (se podría aplicar encapsulamiento)
    
    def __str__(self): # Definimos el método str de la clase object
        return (f'Snack: id_Snack = {self.id_snack}, nombre = {self.nombre}, precio = {self.precio}')
    
    def escribir_snack(self): # Definimos el método escribir_snack
        return f'{self.id_snack},{self.nombre},{self.precio}'
