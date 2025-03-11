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