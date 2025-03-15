**find()**  
cadena.find(subcadena, inicio, fin)
* Parámetros:
  * cadena: La cadena en la que deseas buscar la subcadena.
  * subcadena (obligatoria): La subcadena que deseas encontrar en la cadena.
  * inicio: (Opcional) El índice donde quieres que comience la búsqueda. Si no se especifica, la búsqueda comienza desde el principio de la cadena (índice 0).
  * fin: (Opcional) El índice donde quieres que termine la búsqueda. Si no se especifica, la búsqueda continúa hasta el final de la cadena.
* Valor de retorno: Si la subcadena se encuentra dentro de la cadena, find() devuelve el índice de la primera aparición de la subcadena. Si la subcadena no se encuentra, find() devuelve -1.  
* La función find() realiza una búsqueda de izquierda a derecha.
* Es sensible a mayúsculas y minúsculas, lo que significa que distingue entre "Hola" y "hola".
* Los parámetros inicio y fin te permiten limitar el rango de búsqueda dentro de la cadena.