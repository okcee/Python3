# Ejemplo:
'''Uno de los usos más frecuentes del bucle for es recorrer objetos iterables, diccionarios, tuplas…etc:'''
'''Por defecto, al pasarle un diccionario a un for, lo recorremos por sus claves. Hay varias maneras de extraer los valores de un diccionario.'''
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario
for k in d:
    info = '{}: {}'.format(k, d[k]) # Texto formateado con claves y valores
    print(info)
'''Resultado:
nombre: Guido
apellidos: van Rossum
edad: 60
'''
# El método str.format sustituye las llaves de la cadena de texto por los parámetros que le pasamos al llamarlo. En cada iteración del ejemplo le estamos pasando la clave (k) del diccionario y el valor del diccionario correspondiente a esa clave (d[k]).

'''WHILE'''
'''1. Bucle while con contador:
Se utiliza una variable como contador para controlar el número de iteraciones.'''
contador = 10
while contador > 0:
    print(contador)
    contador -= 1

'''2. Bucle while con condición de entrada del usuario:
El bucle continúa hasta que el usuario ingresa una entrada específica.'''
entrada = ""
while entrada != "salir":
    entrada = input("Ingrese un comando (o 'salir'): ")
    print("Comando:", entrada)
    
'''3. Bucle while con banderas (flags):
Se utiliza una variable booleana (bandera) para controlar la ejecución del bucle.'''
ejecutando = True
while ejecutando:
    comando = input("Ingrese un comando: ")
    if comando == "detener":
        ejecutando = False
    else:
        print("Comando:", comando)

'''4. Bucle while infinito (con precaución):
El bucle se ejecuta indefinidamente (a menos que se interrumpa manualmente o con una condición de salida dentro del bucle).
Nota: Los bucles infinitos deben usarse con precaución para evitar que el programa se bloquee. Es crucial incluir una condición de salida dentro del bucle para prevenir esto.
'''
while True:
    print("Este bucle es infinito")
    #Es necesario agregar una condición de ruptura, o "break".
    break

'''5. Bucle while con break y continue:
break: Interrumpe la ejecución del bucle por completo.
continue: Salta la iteración actual y pasa a la siguiente.'''
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Salta números pares
    print(contador)
    if contador == 7:
        break  # Detiene el bucle en 7

'''6. Bucle while con else:
El bloque else se ejecuta si el bucle termina normalmente (sin un break).'''
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Bucle completado")

