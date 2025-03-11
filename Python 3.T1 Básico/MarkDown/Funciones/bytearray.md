# Función bytearray()

Es una función incorporada que crea un objeto bytearray, el cual es una secuencia mutable de enteros en el rango de 0 <= x < 256. En términos más sencillos, es como una lista de bytes que puedes modificar.  

## Posibles sintáxis

- Sin argumentos: Crea un bytearray vacío.  
arr = bytearray()  
print(arr) # bytearray(b'')  

- Un entero: Crea un bytearray del tamaño especificado, inicializado con bytes nulos (0).  
arr = bytearray(5)  
print(arr) # bytearray(b'\x00\x00\x00\x00\x00')  

- Un iterable de enteros: Crea un bytearray a partir de un iterable (como una lista o tupla) de enteros en el rango 0-255.  
arr = bytearray([65, 66, 67])  
print(arr) # bytearray(b'ABC')  

- Una cadena y una codificación: Crea un bytearray a partir de una cadena, codificada según la codificación especificada.  
arr = bytearray("Hola", "utf-8")  
print(arr) # bytearray(b'Hola')  

- Un objeto que se ajusta al protocolo de búfer: Esto incluye los objetos bytes.  
b = bytes("Hola", "utf-8")  
arr = bytearray(b)  
print(arr) # bytearray(b'Hola')  

## Propósito y características clave:

- Secuencia mutable: A diferencia de los objetos bytes (que son inmutables), los objetos bytearray se pueden modificar. Esto significa que puedes cambiar, añadir o eliminar elementos después de crear el objeto.  
- Enteros en el rango 0-255: Cada elemento en un bytearray representa un byte y, por lo tanto, se representa como un entero entre 0 y 255.  
- Útil para datos binarios: bytearray es especialmente útil cuando necesitas trabajar con datos binarios, como leer o escribir archivos binarios, manipular datos de red o procesar imágenes.  