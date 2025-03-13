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
    numero=int(input("Escribe un número entero"))
    for i in range(1,numero+1,2):
        for j in range(i,0,-2):
            print(j,end=" ")
except ValueError:
    print("Debes introducir un número entero")
