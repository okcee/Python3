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
