# Diferencia entre Funciones Predefinidas y Métodos en Python

Esta distinción es fundamental en la programación orientada a objetos (POO), que es un paradigma importante en Python. La diferencia principal radica en dónde están definidas y cómo se invocan.

---

## Funciones Predefinidas (Built-in Functions)

### Definición:
Son bloques de código con nombre que realizan una tarea específica y que están disponibles globalmente en Python. Esto significa que puedes llamarlas directamente desde cualquier parte de tu código sin necesidad de hacer nada especial.

### Independencia:
Las funciones predefinidas no están asociadas a ningún objeto o clase en particular. Actúan de forma independiente sobre los datos que se les pasan como argumentos.

### Ejemplos comunes:
`print()`, `len()`, `type()`, `int()`, `float()`, `str()`, `list()`, `tuple()`, `dict()`, `sum()`, `max()`, `min()`, `abs()`, `range()`, etc.

```python
mi_lista = [1, 2, 3]
longitud = len(mi_lista)  # len() es una función predefinida
print(longitud)          # print() también es una función predefinida

numero_str = "123"
numero_int = int(numero_str) # int() es una función predefinida
print(type(numero_int))    # type() es otra función predefinida
```

---

## Métodos

### Definición:
Son también bloques de código con nombre que realizan tareas específicas, pero están asociados a un objeto de una clase. Esto significa que solo puedes llamar a un método a través de un objeto específico de esa clase.

### Dependencia de objetos:
Los métodos operan sobre el objeto al que pertenecen (a menudo accediendo o modificando sus atributos internos).

### Sintaxis de llamada:
Para llamar a un método, se utiliza la sintaxis de punto (`.`) después del objeto, seguido del nombre del método y los paréntesis (que pueden contener argumentos).

```python
mi_cadena = "hola"
mayusculas = mi_cadena.upper()  # upper() es un método del objeto string
print(mayusculas)              # Output: HOLA

otra_lista = [3, 1, 4, 1, 5, 9]
otra_lista.sort()             # sort() es un método del objeto lista
print(otra_lista)             # Output: [1, 1, 3, 4, 5, 9]

mi_diccionario = {"nombre": "Ana", "edad": 30}
claves = mi_diccionario.keys() # keys() es un método del objeto diccionario
print(claves)                  # Output: dict_keys(['nombre', 'edad'])
```

---

## Analogía para entenderlo:

Imagina que tienes un perro (un objeto).

- **Una función predefinida** sería como una orden general que puedes dar a cualquier cosa, por ejemplo, "haz ruido". Tanto tu perro como un coche de juguete podrían "hacer ruido" de alguna manera, pero la función en sí no está ligada específicamente al perro.
- **Un método** sería una acción específica que tu perro puede realizar, como "ladra" o "mueve la cola". Estas acciones están intrínsecamente ligadas al objeto "perro" y solo tienen sentido cuando se aplican a un perro (o a un objeto de la clase "Perro").

---

## Resumen:

| Característica       | Función Predefinida                     | Método                                   |
|----------------------|-----------------------------------------|------------------------------------------|
| **Definición**       | Globalmente disponible                 | Asociado a un objeto de una clase        |
| **Asociación**       | Independiente de objetos               | Dependiente de un objeto específico      |
| **Sintaxis de llamada** | `nombre_funcion(argumentos)`         | `objeto.nombre_metodo(argumentos)`       |
| **Propósito**        | Tareas generales                       | Operaciones específicas sobre objetos    |

---

Entender esta diferencia es crucial cuando empiezas a trabajar con objetos en Python. Verás que la mayoría de las interacciones con los datos en Python se realizan a través de métodos de los objetos que representan esos datos (cadenas, listas, diccionarios, etc.).
```