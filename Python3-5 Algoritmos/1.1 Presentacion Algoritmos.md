# ¿Qué es un algoritmo?
- Un algoritmo es una secuencia de instrucciones cuyo objetivo es la resolución de un problema.  
- Un mismo problema puede tener múltiples soluciones, y necesitamos evaluar cuál es la mejor.  

# Complejidad algorítmica
- Se evalúa la eficiencia de un algoritmo en términos de:  
  - Complejidad temporal (tiempo de ejecución).  
  - Complejidad espacial (uso de recursos del sistema).  
- La complejidad temporal es generalmente más importante debido a la limitación del tiempo.  
- En lugar de medir el tiempo real, contamos el número de instrucciones para obtener una medida independiente del hardware.  
- La complejidad algorítmica se expresa como una función que describe cómo el tiempo de ejecución aumenta con el tamaño de la entrada.  

## Factores que afectan la complejidad
- El tamaño de los datos de entrada influye directamente en el tiempo de ejecución.  
- Los bucles y las comparaciones dentro del algoritmo contribuyen a su complejidad.  

## Medición de la complejidad

- La complejidad algorítmica no es un número fijo, sino una función que describe cómo escala el tiempo de ejecución con el tamaño de la entrada.  
- Para obtener una medición independiente del hardware, contamos el número de instrucciones en lugar del tiempo real de ejecución.  

### En resumen

- La complejidad algorítmica nos ayuda a entender cómo se comporta un algoritmo a medida que aumenta el tamaño de los datos, permitiéndonos comparar y elegir los algoritmos más eficientes.  
- Cuantos más datos, la curva de complejidad algorítmica se va haciendo cada vez más grande. Esto es lo que realmente nos interesa ver en una complejidad algorítmica, cómo se comporta el algoritmo con volúmenes de entradas grandes en el tiempo.  

# Órden de Complejidad

E posible medir cualquier algoritmo. Pero incluso así es complicado comparar unos algoritmos con otros. Además, se requiere poder categorizar lo complejo que es un algoritmo con respecto a otros. Para esto recurriremos al orden de complejidad.  
Para el peor de los casos la complejidad algorítmica sería: F(x)=n  
Para expresar el peor caso usaremos una notación conocida como “O Grande” y se escribe: O(n)  
Que significa complejidad en el peor caso. Se escribe como “O” pero en realidad es la letra griega Omicron.

## Orden de Complejidad (Big-O)

### Propósito:
- Permite categorizar y comparar la eficiencia de los algoritmos de manera estándar.  
- Simplifica el análisis de algoritmos al enfocarse en el comportamiento del peor caso con grandes volúmenes de datos.  

### Simplificación:
- Las notaciones Big-O simplifican las ecuaciones de complejidad, eliminando términos irrelevantes para grandes conjuntos de datos.  
- Algoritmos con comportamientos de crecimiento similares se agrupan en órdenes de complejidad.  

### Órdenes de Complejidad Comunes:
- **Constante (O(1))**: Tiempo de ejecución constante, independiente del tamaño de la entrada.  
- **Lineal (O(n))**: El tiempo de ejecución crece linealmente con el tamaño de la entrada.  
- **Polinómico (O(n^c))**: El tiempo de ejecución crece como una potencia del tamaño de la entrada (cuadrático, cúbico, etc.).  
- **Logarítmico (O(log n))**: El tiempo de ejecución crece logarítmicamente con el tamaño de la entrada.  
- **Enelogarítmico (O(n log n))**: Combinación de comportamiento lineal y logarítmico. Combinan características de los algoritmos lineales (O(n)) y logarítmicos (O(log n)). Esto significa que su tiempo de ejecución crece de manera proporcional al tamaño de la entrada (n) multiplicado por el logaritmo del tamaño de la entrada (log n). Ofrecen un buen equilibrio entre velocidad y escalabilidad. Ejemplos comunes: QuickSort y MergeSort.  
- **Exponencial (O(2^n))**: El tiempo de ejecución crece exponencialmente con el tamaño de la entrada.  

### Importancia de la Notación Big-O:
- Permite comparar algoritmos independientemente del hardware.  
- Ayuda a identificar algoritmos ineficientes (cuadráticos, exponenciales) que requieren revisión.  
- Fomenta la documentación de la complejidad algorítmica en el código para facilitar el mantenimiento y la optimización. 

### Comparación de Complejidades:
- Muestra cómo el tiempo de ejecución aumenta drásticamente con la complejidad del algoritmo, especialmente con grandes conjuntos de datos.  
- La notación Big O, es una herramienta muy útil para poder elegir entre algoritmos que realizan la misma tarea, para que en el momento en que se trabaje con grandes cantidades de datos, el programa no se ralentice.  

# Análisis asintótico
El análisis asintótico nos permite comprender y comparar la eficiencia de los algoritmos a medida que el tamaño de la entrada aumenta. Al centrarnos en el orden de crecimiento, podemos predecir cómo se comportarán los algoritmos en situaciones del mundo real y tomar decisiones informadas sobre qué algoritmos son más adecuados para cada tarea.  
**¿Por qué es importante?**
- Escalabilidad: Nos permite predecir cómo se comportará un algoritmo cuando se enfrenta a grandes cantidades de datos. Esto es crucial en aplicaciones que manejan grandes volúmenes de información.  
- Comparación de algoritmos: Nos proporciona una forma de comparar la eficiencia de diferentes algoritmos, incluso si se implementan en diferentes lenguajes de programación o en diferentes computadoras.  
- Optimización: Nos ayuda a identificar los cuellos de botella en un algoritmo y a determinar dónde se pueden realizar mejoras para que sea más eficiente.  

Las notaciones son fundamentales para entender la eficiencia de los algoritmos.  

## Hay principalmente tres notaciones asintóticas:

1. **Notación Theta (Θ): Límite Exacto**  
La notación Theta (Θ) define un límite ajustado para el tiempo de ejecución de un algoritmo. En otras palabras, proporciona tanto un límite superior como un límite inferior.  
Cuando decimos que un algoritmo tiene una complejidad Θ(g(n)), significa que su tiempo de ejecución crecerá a la misma velocidad que g(n), tanto en el mejor como en el peor de los casos.  
Significado: Es la notación más precisa, ya que describe el comportamiento exacto del algoritmo a medida que el tamaño de la entrada aumenta.  
Ejemplo:  
Si un algoritmo siempre realiza una cantidad de operaciones proporcional a n², entonces su complejidad sería Θ(n²).  

2. **Notación Omega (Ω): Límite Inferior**  
La notación Omega (Ω) define un límite inferior para el tiempo de ejecución de un algoritmo.  
Cuando decimos que un algoritmo tiene una complejidad Ω(g(n)), significa que su tiempo de ejecución siempre será al menos tan grande como g(n), en el mejor de los casos.  
Significado: Nos proporciona una garantía sobre el mejor rendimiento posible del algoritmo.  
Ejemplo:  
Un algoritmo de búsqueda que, en el mejor de los casos, encuentra el elemento buscado en el primer paso, tendría una complejidad Ω(1).  

3. **Notación Big-O (O): Límite Superior**
La notación Big-O (O) define un límite superior para el tiempo de ejecución de un algoritmo.  
Cuando decimos que un algoritmo tiene una complejidad O(g(n)), significa que su tiempo de ejecución nunca será mayor que g(n), en el peor de los casos.  
Significado: Es la notación más utilizada, ya que nos proporciona una garantía sobre el peor rendimiento posible del algoritmo.  
Ejemplo:  
Un algoritmo de ordenamiento que, en el peor de los casos, realiza una cantidad de operaciones proporcional a n², tendría una complejidad O(n²).  

## Puntos Clave
Relación entre las notaciones:  
- Si un algoritmo tiene una complejidad Θ(g(n)), entonces también tiene una complejidad O(g(n)) y Ω(g(n)).  
- La notación Big-O es la más común porque es muy util el conocer el peor de los casos de un algoritmo.  

Importancia práctica:  
- Estas notaciones nos permiten comparar la eficiencia de diferentes algoritmos y elegir el más adecuado para una tarea específica.  
- Son fundamentales para el diseño y análisis de algoritmos eficientes, especialmente cuando se trabaja con grandes conjuntos de datos.  
