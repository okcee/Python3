## Función Zip o de cremallera

La función zip() en Python es una herramienta muy útil para combinar múltiples iterables (como listas, tuplas o diccionarios) en un solo iterador.  

## ¿Qué hace *zip()*?

La función zip() en Python une dos listas separadas en una lista de pares. Convierte el objeto a tipo zip y, tenemos que convertirlo a lista si queremos ver los elementos de la cremallera.    

### Combinación de iterables:
zip() toma uno o más iterables como argumentos y devuelve un iterador de tuplas.  
Cada tupla en el iterador contiene los elementos correspondientes de los iterables de entrada. Es decir, la primera tupla contiene el primer elemento de cada iterable, la segunda tupla contiene el segundo elemento de cada iterable, y así sucesivamente.  
### Longitud del resultado:
El iterador resultante de zip() se detiene cuando el iterable más corto se agota.  
Esto significa que si tienes iterables de diferentes longitudes, el resultado solo contendrá tuplas hasta la longitud del iterable más corto.  

#### Ejemplo básico:  
nombres = ["Ana", "Juan", "Pedro"]
edades = [25, 30, 28]

combinado = zip(nombres, edades)

for nombre, edad in combinado:
    print(f"{nombre} tiene {edad} años.")

En este ejemplo:
- zip(nombres, edades) combina las listas nombres y edades.  
- El resultado es un iterador que produce las tuplas ("Ana", 25), ("Juan", 30) y ("Pedro", 28).  
- El bucle for itera sobre cada una de esas tuplas, y desempaqueta los valores dentro de cada tupla, y los asigna a las variables nombre, y edad, para poder ser impresos en el terminal.  
- 
## Usos comunes de zip():
- Iteración paralela: Recorrer múltiples listas o tuplas al mismo tiempo.  
- Creación de diccionarios: Combinar listas de claves y valores para crear un diccionario.  
- Procesamiento de datos: Combinar datos de diferentes fuentes para su análisis o manipulación.  

### Ejemplo de creación de diccionarios:
claves = ["nombre", "edad", "ciudad"]  
valores = ["María", 35, "Madrid"]  

diccionario = dict(zip(claves, valores))  
print(diccionario)  # Salida: {'nombre': 'María', 'edad': 35, 'ciudad': 'Madrid'}  

Puntos clave:  
zip() devuelve un iterador, por lo que debes convertirlo a una lista o tupla si necesitas almacenar los resultados.  
Es una forma eficiente y concisa de combinar y procesar datos de múltiples iterables.  