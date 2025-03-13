'''Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''
edad = int(input("¿Qué edad tienes?"))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

'''Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
passw = input("Introduce una contraseña: ")
pass2 = input("Confirma la contraseña: ")

if passw==pass2:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")

'''Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
num1 = float(input("Introduce un número como dividendo: "))
num2 = float(input("Introduce otro número como divisor: "))

try:
    division=num1/num2
    print(division)
except:
    num2==0
    print("Error, el divisor no puede ser 0")

'''Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
try:
    numero=int(input("Introduzca un numero entero"))
    if numero%2==0:
        print("El número es par")
    else:
        print("El número es impar")
except ValueError:
    print("Error: El valor introducido no es un número entero")

'''Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
edad=int(input("¿Cuántos años tienes?"))
ingresos=float(input("¿Cuáles son tus ingresos mensuales?"))

if edad>16 and ingresos>=1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")

'''Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''
nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o F)? ")

if sexo == "F":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Tu grupo es " + grupo)

'''Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''
renta=float(input("¿Cuál es tu renta anual?"))

if renta<10000:
    print("Tu tipo impositivo es del 5%")
    print(renta*0.05)

elif renta>=10000 and renta<20000:
    print("Tu tipo impositivo es del 15%")
    print(renta*0.15)

elif renta>=20000 and renta<35000:
    print("Tu tipo impositivo es del 20%")
    print(renta*0.2)

elif renta>=35000 and renta<60000:
    print("Tu tipo impositivo es del 30%")
    print(renta*0.3)

else:
    print("Tu tipo impositivo es del 45%")
    print(renta*0.45)

'''Otro modo'''

# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')

'''Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''
puntuacion = float(input("¿Qué puntuación tiene el usuario? "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    rendimiento = 0.0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    rendimiento = 0.4
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    rendimiento = puntuacion  # Usar la puntuación real para el cálculo del dinero
else:
    nivel = "Puntuación no válida"
    rendimiento = 0.0  # O manejar de otra manera, según se requiera

dinero = 2400 * rendimiento

print("El rendimiento obtenido por el usuario es:", nivel)
print("La cantidad de dinero que recibirá el usuario es:", dinero, "€")

'''Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''
edad = int(input("¿Qué edad tiene"))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10

print("El precio de la entrada es:", precio, "€")

'''Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
base = "mozzarella, tomate"
pim = "pimiento"
tof = "tofu"
pep = "peperoni"
jam = "jamón"
salm = "salmón"

tipo = input("¿Quieres una pizza vegetariana? (S/N): ").upper() # Convertir a mayúsculas para aceptar 's' o 'n'

if tipo == "S":
    ingrediente = input(f"Ingredientes vegetarianos: {pim} o {tof}: ").lower() # Convertir a minúsculas
    if ingrediente == pim:
        print(f"Pizza vegetariana con {base} y {pim}.")
    elif ingrediente == tof:
        print(f"Pizza vegetariana con {base} y {tof}.")
    else:
        print("Opción no válida.")
elif tipo == "N":
    ingrediente = input(f"Ingredientes no vegetarianos: {pep}, {jam} o {salm}: ").lower()
    if ingrediente == pep:
        print(f"Pizza no vegetariana con {base} y {pep}.")
    elif ingrediente == jam:
        print(f"Pizza no vegetariana con {base} y {jam}.")
    elif ingrediente == salm:
        print(f"Pizza no vegetariana con {base} y {salm}.")
    else:
        print("Opción no válida.")
else:
    print("Opción no válida.")
