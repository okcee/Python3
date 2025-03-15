 # Función **range()**
range(start, stop, step).  
range(inicio, fin, paso)

**Argumentos:**
* inicio (opcional):
  * Es un número entero que indica el valor inicial de la secuencia.
  * Si no se especifica, el valor inicial por defecto es 0.
  * La secuencia comenzará en este número (inclusive).
* fin (obligatorio):
  * Es un número entero que indica el valor final de la secuencia.
  * La secuencia se detendrá antes de alcanzar este número (es decir, este valor no está incluido en la secuencia generada).
  * Este argumento siempre debe proporcionarse.
* paso (opcional):
  * Es un número entero que indica la diferencia entre cada número consecutivo en la secuencia.
  * Si se omite, el valor del paso por defecto es 1.
  * El paso puede ser positivo (para secuencias ascendentes) o negativo (para secuencias descendentes).
  * El paso no puede ser cero, ya que esto resultaría en una secuencia infinita (o un error).

La función range() en Python es una función incorporada que se utiliza para generar una secuencia de números enteros. Es muy útil cuando necesitas iterar sobre una secuencia de números, especialmente en bucles for.  

## ¿Cómo funciona range()?

range() puede tomar uno, dos o tres argumentos:  
- range(stop): Genera una secuencia de números enteros desde 0 hasta stop - 1.  
Por ejemplo, range(5) generará la secuencia 0, 1, 2, 3, 4.  
- range(start, stop): Genera una secuencia de números enteros desde start hasta stop - 1.  
Por ejemplo, range(2, 7) generará la secuencia 2, 3, 4, 5, 6.  
- range(start, stop, step): Genera una secuencia de números enteros desde start hasta stop - 1, con un incremento de step.  
Por ejemplo, range(1, 10, 2) generará la secuencia 1, 3, 5, 7, 9.


## Puntos clave:
- range() devuelve un objeto iterable, no una lista. Si necesitas una lista, puedes convertir el resultado de range() usando list(range(...)).  
- Los argumentos de range() deben ser números enteros.  
- range() es muy eficiente en memoria, ya que no almacena todos los números en la secuencia a la vez, sino que los genera a medida que se necesitan.  
- Una de las ventajas de range con respecto a otras estructuras semejantes (como una lista o una tupla) es que range va a ocupar siempre una cantidad mínima de memoria (la necesaria para almacenar los argumentos start, stop y step), calculándose los números generados o los subrangos cuando resulte necesario.  
