# Función range()

La función range() en Python es una función incorporada que se utiliza para generar una secuencia de números enteros. Es muy útil cuando necesitas iterar sobre una secuencia de números, especialmente en bucles for.  

## ¿Cómo funciona range()?

range() puede tomar uno, dos o tres argumentos:  
- range(stop): Genera una secuencia de números enteros desde 0 hasta stop - 1.  
Por ejemplo, range(5) generará la secuencia 0, 1, 2, 3, 4.  
- range(start, stop): Genera una secuencia de números enteros desde start hasta stop - 1.  
Por ejemplo, range(2, 7) generará la secuencia 2, 3, 4, 5, 6.  
- range(start, stop, step): Genera una secuencia de números enteros desde start hasta stop - 1, con un incremento de step.  
Por ejemplo, range(1, 10, 2) generará la secuencia 1, 3, 5, 7, 9.

### Ejemplos:
1. Bucle for con range():  
for i in range(5):  
    print(i)  
Este código imprimirá: 
0  
1  
2  
3  
4  

2. range() con start y stop:  
for i in range(3, 8):  
    print(i)  
Este código imprimirá: 
3  
4  
5  
6  
7  

3. range() con start, stop y step:  
for i in range(0, 10, 2):  
    print(i)  
Este código imprimirá:  
0  
2  
4  
6  
8  

## Puntos clave:
- range() devuelve un objeto iterable, no una lista. Si necesitas una lista, puedes convertir el resultado de range() usando list(range(...)).  
- Los argumentos de range() deben ser números enteros.  
- range() es muy eficiente en memoria, ya que no almacena todos los números en la secuencia a la vez, sino que los genera a medida que se necesitan.  
- Una de las ventajas de range con respecto a otras estructuras semejantes (como una lista o una tupla) es que range va a ocupar siempre una cantidad mínima de memoria (la necesaria para almacenar los argumentos start, stop y step), calculándose los números generados o los subrangos cuando resulte necesario.  
