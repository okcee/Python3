'''Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
s_nombre = input("¿Cuál es tu nombre? ")
try:
    i_repeticiones = int(input("Dime un número entero del 1 al 10: "))
    for _ in range(i_repeticiones): # se utiliza como una variable de bucle "dummy" porque no necesitamos usar el valor de la variable en sí, solo necesitamos que el bucle se ejecute el número correcto de veces.
        print(s_nombre)
except ValueError:
    print("Por favor, introduce un número entero válido.")
''' Solución aprendeconalf
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))
'''
'''Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
