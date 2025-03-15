#Salida de directa de datos
print("En esta ocasión hemos imprimido por pantalla este string")

#Salida de datos calculados
n_numero_1 = 4
n_numero_2 = 6
print("El resultado de sumar" , n_numero_1, "y" , n_numero_2 , "es" , (n_numero_1+n_numero_2))
#Si concatenamos int y strings usando el signo + nos puede dar problemas.
print("El resultado de sumar " + n_numero_1 + " y " + n_numero_2 + " es " + (n_numero_1+n_numero_2))
print("El resultado de sumar" + " " + " os numeros")

'''Literales de cadena formateados (f-strings)'''

nombre = "Laura"
puntuacion = 95.75
# Ejemplo básico
print(f"¡Hola, {nombre}! Tu puntuación es {puntuacion}.")
# Formateo de números flotantes
print(f"Tu puntuación redondeada a un decimal es {puntuacion:.1f}.")
# Expresiones dentro de f-strings
print(f"El doble de tu puntuación es {puntuacion * 2}.")

'''Método format()'''

producto = "Laptop"
precio = 1200
descuento = 0.15
# Formateo por posición
print("El producto {} tiene un precio de {} con un descuento del {}%.".format(producto, precio, descuento * 100))
# Formateo por nombre
print("El precio final de {producto_nombre} es {precio_final}.".format(
    producto_nombre=producto, precio_final=precio * (1 - descuento)
))
# Formateo con alineación y ancho
print("{:<10} | {:^10} | {:>10}".format("Producto", "Precio", "Descuento"))

# Otro ejemplo
x = 10  # Se asigna el valor 10 a la variable x
y = 20  # Se asigna el valor 20 a la variable y
# Ejemplo 1: Formateo por posición implícita
# Las llaves {} actúan como marcadores de posición.
# format(x, y) asigna x a la primera llave y y a la segunda.
print("x = {}, y = {}".format(x, y))  # Imprime: x = 10, y = 20
# Ejemplo 2: Formateo por posición explícita
# Las llaves {1} y {0} especifican el orden de los argumentos.
# format(x, y) asigna y a {1} (segunda posición) y x a {0} (primera posición).
print("y = {1}, x = {0}".format(x, y))  # Imprime: y = 20, x = 10
# Ejemplo 3: Formateo por nombre de variable
# Se asignan nombres a los argumentos de format().
# Las llaves {valor_x} y {valor_y} hacen referencia a esos nombres.
print("x = {valor_x}, y = {valor_y}".format(valor_x=x, valor_y=y))  # Imprime: x = 10, y = 20
'''Resultado
x = 10, y = 20
y = 20, x = 10
x = 10, y = 20
'''

''' Operador % (formateo estilo C)'''
cantidad = 3
fruta = "manzanas"
# Formateo de enteros y cadenas
print("Tengo %d %s." % (cantidad, fruta))
# Formateo de números flotantes
temperatura = 23.5
print("La temperatura es %.1f grados Celsius." % temperatura)
# Formateo con múltiples valores
print("Hoy compré %d %s a un precio de %.2f euros." % (cantidad, fruta, precio))