'''Operadores de menor a mayor precedencia (se refiere al orden en que se evalúan las expresiones que contienen múltiples operadores.)
- yield x => Protocolo de generadores “send”
lambda args: expresión => Función anónima
x if y else z => Selección ternaria (retorna x si y es cierta)
x or y OR lógico => (y es evaluada sólo si x es falsa)
x and y AND lógico => (y es evaluada sólo si x es verdadera)
not x => Negación Lógica
x in y, x not in y => Operadores de membresía
x is y, y is not y => Operadores de identidad
x < y, x<= y, x > y, x >= y => Comparación de magnitudes. Set, subset y superset
x == y, x != y => Operadores de igualdad
x | y Bit a bit (bitwise) OR. => Unión de sets (conjuntos)
x ^ y Bitwise XOR. => Diferencia simétrica de sets
x & y Bit a bit AND. => Intersección de sets (conjuntos)
x << y, x >> y => Desplazamiento de x en y bits a izquierda y derecha
x + y Adición. => Concatenación
x - y Substración. => Diferencia entre sets (conjuntos)
x * y Multiplicación. => Repetición
x % y => Resto de la división
x / y => División real (verdadera)
x // y => División truncada
-x, +x => Negación. Identidad
~x => Negación Bit a bit
x ** y => Potencia (exponenciación)
x[i] => Indexado (secuencias, mapeados, otros)
x[i:j:k] => Troceado (slicing)
x(...) => Llamada (función, método, clase, etc.)
x.attr => Referencia a un atributo
(...) => Tupla, expresión, expresión de generador
[...] => Lista, lista por comprensión
{...} => Diccionario, Set, comprensión de diccionarios y sets
'''

'''
Python sigue reglas de precedencia similares a las matemáticas:
- Paréntesis: Los paréntesis tienen la máxima precedencia. Se evalúa primero lo que está dentro de los paréntesis.
- Potencias: Las potencias (**) se evalúan de derecha a izquierda.
- Multiplicación, división, módulo y división entera: Estos operadores tienen la misma precedencia y se evalúan de izquierda a derecha.
- Suma y resta: Estos operadores tienen la misma precedencia y se evalúan de izquierda a derecha.
- Comparaciones: Operadores como ==, !=, <, >, <=, >= se evalúan después de las operaciones aritméticas.
- Operadores lógicos: and, or y not se evalúan al final.
'''

'''OPERADORES'''

#   Módulo. Nos devuelve el resto de una división:
n_numerador = 85
n_denominador = 9
n_resto = n_numerador%n_denominador
print("El resto de dividir" , n_numerador , "entre" , n_denominador , "es" , n_resto)

#   ==  Igual que...
#   No confundir con el operador de asignación =
#   Con = le damos un valor a una variable. Con == comprobamos si dos objetos son iguales.

n_numero1 = 34
s_texto1 = "34"
n_numero1 == s_texto1


n_numero2 = 34
n_numero3 = 34
n_numero2 == n_numero3

#   !=  Diferente que...

n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5

#   +=  Suma e incremento

n_numero6 = 34
n_numero6 += 1 #Sería como poner: n_numero6 = n_numero6 +1 
print(n_numero6)

'''OPERADORES LÓGICOS'''
a = True
b = False
resultado = a and b
# print(resultado)

resultado = a or b
# print(resultado)

resultado = not a
print(resultado)

#----------------------------------
# Sintaxis simplificada para varios operadores lógicos
edad = input('Introduce tu edad: ')


#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad <40
#print(treintas)

if ( 20 <= edad < 30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
#    if veintes:
#        print('Dentro de los 20\'s')
#    elif treintas:
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de rango')
else:
    print("No está dentro de los 20's ni 30's")

# Módulo. Nos devuelve el resto de una división:
n_numerador = 85
n_denominador = 9
n_resto = n_numerador%n_denominador
print("El resto de dividir" , n_numerador , "entre" , n_denominador , "es" , n_resto)

# == Igual que...
# No confundir con el operador de asignación =
# Con = le damos un valor a una variable. Con == comprobamos si dos objetos son iguales.
n_numero1 = 34
s_texto1 = "34"
n_numero1 == s_texto1
n_numero2 = 34
n_numero3 = 34
n_numero2 == n_numero3

# != Diferente que...
n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5

# += Suma e incremento
n_numero6 = 34
n_numero6 += 1 #Sería como poner:
n_numero6 = n_numero6 +1
print(n_numero6)

'''Operadores lógicos'''
a = True
b = False
resultado = a and b
# print(resultado)
resultado = a or b
# print(resultado)
resultado = not a
print(resultado)

#----------------------------------

# Sintaxis simplificada para varios operadores lógicos
edad = int(input('Introduce tu edad: '))
#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad <40
#print(treintas)
if ( 20 <= edad < 30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
# if veintes:
# print('Dentro de los 20\'s')
# elif treintas:
# print('Dentro de los 30\'s')
# else:
# print('Fuera de rango')
else:
    print("No está dentro de los 20's ni 30's")