# Estructuras que posee Python para poder trabajar con colecciones de datos

Las estructuras de datos en Python se pueden entender como un tipo de dato compuesto, debido a que en una misma variable podemos almacenar no sólo un dato, sino infinidad de ellos. Dichas estructuras, pueden tener diferentes características y funcionalidades.  
Hay cuatro **tipos de estructuras de recopilación de datos** en el lenguaje de programación Python:  
- La *lista* [list] o *Array*; es una colección ordenada y modificable. Permite miembros duplicados.  
list = ["ordenada", "mutable", "duplicados"]  
- *Tupla* (tuple); es una colección ordenada e inmutable. Permite miembros duplicados.  
tuple = ("ordenada", "immutable", "duplicados")  
- *Conjuntos* {*Set*}; es una colección que no está ordenada ni indexada. No hay miembros duplicados.  
set = {"desordenada", "mutable", "no duplicados"}  
- *Diccionario* {*Dictionary*}; es una colección desordenada, modificable e indexada. No hay miembros duplicados. También llamados matrices asociativas.  
diccionario = {1:"desordenada", 2:"mutable", 3:"claves no duplicables", 4:"Indexada"}  

## Propiedades de cada tipo
1. Listas o Arrays  [list]
   - Ordenadas: Los elementos tienen un orden específico.  
   - Mutables: Se pueden modificar después de su creación (agregar, eliminar, modificar elementos).  
   - Indexadas: Se accede a los elementos mediante índices numéricos.  
   - Permiten duplicados: Pueden contener elementos repetidos.  
   - Se pueden mezclar elementos de distinto tipo.  
   - Se puede crear una lista desde un *string*, crea la lista de los caracteres del string  
   - Para imprimir toda la lista podemos poner: print(miLista[:])  
   - Se puede declarar una lista vacía.  
   - Una lista puede contener otra lista (listas anidadas).  
   - Una lista puede contener una función.  
2. Tuplas  (tuple)
   - Ordenadas: Los elementos tienen un orden específico.  
   - Inmutables: No se pueden modificar después de su creación.  
   - Indexadas: Se accede a los elementos mediante índices numéricos.  
   - Permiten duplicados: Pueden contener elementos repetidos.  
   - No permiten añadir, eliminar, mover elementos (no append, extend, remove)  
   - No permiten búsquedas (no index)  
   - Sí permiten extraer porciones, pero el resultado de la extracción es una tupla nueva.  
   - Permiten comprobar si un elemento se encuentra en la tupla (index())  
   - Puedes recorrer los elementos de la tupla utilizando un bucle for.  
   - Para crear una tupla con un solo elemento, debes agregar una coma después del elemento.  
   - La palabra clave del puede eliminar la tupla por completo.  
   - Una vez que se crea una tupla, no puede cambiar sus valores, son inmutables. Pero podemos convertir la tupla en una lista, cambiar la lista y volver a crear una nueva tupla. Convertiendo la lista en una tupla.
3. Conjuntos {set} 
   - Colecciones de elementos únicos: Los conjuntos almacenan una colección de elementos únicos, lo que significa que no pueden contener duplicados.  
   - Mutables: Puedes modificar los conjuntos agregando o eliminando elementos después de su creación.  
   - No ordenados: Los conjuntos no mantienen un orden específico de los elementos. El orden en que se almacenan los elementos puede variar.  
   - Elementos inmutables: Los elementos de un conjunto deben ser objetos inmutables, como cadenas, números o tuplas.  
   - Operaciones de conjuntos: Los conjuntos admiten operaciones matemáticas de conjuntos, como unión, intersección, diferencia y diferencia simétrica.  
   - Se basan en la noción matemática de conjuntos, implementan una serie de métodos que permiten trabajar con conjuntos de objetos de la misma manera que lo hacemos en conjuntos matemáticos.  
   - Son útiles cuando queremos trabajar con datos masivos y queremos extraer información relevante de ellos.

4. Diccionarios  {dic}
   - Colecciones de pares clave-valor: Los diccionarios almacenan datos en forma de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente.  
   - Mutables: Puedes modificar los diccionarios agregando, eliminando o actualizando pares clave-valor después de su creación.  
   - Desordenados: Los diccionarios no mantienen un orden específico de los elementos. El orden en que se almacenan los pares clave-valor puede variar.  
   - Claves inmutables: Las claves de un diccionario deben ser objetos inmutables, como cadenas, números o tuplas. Los valores pueden ser de cualquier tipo.  
   - Acceso por clave: Puedes acceder a los valores de un diccionario utilizando sus claves correspondientes.  
   - Son estructuras de datos que nos permiten almacenar valores de diferente tipo (números, strings, etc) e incluso listas y otros diccionarios.  
   - Es posible usar el *Constructor dict(clave="valor, ")* para crear un nuevo diccionario.  
   - print(miDiccionario.keys()) -->  Me imprime las claves.  
   - print(miDiccionario.values()) -->  Me imprime el valor de las claves.  

5. Bytes <bytes>  
   - Sintáxis b'<cadena de bytes>'  
   - Ubicación de memoria de 8 bits.  
   - Es una secuencia inmutable de bytes, conceptualmente similar a un string. Si necesitas modificar una secuencia de bytes, debes usar bytearray.  
   - Contiene enteros: Los elementos de un objeto bytes son enteros en el rango de 0 a 255 (inclusive). Cada entero representa un byte individual.  
   - Representación de datos binarios: Los objetos bytes se utilizan comúnmente para representar datos binarios, como datos de archivos, datos de red o datos de protocolos de comunicación.  
   - Creación: Se pueden crear objetos bytes utilizando el prefijo b antes de una cadena literal (por ejemplo, b'hola') o utilizando la función bytes():  
   - Los objetos bytes a menudo se utilizan junto con la codificación y decodificación de caracteres. El método .decode() se utiliza para convertir un objeto bytes en una cadena (str), y el método .encode() se utiliza para convertir una cadena en un objeto bytes.  
   - Diferencias clave con las cadenas (str):  
     - Mientras que las cadenas representan secuencias de caracteres Unicode, los objetos bytes representan secuencias de bytes.  
     - Las cadenas son para texto, los bytes son para datos binarios.  

# Métodos de las listas [list]

| Método | Descripción |
|---|---|
| `append(x)` | Añade el elemento `x` al final de la lista. |
| `extend(iterable)` | Extiende la lista añadiendo todos los elementos del iterable. |
| `insert(i, x)` | Inserta el elemento `x` en la posición `i`. |
| `remove(x)` | Elimina el primer elemento cuyo valor sea `x`. Lanza un `ValueError` si no existe tal elemento. |
| `pop(i)` | Elimina el elemento en la posición `i` y lo retorna. Si no se especifica `i`, elimina y retorna el último elemento. |
| `clear()` | Elimina todos los elementos de la lista. |
| `index(x, start, end)` | Retorna el índice del primer elemento cuyo valor sea `x`. Lanza un `ValueError` si no existe tal elemento. Los argumentos opcionales `start` y `end` son interpretados como en la notación de rebanadas y son usados para buscar en una subsecuencia específica de la lista. |
| `count(x)` | Retorna el número de veces que `x` aparece en la lista. |
| `sort(key=..., reverse=...)` | Ordena los elementos de la lista en su lugar (los argumentos pueden ser usados para personalizar el ordenamiento, mira `sorted()` para su explicación). |
| `reverse()` | Invierte los elementos de la lista en su lugar. |
| `copy()` | Retorna una copia superficial de la lista, equivalente a `a[:]`. |

# Métodos de las tuplas (tuple)

| Método | Descripción | Ejemplo |
|---|---|---|
| `count(valor)` | Devuelve el número de veces que aparece un valor en la tupla. | `mi_tupla.count(2)` |
| `index(valor)` | Devuelve el índice de la primera aparición de un valor en la tupla. | `mi_tupla.index(5)` |
| `lens(nombreTupla)` | Determinar cuántos elementos tiene una tupla. | `print(len(mytuple))` |

## Ventajas de las tuplas respecto a las listas
- Más rápidas.  
- Menos espacio (mayor optimización)  
- Formatean string.  
- Pueden utilizarse como claves en un diccionario (las listas no).  

# Métodos de los sets {conjunto}

| Método                  | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `add(elemento)`          | Añade un elemento al set.                                                   |
| `clear()`                | Borra todos los elementos del set.                                           |
| `copy()`                 | Devuelve una copia del set.                                                  |
| `difference(otro_conjunto)` | Devuelve un set que contiene las diferencias entre dos o más sets.             |
| `difference_update(otro_conjunto)` | Borra los elementos del set que están incluidos en otro.                        |
| `discard(elemento)`      | Borra el elemento especificado.                                              |
| `intersection(otro_conjunto)` | Devuelve un set que es la intersección resultante de otros dos.               |
| `intersection_update(otro_conjunto)` | Borra los elementos del set que no están presentes en otro.                   |
| `isdisjoint(otro_conjunto)` | Informa si dos sets tienen una intersección o no.                          |
| `issubset(otro_conjunto)`  | Informa si otro set contiene a este set o no.                               |
| `issuperset(otro_conjunto)` | Informa si este set contiene a otro set o no.                               |
| `pop()`                  | Borra un elemento del set, no podremos elegir cuál.                             |
| `remove(elemento)`       | Borra un elemento específico.                                                |
| `symmetric_difference(otro_conjunto)` | Devuelve un set con las diferencias simétricas de dos sets.                   |
| `symmetric_difference_update(otro_conjunto)` | Inserta las diferencias simétricas de este set y otro.                       |
| `union(otro_conjunto)`   | Devuelve un set con la unión de dos sets.                                    |
| `update(otro_conjunto)`  | Actualiza el set con la unión de este set y otros.                              |

# Métodos de los diccionarios {dic}

| Método | Descripción |
|---|---|
| `clear()` | Borra todos los elementos de un diccionario. |
| `copy()` | Devuelve una copia superficial de un diccionario. |
| `fromkeys(secuencia, [valor])` | Crea un nuevo diccionario con las claves de la secuencia y valores establecidos a valor. |
| `get(clave, [valor])` | Devuelve el valor para la clave si la clave está en el diccionario, de lo contrario valor. |
| `items()` | Devuelve una vista de los pares clave-valor del diccionario. |
| `keys()` | Devuelve una vista de las claves del diccionario. |
| `pop(clave, [valor])` | Si la clave está en el diccionario, la elimina y devuelve su valor, de lo contrario devuelve valor. |
| `popitem()` | Elimina y devuelve un par (clave, valor) arbitrario del diccionario. |
| `setdefault(clave, [valor])` | Si la clave está en el diccionario, devuelve su valor. Si no, inserta la clave con un valor de valor. |
| `update([otro])` | Actualiza el diccionario con los pares clave-valor de otro, sobrescribiendo las claves existentes. |
| `values()` | Devuelve una vista de los valores del diccionario. |