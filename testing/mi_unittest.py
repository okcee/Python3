# En el siguiente ejemplo:
from math import pi
def area(r):
    areaC = pi*(r**2)
    return areaC
valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']
for v in valores:
    areaCalculada = area(v)
    print('Para el valor', v, 'el área es', areaCalculada)
''' Analizamos los resultados:
- Para los valores 1, 3 y 0 nos da resultados correctos.
- Para -1 y -3 nos da valores que no son lo que debería dar, por lo que ya sabemos que, cuando ingresemos radios negativos, tendremos que hacer algo al respecto, como por ejemplo lanzar una excepción.
- Para el número complejo (2+3j) el resultado tampoco es lo esperado.
- Para el valor True el resultado tampoco es lo esperado.
- Para el valor ‘hola’ directamente obtenemos un error de tipo.
'''

'''
Para testear con Unittest debemos:
- Deberemos crear un archivo con el siguiente nombre:
    test_nombreArchivo.py
    En mí caso el archivo a probar es unittest.py por lo que el archivo de prueba será test_unittest.py
- Ejecutar en consola:
    python -m unittest test_mi_unittest.py
    Nota: Podemos ejecutar automáticamente las pruebas usando el comando: python -m unittest discover

'''