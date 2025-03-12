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

