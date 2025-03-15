'''Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.'''
print ("¡Hola Mundo!")

'''Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.'''
s_var="¡Hola Mundo!"
print(s_var)

'''Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido'''
s_name=input("Por favor, introduce tu nombre: ") # Creo una variable
print("¡Hola ",s_name,"!") # Imprimo strings y la variable

'''Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
((3+2)/(2*5))^2'''
f_var=((3+2)/(2*5))**2
print(f_var)

'''Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''
i_horas=int(input("¿Cuántas horas as trabajado? "))
f_coste=float(input("¿Cuánto es salario acordado por hora trabajada? "))
f_paga=i_horas*f_coste
print=(f"La paga que corresponde es igual a {f_paga}")

'''Ejercicio 6
Escribir un programa que lea un entero positivo, "n" , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta "n". La suma de los "n"  primeros enteros positivos puede ser calculada de la siguiente forma:
suma = n(n+1) / 2
'''
try:
    numero = int(input("Introduce un número entero: "))
    print("El número introducido es:", numero)
    suma = (numero * (numero+1)) / 2
    print("La suma de los números primeros enteros es:", suma)
except ValueError:
    print("Error: Debes introducir un número entero válido.")

'''Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
'''
#NOTA: IMC = peso (kg) / altura² (m)
f_peso=float(input("¿Cuál es tu peso en Kilogramos?"))
f_altura=float(input("¿Cuánto mides en metros?"))
f_IMC = round(f_peso / f_altura**2, 2) # Redondeo a 2 decimales
print("Tu índice de masa corporal es ", f_IMC)

'''Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
cociente = dividendo // divisor  # cociente = 3
resto = dividendo % divisor     # resto = 2
'''
n=int(input("Escribe el primer número entero "))
m=int(input("Escribe el segundo número entero "))
c=(n//m)
r=(n%m)
print("la división del número ",n, "entre el número",m, "da un cociente de ",c, "y un resto de ",r)

'''Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

Fórmula del Interés Compuesto
La fórmula para calcular el capital final (Cf) después de un período de inversión con interés compuesto es:
Cf = Ci * (1 + i)^n
Donde:
Cf: Capital final (lo que queremos calcular).
Ci: Capital inicial (la cantidad invertida).
i: Tasa de interés anual (expresada como decimal).
n: Número de años.
'''
def calcular_capital_final():
    """Calcula el capital final de una inversión con interés compuesto."""

    try:
        cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
        interes_anual = float(input("Introduce el interés anual (en porcentaje): ")) / 100
        numero_años = int(input("Introduce el número de años: "))

        capital_final = cantidad_invertir * (1 + interes_anual) ** numero_años

        print(f"El capital obtenido en la inversión es: {capital_final:.2f}")

    except ValueError:
        print("Error: Introduce valores numéricos válidos.")

calcular_capital_final()

'''Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
'''
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))

'''Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''
dinero = float(input("Cuál es la cantidad de dinero depositada en la cuenta de ahorros: "))

saldo = dinero
saldos = []

for i in range(3):
    saldo = saldo * 1.04
    saldos.append(saldo)
    
print("Cantidad de ahorros tras el primer año: %.2f" % saldos[0])
print("Cantidad de ahorros tras el segundo año: %.2f" % saldos[1])
print("Cantidad de ahorros tras el tercer año: %.2f" % saldos[2])

'''Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''
precioBarra=3.49
descuento=60/100
precioBanterior=3.49*descuento
vendidas=int(input("¿Cuál es el número de barras vendidas que no son del día?"))
costeFinal=vendidas*precioBanterior
print("El precio habitual de una barra de pan es: ", precioBarra,  "€")
print("El descuento que se le hace por no ser fresca es: " + str(round(descuento*100, 2)), "%")
print("El coste final total es: ", round(costeFinal, 2),  "€")
