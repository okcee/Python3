# Método \_\_iter__

La función iter() en Python es una herramienta fundamental para trabajar con iteradores. Permite convertir un objeto iterable en un objeto iterador.  

Aquí te explico los aspectos clave:
- Función principal  
La función iter() se utiliza para obtener un objeto iterador a partir de un objeto iterable.  
Un objeto iterable es cualquier objeto que puede ser recorrido, como listas, tuplas, cadenas, diccionarios, conjuntos, etc.  
Un objeto iterador es un objeto que produce valores uno a la vez cuando se le solicita.  

- Funcionamiento detallado  
Cuando se llama a iter() con un objeto iterable, Python llama internamente al método __iter__() del objeto.  
El método __iter__() devuelve un objeto iterador.  
El objeto iterador tiene un método __next__() que se utiliza para obtener el siguiente valor en la secuencia.  
Cuando no hay más valores disponibles, el método __next__() genera una excepción *StopIteration*  

# Relación con el bucle for

El bucle for en Python utiliza internamente la función iter() para obtener un iterador del objeto iterable que se está recorriendo.  
Luego, el bucle for llama repetidamente a la función next() en el iterador para obtener los valores.  
Cuando se genera la excepción StopIteration, el bucle for se detiene.  

## Ejemplos de uso

Con una lista:  
mi_lista = [1, 2, 3]  
mi_iterador = iter(mi_lista)  

print(next(mi_iterador))  # Salida: 1  
print(next(mi_iterador))  # Salida: 2  
print(next(mi_iterador))  # Salida: 3  
#print(next(mi_iterador))  # Genera StopIteration  

Con una cadena:  
mi_cadena = "Hola"  
mi_iterador = iter(mi_cadena)  

print(next(mi_iterador))  # Salida: H  
print(next(mi_iterador))  # Salida: o  
print(next(mi_iterador))  # Salida: l  
print(next(mi_iterador))  # Salida: a  
#print(next(mi_iterador)) # Genera StopIteration  

