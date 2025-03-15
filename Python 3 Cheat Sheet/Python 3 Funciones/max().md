# Función max()
La función max() en Python es una función incorporada que se utiliza para encontrar el valor máximo de un conjunto de valores. Puede utilizarse de dos maneras principales:  1

1. Encontrar el valor máximo en un iterable:  
   - Un iterable puede ser una lista, una tupla, un conjunto, un diccionario (devuelve la clave máxima), o cualquier otro objeto que pueda ser iterado.  
   - max(iterable) devuelve el elemento más grande del iterable.  

2. Encontrar el valor máximo entre múltiples argumentos:  
   - max(arg1, arg2, arg3, ...) devuelve el argumento más grande entre los valores proporcionados.  

## Parámetros opcionales:
- **key:**
Este parámetro permite especificar una función que se utiliza para determinar el orden de los elementos.  
Por ejemplo, se puede utilizar para encontrar la palabra más larga en una lista de cadenas.  
- **default:**
Este parámetro especifica un valor que se devuelve si el iterable está vacío.  
Si el iterable esta vacío, y no se especifica un valor default, se producirá un error.  

# Puntos clave:
- max() funciona con diferentes tipos de datos, siempre que sean comparables.  
- Cuando se trabaja con cadenas, la comparación se basa en el orden lexicográfico (orden alfabético).  
- Es una función de python muy util, para encontrar valores máximos en una gran diversidad de casos.  