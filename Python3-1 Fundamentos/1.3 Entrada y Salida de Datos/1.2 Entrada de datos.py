s_nombreIntroducido = input("Introduzca su nombre: ")
print("Bienvenido", s_nombreIntroducido)
# -------------------------------------
""" IMPORTANTE: Todo lo introducido por input() se considera string, aunque sea un número,
por lo que, si necesitamos operar matemáticamente con números, tendremos que hacer un casting:
"""
s_edad = int(input("Introduzca su edad: "))
print("El año que viene tendrá usted ", s_edad + 1, "años")

# Ejemplo de introducir datos utilizando append() para listas y add() para conjuntos.
lista = list()
conjunto = set()

tamaño_lista = int(input("Introduce el tamaño de la lista: "))
tamaño_conjunto = int(input("Introduce el tamaño del conjunto: "))

print("Introduce los elementos de la lista:")
for i in range(tamaño_lista): # Corrección: Usar el tamaño correcto
    lista.append(int(input()))

print("Introduce los elementos del conjunto:")
for i in range(tamaño_conjunto): # Corrección: Usar el tamaño correcto
    conjunto.add(int(input()))

print("Lista:", lista)
print("Conjunto:", conjunto)

# Ejemplo de introducir datos utilizando map() y split():
lista = list(map(int, input("Introduce los elementos de la lista separados por espacios: ").split()))
conjunto = set(map(int, input("Introduce los elementos del conjunto separados por espacios: ").split()))

print("Lista:", lista)
print("Conjunto:", conjunto)

# Tuplas: Inmutabilidad y Conversión
T = (2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L = list(T)
L.append(int(input("Introduzca el nuevo elemento: ")))
L = tuple(L)
print("Tupla final")
print(T)

#Ejercicios para Practicar

# 1) Escribe un programa que pida al usuario una lista de nombres y luego imprima la lista en orden alfabético.

nombres = []
while True:
    nombre = input("Introduce un nombre (o escribe 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)
nombres.sort()
print("Lista de nombres ordenada alfabéticamente:", nombres)

# 2) Crea un programa que pida al usuario un conjunto de números y luego imprima los números pares del conjunto.

numeros = set()
while True:
    entrada = input("Introduce un número entero (o escribe 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)
        numeros.add(numero)
    except ValueError:
        print("Entrada inválida. Introduce un número entero.")
pares = {numero for numero in numeros if numero % 2 == 0}
print("Números pares en el conjunto:", pares)

# 3) Escribe un programa que pida al usuario una tupla de coordenadas (x, y) y luego calcule la distancia al origen (0, 0).

import math
try:
    entrada = input("Introduce las coordenadas (x, y) separadas por comas: ")
    coordenadas = tuple(map(float, entrada.split(',')))
    if len(coordenadas) != 2:
        raise ValueError
    x, y = coordenadas
    distancia = math.sqrt(x**2 + y**2)
    print("Distancia al origen:", distancia)
except ValueError:
    print("Entrada inválida. Introduce dos números separados por comas.")
