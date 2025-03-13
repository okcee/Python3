'''Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''
edad = int(input("¿Qué edad tienes?"))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

'''Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
passw = input("Introduce una contraseña: ")
pass2 = input("Confirma la contraseña: ")

if passw==pass2:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")

'''Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
num1 = float(input("Introduce un número como dividendo: "))
num2 = float(input("Introduce otro número como divisor: "))

try:
    division=num1/num2
    print(division)
except:
    num2==0
    print("Error, el divisor no puede ser 0")

'''Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
try:
    numero=int(input("Introduzca un numero entero"))
    if numero%2==0:
        print("El número es par")
    else:
        print("El número es impar")
except ValueError:
    print("Error: El valor introducido no es un número entero")

'''Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
