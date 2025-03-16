# Sintaxis Completa de una Clase en Python

```Python
class NombreDeLaClase(ClasePadre1, ClasePadre2, ...):
    """
    Documentación de la clase: Describe el propósito y funcionamiento de la clase.
    """

    # Atributos de clase (compartidos por todas las instancias de la clase)
    variable_de_clase = valor_inicial

    # Método constructor (se llama al crear una nueva instancia)
    def __init__(self, parametro1, parametro2, ...):
        """
        Documentación del método __init__. Inicializa los atributos del objeto.
        """
        # Atributos de instancia (propios de cada objeto)
        self.atributo1 = parametro1
        self.atributo2 = parametro2
        # ... otras inicializaciones

    # Otros métodos de instancia (acciones que los objetos pueden realizar)
    def metodo1(self, otro_parametro):
        """
        Documentación del método metodo1. Describe lo que hace este método.
        """
        # Lógica del método
        resultado = self.atributo1 + otro_parametro
        return resultado

    def metodo2(self):
        """
        Documentación del método metodo2.
        """
        # ... más lógica

    # Métodos de clase (operan sobre la clase en sí misma)
    @classmethod
    def metodo_de_clase(cls, argumento):
        """
        Documentación del método de clase.
        """
        # Lógica del método de clase (usa 'cls' en lugar de 'self')
        return cls.variable_de_clase + argumento

    # Métodos estáticos (asociados a la clase pero no acceden a sus atributos ni a la instancia)
    @staticmethod
    def metodo_estatico(parametro):
        """
        Documentación del método estático.
        """
        # Lógica del método estático
        return "Resultado: " + str(parametro)

    # Métodos especiales (con nombres predefinidos que Python utiliza para ciertas operaciones)
    def __str__(self):
        """
        Define cómo se representa el objeto como una cadena (para print()).
        """
        return f"Objeto de la clase {self.__class__.__name__} con atributo1: {self.atributo1}"

    def __repr__(self):
        """
        Define una representación "oficial" del objeto (para desarrollo y debugging).
        """
        return f"<{self.__class__.__name__}(atributo1={self.atributo1}, atributo2={self.atributo2})>"

    # ... otros métodos especiales como __len__, __getitem__, __setitem__, etc. 
```