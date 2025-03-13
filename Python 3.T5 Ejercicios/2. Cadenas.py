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
name = input("¿Cómo te llamas? ")
print(name.lower()) # El método .lower() convierte todos los caracteres de la cadena almacenada en name a minúsculas.
print(name.upper()) # El método .upper() convierte todos los caracteres de la cadena almacenada en name a mayúsculas.
print(name.title()) # El método .title() convierte la cadena almacenada en name al formato de título, donde la primera letra de cada palabra se convierte en mayúscula y el resto en minúscula.

'''Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''
name = input("¿Cómo te llamas? ")
print(name.upper(), "tiene", len(name), " letras")

'''Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''
# Solicitar al usuario que ingrese un número de teléfono con el formato +34-913724710-56
telefono_completo = input("Ingrese un número de teléfono con el formato +34-XXXXXXXXX-XX: ")

# Dividir la cadena usando el carácter '-' como separador
partes = telefono_completo.split('-')

# Validar que haya exactamente tres partes: prefijo, número y extensión
if len(partes) == 3:
    # Extraer el número de teléfono central (segunda parte)
    numero_telefono = partes[1]
    
    # Mostrar el número de teléfono sin el prefijo y la extensión
    print(f"El número de teléfono sin prefijo y extensión es: {numero_telefono}")
else:
    # Si el formato no es correcto, mostrar un mensaje de error
    print("El formato del número de teléfono no es válido. Asegúrese de usar el formato +34-XXXXXXXXX-XX.")

'''Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
'''
# Solicitar al usuario que ingrese una frase
frase = input("Introduzca una frase: ")

# Invertir la frase usando slicing
frase_invertida = frase[::-1]
'''Otro método
# Invertir la frase usando reversed() y join()
frase_invertida = ''.join(reversed(frase))'''

# Mostrar la frase invertida
print(f"La frase invertida es: {frase_invertida}")
'''Ejercicio 5 - Usando bucle for'''
# Solicitar al usuario que ingrese una frase
frase = input("Introduzca una frase: ")

# Inicializar una cadena vacía para almacenar la frase invertida
frase_invertida = ""

# Recorrer la frase de derecha a izquierda usando un bucle for
for i in range(len(frase) - 1, -1, -1):  # Iteramos desde el último índice hasta el primero
    frase_invertida += frase[i]  # Concatenamos cada carácter a la nueva cadena

# Mostrar la frase invertida
print(f"La frase invertida es: {frase_invertida}")

'''Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''
# Solicitar al usuario que ingrese una frase
frase = input("Introduzca una frase: ")
# Solicitar al usuario que ingrese una vocal
vocal = input("Introduzca una vocal: ")
# Validar que la entrada sea una vocal válida
if vocal.lower() in "aeiou":
    # Reemplazar la vocal en minúscula por su versión en mayúscula
    frase_modificada = frase.replace(vocal.lower(), vocal.upper())
    # Mostrar la frase modificada
    print(f"La frase con la vocal en mayúscula es: {frase_modificada}")
else:
    # Si la entrada no es una vocal válida, mostrar un mensaje de error
    print("Error: Por favor, introduzca una vocal válida (a, e, i, o, u).")

'''Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''
email = input("Introduce tu correo electrónico: ") # pide al usuario que introduzca su dirección de correo electrónico.
print(email[:email.find('@')] + '@ceu.es')
'''email.find('@'): Esta parte busca la posición del carácter "@" dentro de la cadena email. Devuelve el índice (la posición) de la primera aparición de "@".
email[:email.find('@')]: Esto utiliza el "slicing" (rebanado) de cadenas para extraer la parte del correo electrónico que viene antes del "@". Por ejemplo, si el correo es "[dirección de correo electrónico eliminada]", esto extraerá "usuario".
'@ceu.es': Esta es la parte fija que se añadirá al final.
+: El operador "+" concatena (une) las dos partes de la cadena.
print(): Finalmente, la función print() muestra el resultado en la pantalla.'''

'''Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''
