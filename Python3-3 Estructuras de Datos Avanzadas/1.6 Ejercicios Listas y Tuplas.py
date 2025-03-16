'''Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''
curso = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(curso)

'''Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura in asignaturas:
    print("Yo estudio " + asignatura)

'''Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "? ")
    notas.append(nota)
    
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado un " + notas[i])

'''Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''
numeros = []
for i in range(6):
    numero = int(input("Introduce un número ganador: "))
    numeros.append(numero)
numeros.sort()
print("Los números ganadores son " + str(numeros))

'''Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numeros[-i], end=", ")

'''Solución alternativa'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")

'''Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    notas.append(nota)
    if nota >= 5:
        asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))

'''Resolución con pop()'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(asignaturas)-1, -1, -1):
    nota = float(input("¿Qué nota has sacado en " + asignaturas[i] + "?"))
    if nota >= 5:
        asignaturas.pop(i)
print("Tienes que repetir " + str(asignaturas))

'''Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(abecedario), 1, -1):
    if i % 3 == 0:
        abecedario.pop(i-1)
print(abecedario)

'''Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''
palabra = input("Introduce una palabra: ")
palabra = palabra.lower()
palabra_invertida = palabra[::-1]
if palabra == palabra_invertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

'''Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''
palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    contador = 0
    for letra in palabra:
        if letra == vocal:
            contador += 1
    print("La vocal " + vocal + " aparece " + str(contador) + " veces")

'''Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''
precios = [50, 75, 46, 22, 80, 65, 8]
menor = min(precios)
mayor = max(precios)
print("El menor es " + str(menor))
print("El mayor es " + str(mayor))

'''Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

El producto escalar (también conocido como producto punto o producto interno) es una operación fundamental en álgebra lineal que toma dos vectores de igual dimensión y devuelve un único número escalar.
En esencia, el producto escalar mide la "similitud" o la "proyección" de un vector sobre otro. Cuanto mayor sea el producto escalar (en valor absoluto), más se "alinean" los vectores.

Cómo se calcula:
Si tienes dos vectores, digamos:
a = [a₁, a₂, ..., a<0xE2><0x82><0x99>]
b = [b₁, b₂, ..., b<0xE2><0x82><0x99>]
El producto escalar de a y b, denotado como a ⋅ b (o a veces <a, b>), se calcula multiplicando las componentes correspondientes de los vectores y luego sumando esos productos:
a ⋅ b = a₁ * b₁ + a₂ * b₂ + ... + a<0xE2><0x82><0x99> * b<0xE2><0x82><0x99>

Además de la definición algebraica, el producto escalar tiene una importante interpretación geométrica:
a ⋅ b = ||a|| * ||b|| * cos(θ)
'''
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
producto_escalar = 0 # Se inicializa una variable llamada producto_escalar en 0.
for i in range(len(vector1)):
    producto_escalar += vector1[i] * vector2[i]
print("El producto escalar de los vectores es " + str(producto_escalar))

'''Ejercicio 12
Escribir un programa que almacene las matrices
A =  [[1, 2, 3], [4, 5, 6]]
B = [[-1, 0], [0, 1], [1, 1]]
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
'''
A =  [[1, 2, 3], [4, 5, 6]]
B = [[-1, 0], [0, 1], [1, 1]]
producto = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            producto[i][j] += A[i][k] * B[k][j]
print(producto)

'''Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
'''
# Solicita al usuario que introduzca una lista de números separados por comas.
numeros_str = input("Introduce una lista de números separados por comas: ")
# Divide la cadena de entrada en una lista de cadenas, utilizando la coma como separador.
numeros_lista_str = numeros_str.split(',')
# Convierte cada cadena de la lista a un número de punto flotante (decimal).
# Esto es necesario para poder realizar cálculos numéricos con los valores.
numeros = [float(numero) for numero in numeros_lista_str]
# Calcula la media (promedio) de los números en la lista.
# Se suma todos los números y se divide por la cantidad de números.
media = sum(numeros) / len(numeros)
# Calcula la desviación típica de los números en la lista.
# La desviación típica mide la dispersión de los datos alrededor de la media.
# 1. Se calcula la diferencia de cada número con respecto a la media y se eleva al cuadrado.
# 2. Se suma todos estos cuadrados.
# 3. Se divide la suma por la cantidad de números.
# 4. Se calcula la raíz cuadrada del resultado.
desviacion_tipica = (sum([(numero - media)**2 for numero in numeros]) / len(numeros))**0.5
# Imprime el valor de la media calculado.
print("La media es " + str(media))
# Imprime el valor de la desviación típica calculada.
print("La desviación típica es " + str(desviacion_tipica))
