'''Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''
palabra=input("Escribe una palabra")
for i in range(10):
    print(palabra)

'''Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
edad=int(input("¿Cuántos años tienes?"))
for i in range(edad):
    print("Has cumplido",i+1,"años")

'''Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
numero=int(input("Escribe un número entero positivo"))
for i in range(1,numero+1,2):
    print(i,end=", ")

'''Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
numero=int(input("Escribe un número entero positivo"))
for i in range(numero,-1,-1):
    print(i,end=", ")

'''Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''
cantidad=float(input("¿Cuanto quieres invertir?"))
interes=float(input("¿Cuál es el interés anual?"))
años=int(input("¿Cuántos años?"))
for i in range(años):
    cantidad=cantidad*(1+interes/100)
    print("Capital tras",i+1,"años:",round(cantidad,2))

'''Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
'''
try:
    numero=int(input("Escribe un número entero"))
    for i in range(numero):
        print("*"*(i+1))
except ValueError:
    print("Debes introducir un número entero")

'''Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
for i in range(1,11):
    print("Tabla del ",i)
    for j in range(1,11):
        print(i*j,end="\t")
        print()

'''Otro método'''
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

'''Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
try:
    numero = int(input("Introduce la altura del triángulo (entero positivo): "))  # Solicita al usuario la altura del triángulo y la convierte a entero

    for i in range(1, numero + 1, 2):  # Bucle externo: itera sobre números impares desde 1 hasta la altura ingresada
        # i representa el número de elementos en cada fila del triángulo

        for j in range(i, 0, -2):  # Bucle interno: itera en reversa desde i hasta 1, disminuyendo de 2 en 2
            # j representa los números que se imprimen en cada fila
            print(j, end=" ")  # Imprime el valor de j seguido de un espacio (sin salto de línea)

        print(" ")  # Imprime un salto de línea al final de cada fila del triángulo

except ValueError:
    print("Debes introducir un número entero")  # Captura la excepción si el usuario no ingresa un entero

'''Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
contrasena = ""  # Inicializa la variable contraseña vacía

while contrasena != "contraseña":
    contrasena = input("Introduzca la contraseña: ")
    if contrasena != "contraseña":
        print("La contraseña es incorrecta")

print("Bienvenido")

'''Otro método'''
key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

'''Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
try:
    numero = int(input("Escribe un número entero: "))  # Solicita al usuario un número entero y lo convierte a tipo int

    if numero <= 1:  # Verifica si el número es menor o igual a 1
        print("No es un número primo")  # Si es menor o igual a 1, no es primo
    else:
        for i in range(2, numero):  # Itera desde 2 hasta el número ingresado - 1
            if numero % i == 0:  # Verifica si el número es divisible por i
                print("No es un número primo")  # Si es divisible, no es primo
                break  # Sale del bucle, ya que no es necesario seguir comprobando
        else: # este else pertenece al for, y solo se ejecuta si el for termina sin un break.
            print("Es un número primo") # si el for termina sin encontrar divisores, es primo.

except ValueError: # Captura la excepción si el usuario no ingresa un número entero
    print("Debes introducir un número entero") # Indica al usuario que debe ingresar un entero.

except: # captura cualquier otro tipo de error.
    print("Error desconocido") # informa que ocurrio un error que no fue un ValueError.

'''Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''
palabra = input("Introduce una palabra: ") # Solicita al usuario que ingrese una palabra
for i in range(len(palabra) - 1, -1, -1): # Recorre la palabra empezando por la última, de una en una posición, hasta la primera.
    print(palabra[i]) # Imprime cada letra de la palabra en orden inverso.

'''Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''
frase = input("Introduce una frase: ") # Solicita al usuario que ingrese una frase
letra = input("Introduce una letra: ")  # Solicita al usuario que ingrese una letra
contador = 0
for i in range(len(frase)):
    if frase[i] == letra:
        contador += 1
print("La letra", letra, "aparece", contador, "veces en la frase")

'''Método con función count()'''
frase = input("Introduce una frase: ") # Solicita al usuario que ingrese una frase
letra = input("Introduce una letra: ")  # Solicita al usuario que ingrese una letra
contador = frase.count(letra)
print("La letra", letra, "aparece", contador, "veces en la frase")

'''Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''
while True:  # Bucle infinito que se ejecuta hasta que se encuentra la palabra "salir"
    frase = input("Introduce algo (escribe 'salir' para terminar): ")  # Solicita al usuario que ingrese una frase    
    if frase.lower() == "salir":  # Verifica si la frase (en minúsculas) es "salir"
        break  # Sale del bucle si la frase es "salir"    
    print(frase)  # Imprime la frase ingresada por el usuario
print("Adiós")  # Imprime "Adiós" después de que el bucle termina
