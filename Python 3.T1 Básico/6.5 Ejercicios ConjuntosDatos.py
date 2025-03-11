"""
LISTAS
La lista es un tipo de colección ordenada y modificable.
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""
miLista=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1,2]]
# MÉTODOS DE LAS LISTAS
# Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

# Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1,2]]
print(miLista[0])

miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1][1]
print(miVar)

# Función con una lista como parámetro
def miFunccion(listaFrutas):
    for x in listaFrutas:
        print(x)
frutas = ["Manzana", "banana", "cereza"]
miFunccion(frutas)

"""
TUPLA
Una tupla es una colección ordenada e
inmutable.
En Python, las tuplas se escriben entre
paréntesis.
"""
# Declaración de una tupla
miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])

# Otra forma de declararla
miTupla = tuple(("manzana", "banana", "cereza"))
print(miTupla)

# Indexación Negativa
miTupla = ("manzana", "banana", "cereza")
print(miTupla[-1])

# Rango de índices
# Devuelve el tercer, cuarto y quinto elemento:
miTupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(miTupla[2:5])

# Convierta la tupla en una lista para poder cambiarla:
miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)
print(miTupla)

# Recorrer una tupla
miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
    print(x)

# Comprobar si existe un elemento
# Compruebe si "manzana" está presente en la tupla:
miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
    print("Sí, 'manzana' está en la tupla.")
    
# Otra forma, simplemente con un boolean
miTupla = ("manzana", "banana", "cereza")
print("manzana" in miTupla)

# Longitud de la tupla
miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))

# Unir dos tuplas
tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)
tupla3 = tupla1 + tupla2
print(tupla3)

# Cuantas veces se encuentra el elemento 4 en miTupla?
miTupla = ("manzana", "banana", "cereza" , "manzana")
print(miTupla.count("manzana"))

# Desempaquetdo de tupla
miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla
print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)

"""
DICCIONARIOS
Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben 
entre llaves y tienen claves y valores.
"""
# Declaración de un diccionario 
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)

# A los valores almacenados en un diccionario se accede por su clave
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
peliculas["Love Actually"] # En este caso las claves representan el nombre de una pelicula, y el valor, el nombre del director.

# Reasignar valores a un diccionario
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
peliculas["Kill Bill"] = "Quentin Tarantino"
print(peliculas)

# Usar una tupla dentro de un diccionario:
miDiccionario3={"nombre":"Jordan", "Equipo":"Bulls", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario3["Anillos"])

# Quitar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
peliculas.pop("Love Actually")
print(peliculas)

# Crear un diccionario a partir de dos listas:
lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario = dict(zip(lista_claves , lista_valores))
print(diccionario)

# Para comprobar si una clave está en el diccionario:
diccionario = {'nombre': 'Angel', 'edad': 43}
print("nombre" in diccionario) #Devuelve true o false

# Imprima las claves del diccionario:
peliculas = {"Love Actually": "Richard Curtis",
"Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
    print(peliculas[x])

# Longitud de un diccionario:
peliculas = {"Love Actually": "Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
print(len(peliculas))

# Agregar elementos a un diccionario:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
miDiccionario["color"] = "red"
print(miDiccionario)

# Eliminar el último elemento insertado:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
miDiccionario.popitem()
print(miDiccionario)

# La palabra clave "del" elimina el elemento con el nombre de clave especificado:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
del miDiccionario["model"]
print(miDiccionario)

# La palabra clave "del" también puede eliminar completamente el diccionario:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
del miDiccionario
print(miDiccionario)

# La palabra clave "clear()"" vacía el diccionario:
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
miDiccionario.clear()
print(miDiccionario)

# Copiar un diccionario
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
midict = miDiccionario.copy()
print(midict)

# Otra forma de copiar un diccionario
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
midict = dict(miDiccionario)
print(midict)

# Diccionarios anidados
child1 = {"name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias", "year" : 2007}
child3 = {"name" : "Linus", "year" : 2011}
myfamily = {"child1" : child1, "child2" : child2, "child3" : child3}
print(myfamily["child1"])

"""
SETs, conjuntos
Un conjunto es una colección de elementos únicos que no está ordenada ni indexada, por lo que no puede estar seguro de en qué orden aparecerán los elementos. En Python, los conjuntos se escriben entre llaves.
Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar nuevos elementos.
"""
# Declaración:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}

# Otra forma de declararlo
mi_conjunto3 = set(("Angel", "Sara", "Pilar"))
print(mi_conjunto3)

# Para añadir un nuevo elemento:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto.add("Antonio")

# Para añadir varios elementos:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto.update({"Fran", "María"})

# Unión de colecciones. Si hay algún valor repetido sólo aparecerá una vez.
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}
union= mi_conjunto | mi_conjunto2

# Intersección de conjuntos:  La intersección de dos o más conjuntos es un nuevo conjunto que contiene solo los elementos que están presentes en ambos conjuntos al mismo tiempo.
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}
interseccion= mi_conjunto & mi_conjunto2
# Nos crea otro conjunto con los valores que estaban duplicados en ambos conjuntos.
# En nuestro caso sólo Angel.

# Diferencia de conjuntos. Nos crea otro conjunto con los elementos que no están duplicados.
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}
diferencia= mi_conjunto - mi_conjunto2

# Para comprobar si un elemento está en un conjunto:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}
"Angel" in mi_conjunto # Devuelve true o false

# Recorra el conjunto e imprima los valores:
miSet = {"manzana", "banana", "cereza"}
for x in miSet:
    print(x)
    
"""
No puede acceder a los elementos de un conjunto haciendo referencia a un índice, ya que los conjuntos no están ordenados, los elementos no tienen índice.
"""
# Obtenga la cantidad de elementos en un conjunto:
miSet = {"manzana", "banana", "cereza"}
print(len(miSet))

# Elimine "banana" utilizando el método "remove(elemento)":
#   Función: Elimina el elemento especificado del conjunto.
#   Comportamiento si el elemento no existe: Lanza un error KeyError si el elemento no está presente en el conjunto.
miSet = {"manzana", "banana", "cereza"}
miSet.remove("banana")
print(miSet)
    
# Elimine "banana" utilizando el método "discard(elemento)":
# Función: Elimina el elemento especificado del conjunto si está presente.
# Comportamiento si el elemento no existe: No hace nada si el elemento no está en el conjunto. No lanza ningún error.
miSet = {"manzana", "banana", "cereza"}
miSet.discard("banana")
print(miSet)

"""
Si el elemento a eliminar no existe, remove() generará un error.
Si el elemento a eliminar no existe, discard() NO generará un error.
"""

# Elimine el último elemento utilizando el método "pop()":
"""También puede usar el método "pop()" para eliminar un elemento, pero este método eliminará el último
elemento.
Recuerde que los conjuntos no están ordenados, por lo que no sabrá qué elemento se elimina.
"""
miSet = {"manzana", "banana", "cereza"}
x = miSet.pop()
print(x)
print(miSet)

# El método "clear()"" vacía el conjunto:
miSet = {"manzana", "banana", "cereza"}
miSet.clear()
print(miSet)

# La palabra clave "del" borrará completamente el conjunto:
miSet = {"manzana", "banana", "cereza"}
del miSet
print(miSet)

# Unión de conjuntos
# El método union() devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# El método update() inserta los elementos en set2 en set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Tanto union() como update() excluirán cualquier elemento duplicado.