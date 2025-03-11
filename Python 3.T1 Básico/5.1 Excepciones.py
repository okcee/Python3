# A continuación, vamos a crear un código que generará una excepción si se le introduce un parámetro adecuado.
# 1. El bloque try/except es la base del manejo de excepciones en Python
'''
try:
    # Código que puede generar una excepción
except TipoDeExcepcion:
    # Código para manejar la excepción'''
# Ejemplo 1 - try/except:
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ValueError:
    print("¡Error! Debes introducir un número entero.")
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")
'''   
Excepciones múltiples: Puedes incluir múltiples bloques except para manejar diferentes tipos de excepciones.
Bloque except genérico: Si no especificas un tipo de excepción, el bloque except capturará cualquier excepción que ocurra. (No es una práctica recomendada, ya que dificulta la depuración).
''' 
# Ejemplo 2 - try/except: En este ejemplo, el bloque try/except captura la excepción IndexError y devuelve un mensaje de error en lugar de bloquear el programa.
def indexador(objeto, indice):
    try:
        return objeto[indice]
    except IndexError:
        return "Índice fuera de rango"

print(indexador('Python', 0))
print(indexador('Python', 10))
print(indexador('Python', -1))

# Función indexador: La función indexador(objeto, indice) es una forma sencilla de acceder a un elemento de una secuencia (como una cadena) utilizando un índice. Cuando el índice está dentro del rango válido de la secuencia, la función devuelve el elemento correspondiente.
# IndexError: Cuando intentas acceder a un índice que está fuera del rango de la secuencia (por ejemplo, un índice mayor o igual a la longitud de la cadena), Python genera una excepción IndexError. Esta excepción indica que estás intentando acceder a una posición que no existe en la secuencia.

# 2. try/finally: Asegurando la limpieza de recursos
# El bloque try/finally se utiliza para garantizar que un bloque de código se ejecute siempre, independientemente de si se produce o no una excepción. Esto es especialmente útil para liberar recursos como archivos, conexiones de red o bloqueos.

#Ejemplo: try/finally
archivo = open("datos.txt", "r")
try:
    lineas = archivo.readlines()
    # Procesar las líneas del archivo
finally:
    archivo.close()  # Asegurar que el archivo se cierre siempre
# Combinación con except: Puedes combinar try/finally con try/except para manejar excepciones y asegurar la limpieza de recursos.

# 3. Lanzando excepciones manualmente
def calcular_edad(año_nacimiento):
    if año_nacimiento > 2023:
        raise ValueError("El año de nacimiento no puede ser posterior al año actual.")
    return 2023 - año_nacimiento
try:
    edad = calcular_edad(2025)
except ValueError as error:
    print("¡Error!", error)
# Relanzar excepciones: Dentro de un bloque except, puedes utilizar raise sin argumentos para relanzar la excepción capturada.

# 4. assert: Verificaciones condicionales. Dispara una excepción condicionalmente.
def dividir(a, b):
    assert b != 0, "No se puede dividir por cero"
    return a / b

resultado = dividir(10, 0)  # Esto generará un AssertionError
# Desactivación: Las sentencias assert se pueden desactivar globalmente en tiempo de ejecución, por lo que no deben utilizarse para manejar errores críticos en producción.

'''Creando excepciones manualmente'''
# Creamos la clase MiPropiaExcepcion que hereda de Exception.
class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
    pass
raise miPropiaExcepcion

# Cuando una clase hereda de Exception, podemos incluirla dentro de una sentencia raise para lanzarla, así como dentro de un except para interceptarla:
class miPropiaExcepcion(Exception): #Lasexcepciones heredan de Exception
    pass
try:
    raise miPropiaExcepcion
except miPropiaExcepcion:
    print('He capturado mi propia excepción')
'''Resultado: He capturado mi propia excepci�n'''

# Ejemplo sentencia finally:
"""
Función que devuelve el elemento de un objeto (secuencia) según el índice dado.
Args:
    objeto: La secuencia (cadena, lista, tupla, etc.) de la cual se quiere obtener un elemento.
    indice: El índice del elemento que se quiere obtener.
Returns:
    El elemento en el índice dado del objeto.
"""
def indexador(objeto, indice):
    return objeto[indice]
try:
    # Intentamos acceder a un índice fuera del rango de la cadena 'Python'
    indexador('Python', 10)  # Esto generará un IndexError
except IndexError:
    # Capturamos la excepción IndexError, pero no hacemos nada específico.
    # Podríamos imprimir un mensaje de error o realizar otras acciones aquí.
    pass #El pass se usa para no hacer nada.
finally:
    # El bloque finally siempre se ejecuta, independientemente de si ocurre o no una excepción.
    # En este caso, imprime un mensaje para demostrar que se ejecuta.
    print('Esto se ejecuta incluso cuando salta la excepción')

# Nota: Aunque se lanza un IndexError, el programa no se detiene abruptamente debido al bloque finally.
# El mensaje dentro del finally se imprime antes de que el programa termine.


# Ejemplo sentencia else:
'''
Función (def divide) que divide dos números: 
Args:
    x: El numerador.
    y: El denominador.
'''
def divide(x, y):
    try:
        resultado = x / y
    # Intenta realizar la división de x entre y 
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    # Si ocurre una excepción ZeroDivisionError (división por cero),
    # imprime un mensaje de error
    else:
    # Si no ocurre ninguna excepción en el bloque try,
    # imprime un mensaje indicando que el resultado es válido
        print('El resultado es: ')
    finally:
    # El bloque finally siempre se ejecuta, independientemente de si
    # ocurre o no una excepción. Imprime un mensaje de finalización.
        print('Ejecutamos el finally')
# Llamada a la función divide con argumentos válidos (4 y 12)
divide(4, 12)
# Llamada a la función divide con un denominador cero (4 y 0),
# lo que provocará una excepción ZeroDivisionError
divide(4, 0)
