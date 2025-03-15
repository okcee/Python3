**input()**  
input([prompt]) --> input("Por favor, ingresa tu edad: ")
```python
variable = tipo_de_dato(input("Mensaje opcional: "))
```
* variable: El nombre de la variable donde se almacenará el valor convertido.
* tipo_de_dato: El tipo de dato al que deseas convertir la entrada (por ejemplo, int, float).
* input("Mensaje opcional: "): La función input() que solicita la entrada del usuario. El "Mensaje opcional" es un texto que se muestra al usuario antes de que ingrese su dato.

Manejo de errores:  
Es importante tener en cuenta que si el usuario ingresa un valor que no se puede convertir al tipo de dato deseado, se producirá un error ValueError. Para evitar esto, puedes usar bloques try-except:  
```python
try:
    numero = int(input("Introduce un número entero: "))
    print("El número introducido es:", numero)
except ValueError:
    print("Error: Debes introducir un número entero válido.")
```