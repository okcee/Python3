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
        print(f"El nombre es {nombre} y la edad es {edad}.")
  * El método .lower() convierte todos los caracteres de la cadena almacenada en name a minúsculas.
  * El método .upper() convierte todos los caracteres de la cadena almacenada en name a mayúsculas.
  * El método .title() convierte la cadena almacenada en name al formato de título, donde la primera letra de cada palabra se convierte en mayúscula y el resto en minúscula.
```


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

**round()**  
round(number[, ndigits])  
* number: Es el número que se desea redondear. Puede ser un número entero o un número de punto flotante.
* ndigits (opcional): Es el número de dígitos decimales a los que se desea redondear.
* Si ndigits se omite o es None, la función redondea el número al entero más cercano.
* Si ndigits es un número entero positivo, la función redondea el número a esa cantidad de dígitos decimales.
* Si ndigits es un número entero negativo, la función redondea el número a esa cantidad de dígitos a la izquierda del punto decimal.

**for**  
*Estructura básica*  
for variable in iterable: # cuerpo del bucle  
* *for* variable *in* iterable::
* *for*: Palabra clave que inicia el bucle.
* *variable*: Es el nombre de la variable que tomará el valor de cada elemento del iterable en cada iteración.
* *in*: Palabra clave que conecta la variable con el iterable.
* *iterable*: Es cualquier objeto que pueda devolver sus elementos uno a la vez. Ejemplos comunes son:
  * Listas: frutas = ["manzana", "banana", "cereza"]
  * Tuplas: coordenadas = (3, 5)
  * Cadenas: mensaje = "Hola"
  * Diccionarios: persona = {"nombre": "Ana", "edad": 30}
  * Objetos range: range(inicio, fin, paso)

*Control del bucle*  
* break: Sale del bucle prematuramente.
* continue: Salta la iteración actual y pasa a la siguiente.
* else: Se ejecuta si el bucle termina sin ser interrumpido por break.

**len(objeto)**  
El método len() en Python se utiliza para determinar la longitud de un objeto, como una cadena, una lista, una tupla o un diccionario.  
len() es una función incorporada en Python, lo que significa que está disponible sin necesidad de importar ningún módulo.  

**split()**  
cadena.split(separador, maxsplit) --> lista = cadena.split(",", 2)  
* cadena: La cadena que deseas dividir.
* separador (opcional): El delimitador que se utiliza para dividir la cadena. Si no se especifica, el separador predeterminado es cualquier espacio en blanco (espacios, tabulaciones, saltos de línea).
* maxsplit (opcional): Un número entero que especifica el número máximo de divisiones a realizar. Si se especifica, la cadena se dividirá como máximo en maxsplit subcadenas. Si no se especifica, se realizarán todas las divisiones posibles.
* Valor de retorno: El método split() devuelve una lista de subcadenas.

**slicing [::-1]**  
Inversión de la frase : La expresión frase[::-1] utiliza rebanado con un paso de -1, lo que significa que recorre la cadena desde el final hacia el principio, efectivamente invirtiendo la frase.  

**fin()**  
cadena.find(subcadena, inicio, fin)
* Parámetros:
  * cadena: La cadena en la que deseas buscar la subcadena.
  * subcadena (obligatoria): La subcadena que deseas encontrar en la cadena.
  * inicio: (Opcional) El índice donde quieres que comience la búsqueda. Si no se especifica, la búsqueda comienza desde el principio de la cadena (índice 0).
  * fin: (Opcional) El índice donde quieres que termine la búsqueda. Si no se especifica, la búsqueda continúa hasta el final de la cadena.
* Valor de retorno: Si la subcadena se encuentra dentro de la cadena, find() devuelve el índice de la primera aparición de la subcadena. Si la subcadena no se encuentra, find() devuelve -1.  
* La función find() realiza una búsqueda de izquierda a derecha.
* Es sensible a mayúsculas y minúsculas, lo que significa que distingue entre "Hola" y "hola".
* Los parámetros inicio y fin te permiten limitar el rango de búsqueda dentro de la cadena.

**
