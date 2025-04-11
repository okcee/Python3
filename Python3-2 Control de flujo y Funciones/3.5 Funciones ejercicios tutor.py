"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

# Funcion que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto:'))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')

#---------------------------------------
#---------------------------------------
"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Realizamos algunas pruebas de conversion
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Imprimimos el resultado
print(f'{celsius} C a F: {resultado:.2f}')

# Realizamos la prueba de grados fahrenheit a celsius
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
# Imprimimos el resultado
print(f'{fahrenheit} F a C: {resultado:0.2f}')

'''Ejercicio de codificación : Operaciones Matemáticas
Operaciones Matemáticas Básicas
Objetivo:
Escribe una función en Python llamada operaciones_matematicas que reciba dos números enteros a y b, y realice las siguientes operaciones matemáticas:
Suma: a + b
Resta: a - b
Multiplicación: a * b
División: a / b, si b es diferente de 0; de lo contrario, devolver el mensaje "División por cero no permitida".
Resto de la división: a % b, si b es diferente de 0; de lo contrario, devolver el mensaje "División por cero no permitida".
La función debe devolver estos cinco resultados en una tupla.
Ejemplo de entrada y salida:
a = 10
b = 3
resultado = operaciones_matematicas(a, b)
print("Suma:", resultado[0])         # 13
print("Resta:", resultado[1])        # 7
print("Multiplicación:", resultado[2]) # 30
print("División:", resultado[3])     # 3.3333...
print("Residuo:", resultado[4])      # 1
Requisitos:
La función debe manejar correctamente la división por cero.
Debe devolver los resultados como una tupla (suma, resta, multiplicación, división, resto).
Prueba la función con diferentes valores de entrada para verificar su correcto funcionamiento.'''
a = 10
b = 3

def operaciones_matematicas(a, b):
    if b != 0:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b
        resto = a % b
        return suma, resta, multiplicacion, division, resto
    else:
        return "División por cero no permitida"

resultado = operaciones_matematicas(a, b)
print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])
print("Residuo:", resultado[4])

'''Calcular la suma y promedio de una lista de números
Desarrolla una función llamada 'calcular_suma_y_promedio' que tome como entrada una lista de números y calcule la suma de todos los números de la lista y el promedio de esos números.
La función devolverá un diccionario con los resultados de la suma y el promedio
def calcular_suma_y_promedio(lista_numeros):
# Pruebas
numeros = [1, 2, 3, 4, 5]
resultado = calcular_suma_y_promedio(numeros)
print("Suma:", resultado["suma"])
print("Promedio:", resultado["promedio"])
Suma: 15
Promedio: 3.0'''
numeros = [1, 2, 3, 4, 5]
def calcular_suma_y_promedio(lista_numeros):
    if not lista_numeros:
        return {"suma": 0, "promedio": 0}
    suma_total = sum(lista_numeros)
    cantidad_numeros = len(lista_numeros)
    promedio_total = suma_total / cantidad_numeros
    resultados = {"suma": suma_total, "promedio": promedio_total}
    return resultados
resultado = calcular_suma_y_promedio(numeros)
print("Lista de números:", numeros)
print("Suma:", resultado["suma"]) 
print("Promedio:", resultado["promedio"])

'''Frecuencia de elementos en una lista
Crear una función denominada 'contar_frecuencia' que tome una lista de números y calcule las veces (frecuencia) que aparece cada número en la lista y devuelva los resultados en forma de diccionario, donde cada clave será cada número distinto de la lista y cada valor será el número de veces que aparece ese número en la lista.
def contar_frecuencia(lista):
# Ejemplo de uso
elementos = [1, 2, 2, 3, 1, 2, 4, 5, 4]
resultado = contar_frecuencia(elementos)
print(resultado) {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}'''

elementos = [1, 2, 2, 3, 1, 2, 4, 5, 4]
def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia
resultado = contar_frecuencia(elementos)
print(resultado)

'''Aplicar una Función y Filtrar Elementos en una Lista
Aplicar una Función y Filtrar Resultados
Objetivo:
Escribe una función en Python llamada aplicar_funcion_y_filtrar que tome dos argumentos:
lista: Una lista de números enteros.
valor_umbral: Un número entero que servirá como umbral para filtrar los resultados.
Funcionamiento de la función:
La función debe elevar al cuadrado cada elemento de la lista.
Luego, debe filtrar y devolver solo aquellos valores que sean mayores que valor_umbral.
Ejemplo de entrada y salida:
numeros = [1, 2, 3, 4, 5]
valor_umbral = 3
resultado = aplicar_funcion_y_filtrar(numeros, valor_umbral)
print(resultado)
Salida esperada: [4, 9, 16, 25]'''

numeros = [1, 2, 3, 4, 5]
valor_umbral = 3
def aplicar_funcion_y_filtrar(lista, valor_umbral):
    cuadrados = [x**2 for x in lista]
    condicion = lambda numero_cuadrado: numero_cuadrado > valor_umbral
    iterador_filtrado = filter(condicion, cuadrados)
    resultado_final = list(iterador_filtrado)
    return resultado_final

resultado = aplicar_funcion_y_filtrar(numeros, valor_umbral)
print(resultado)