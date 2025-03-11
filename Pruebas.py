# Pruebas Python3

print ("Hola Mundo")

'''
Dado un grupo de 5 personas == (A, B, C, D, E)
1. (A, B, C, D, E) == Artista, Médico, Periodista, Deportista, Juez
2. (A, C, Juez) == Té
3. (B, Periodista) == Café
4. (A, D, Deportista) == Son amigos, 2 prefieren el café
5. (C, Artista) == Son hermanos

clave -> Sabemos que 3 personas prefieren el té y 2 el café
como -> (A, C, Juez) == Té
(A *prefiere té, D, Deportista) == Son amigos, 2 prefieren el café (D, Deportista)
deducimos -> que como Café == (B, Periodista) y (D, Deportista), además != (A, C, Juez)
B == Deportista
D == Periodista
por lo cual...
E == Juez
Quedan A y C
Si (C, Artista) == Son hermanos Artista no puede ser C
A == Artista
C == Médico

- ¿Quién es el artista? A
- ¿Quién es el deportista? B
- ¿Cuál de los siguientes grupos incluye a una persona que prefiere el té pero no es juez? Ninguno de estos
(A, C, E) o (D, E) o (B, C, E)  o (B, D) o Ninguno de estos
- ¿Cuaál de las afirmaciones dadas es trivial? Ninguna
(2, 3, 4, 5, Ninguna) == Trivial
'''
'''
a+9=b ## a=(b-9) ## a=10-9=1
b*3=c ## c=(3*b) ## 33=3*b ### b=33/3=10
c-5=d ## d=(c-5) ## 28=c-5 ### c=28+5=33
d/4=7 ## d=7*4=28
¿Qué número es a?
a=1

0 = (7*4)/(a+9)*3)-5)
(a+9)*3)-5)=28
(a+9)*3=28+5
a+9=33/3
a=10-9
a=1
'''
# 150 grados
'''
Hay 8 vendedores por cada 2 gerentes
Tomaron vacaciones = 70% vendedores y 30% gerentes
¿Qué porcentaje del total de empleados tomó vacaciones?
VacacionesDisfrutadas=70%de8 + 30%de2
vd=((8*70)/100)+(2*30)/100
vd=5.6+0.6
vd=6.2
100(total)=10
x=6.2
x=62%
'''

# Declarar variables
genero = input("Ingrese el género del aspirante (mujer/hombre): ").strip().lower()
estado_civil = input("Ingrese el estado civil del aspirante (soltero/casado): ").strip().lower()
estatura = float(input("Ingrese la estatura del aspirante en metros: "))
edad = int(input("Ingrese la edad del aspirante: "))
salida = ""

# Evaluar estado civil
if estado_civil == "soltero":
    if genero == "mujer":
        if estatura > 1.60 and 20 <= edad <= 25:
            salida = "Apto"
        else:
            salida = "No es apto"
    elif genero == "hombre":
        if estatura > 1.65 and 18 <= edad <= 24:
            salida = "Apto"
        else:
            salida = "No es apto"
    else:
        salida = ""
else:
    salida = "No es apto"

# Imprimir resultado
if salida:
    print(f"El aspirante es {salida} para ingresar al ejército.")
else:
    print("Género no válido.")
