# Algoritmos de clasificación

La ordenación es fundamental en programación. Un algoritmo de ordenamiento organiza una lista de elementos en un orden específico (ascendente o descendente). La eficiencia de un algoritmo se mide por su complejidad temporal (cuánto tiempo tarda) y espacial (cuánta memoria usa).

1. Insertion Sort (Ordenamiento por Inserción)  
- Cómo funciona: Divide la lista en una parte ordenada y otra no ordenada. Toma elementos de la parte no ordenada y los inserta en la posición correcta en la parte ordenada. Es como ordenar cartas en la mano.  
- Complejidad:  
  - Temporal: O(n²) (no eficiente para grandes listas).  
  - Espacial: O(1) (usa poca memoria extra).  
- Cuándo usarlo:  
  - Listas pequeñas o casi ordenadas.  
  - Implementación sencilla.  

2. Selection Sort (Ordenamiento por Selección)  
- Cómo funciona: Divide la lista en una parte ordenada y otra no ordenada. Encuentra el elemento mínimo en la parte no ordenada y lo intercambia con el primer elemento no ordenado. Repite hasta que toda la lista esté ordenada.  
- Complejidad:  
  - Temporal: O(n²) (no eficiente para grandes listas).  
  - Espacial: O(1) (usa poca memoria extra).  
- Cuándo usarlo:  
  - Listas pequeñas.  
  - Número de intercambios limitado.  

3. Bubble Sort (Ordenamiento de Burbuja)
- Cómo funciona: Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Repite hasta que no haya más intercambios. Los elementos "más grandes" se mueven hacia el final de la lista como burbujas.  
- Complejidad:  
  - Temporal: O(n²) (muy ineficiente para grandes listas).  
  - Espacial: O(1) (usa poca memoria extra).  
- Cuándo usarlo:  
- Fines educativos (fácil de entender). Nunca en aplicaciones prácticas con grandes conjuntos de datos.  

4. Merge Sort (Ordenamiento por Mezcla)  
- Cómo funciona: Divide la lista en mitades recursivamente hasta que cada sublista tenga un solo elemento. Combina (mezcla) las sublistas ordenadas en listas más grandes y ordenadas. Sigue el principio de "divide y vencerás".  
- Complejidad:  
  - Temporal: O(n log n) (muy eficiente para grandes listas).  
  - Espacial: O(n) (requiere memoria adicional).  
- Cuándo usarlo:  
  - Grandes listas.  
  - Necesidad de un algoritmo estable.  

## Resumen
- Insertion Sort, Selection Sort y Bubble Sort: Simples de implementar, pero ineficientes (O(n²)) para grandes listas.  
- Merge Sort: Más complejo, pero mucho más eficiente (O(n log n)) para grandes listas.  
- La elección del algoritmo depende del tamaño de la lista y los requisitos de la aplicación.  