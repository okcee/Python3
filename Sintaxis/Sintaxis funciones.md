**print()**  
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
* objects: Son los objetos que se desean imprimir. Pueden ser uno o varios objetos separados por comas.
  * Permite imprimir cualquier tipo de objeto: cadenas, números, listas, diccionarios, etc.
    * Cadenas de texto (strings): print("Hola, mundo!")
    * Números enteros (integers) y decimales (floats): print(10) o print(3.1416)
    * Listas: mi_lista = [1, 2, 3, "cuatro", 5.0] --> print(mi_lista)
    * Tuplas: mi_tupla = (10, "veinte", 30.0) --> print(mi_tupla)
    * Diccionarios: mi_diccionario = {"nombre": "PyMentor", "edad": "indefinida", "lenguaje": "Python"} --> print(mi_diccionario)
    * Conjuntos (sets): mi_conjunto = {1, 2, 3, 4, 5} --> print(mi_conjunto)
    * Variables: nombre = "PyMentor" --> edad = 0
    * Diferentes tipos de objetos: 
      * ```python
        nombre = "PyMentor"
        edad = 0
        lista_cursos = ["Python básico", "Python intermedio"]
        print("Nombre:", nombre, "Edad:", edad, "Cursos:", lista_cursos)```
    * Incluir marcadores de posición o variables dentro de una cadena de texto { f-strings (cadenas f).}:
      * ```python
        f"cadena de texto {expresión}":
        nombre = "PyMentor"
        edad = 0
        print(f"El nombre es {nombre} y la edad es {edad}.")```

print("El nombre es:", nombre, "y la edad es:", edad)
  * Si se pasan varios objetos, se imprimen en el orden en que se proporcionan.
* sep=' ': Es el separador entre los objetos impresos. Por defecto, es un espacio en blanco.
* end='\n': Es el carácter que se imprime al final de la línea. Por defecto, es un salto de línea.
* file=sys.stdout: Es el objeto donde se escribe la salida. Por defecto, es la salida estándar (la consola).
* flush=False: Indica si se fuerza el vaciado del buffer de salida.

**input()**  
input([prompt]) --> input("Por favor, ingresa tu edad: ")
```python
variable = tipo_de_dato(input("Mensaje opcional: "))
```
* variable: El nombre de la variable donde se almacenará el valor convertido.
* tipo_de_dato: El tipo de dato al que deseas convertir la entrada (por ejemplo, int, float).
* input("Mensaje opcional: "): La función input() que solicita la entrada del usuario. El "Mensaje opcional" es un texto que se muestra al usuario antes de que ingrese su dato.

Manejo de errores:  
Es importante tener en cuenta que si el usuario ingresa un valor que no se puede convertir al tipo de dato deseado, se producirá un error ValueError. Para evitar esto, puedes usar bloques try-except:  
```python
try:
    numero = int(input("Introduce un número entero: "))
    print("El número introducido es:", numero)
except ValueError:
    print("Error: Debes introducir un número entero válido.")
```

