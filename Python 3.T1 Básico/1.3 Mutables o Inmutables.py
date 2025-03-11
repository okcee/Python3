'''Objetos mutables e inmutables'''

'''Análisis del Código'''

# Dirección de memoria de un entero:
a = 65
# Se muestra la dirección de memoria de la variable a.
a+=2
# Se muestra la dirección de memoria de la variable a nuevamente, y se puede observar que ha cambiado, ya que los enteros son inmutables.

# Variables que apuntan al mismo objeto:
miNumero = 65
miNumero2 = miNumero
# Ambas variables apuntan al mismo objeto entero (65), por lo que tienen la misma dirección de memoria. Esto es una optimización de Python para ahorrar memoria.

# Tuplas (inmutables):
a = (1, 2, 3, 4, 5)
# Se muestra la dirección de memoria de la tupla. Las tuplas no pueden ser modificadas.

# Listas (mutables):
a = [1, 2, 3, 4, 5]
# Se muestra la dirección de memoria de la lista. Las listas si pueden ser modificadas, y si se modifican, la dirección de memoria permanece igual.

# Diccionarios (mutables):
a = {'a': 1, 'b': 2}
# Se muestra la dirección de memoria del diccionario.
a["c"] = 3
# Se modifica el diccionario, y se vuelve a mostrar la dirección de memoria, y se puede observar que no ha cambiado.


# Obtener la dirección de memoria de una variable
a = 65
print("La dirección de memoria es" ,
id(a))

# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("La dirección de memoria es" , id(miNumero))
print("La dirección de memoria es" , id(miNumero2))
# Si cambio la variable, realmente creo una copia en otra dirección de memoria:
a = 65
print("La dirección de memoria es" , id(a))
a+=2
print("La dirección de memoria es" , id(a))

# Obtener la dirección de memoria de una tupla
a = (1, 2, 3, 4, 5)
print("La dirección de memoria es" , id(a))

# Obtener la dirección de memoria de una lista
a = [1, 2, 3, 4, 5]
print("La dirección de memoria es" , id(a))

# Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2}
print(a)
print("La dirección de memoria es" , id(a))
a["c"] = 3
print(a)
print("La dirección de memoria es" , id(a))