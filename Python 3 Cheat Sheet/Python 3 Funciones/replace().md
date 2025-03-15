**replace()**  
cadena_original.replace(cadena_a_reemplazar, cadena_reemplazo, contador)  
* Explicación de los parámetros:
  * cadena_original: Esta es la cadena de texto en la que deseas realizar el reemplazo.
  * cadena_a_reemplazar: Esta es la subcadena que quieres buscar y reemplazar dentro de cadena_original.
  * cadena_reemplazo: Esta es la subcadena que se utilizará para reemplazar todas las ocurrencias de cadena_a_reemplazar.
  * contador (opcional): Este es un número entero que especifica cuántas ocurrencias de cadena_a_reemplazar se reemplazarán. Si se omite, se reemplazarán todas las ocurrencias.  
* Puntos importantes:
  * replace() crea una nueva cadena con los reemplazos realizados. No modifica la cadena original.
  * replace() distingue entre mayúsculas y minúsculas. "Mundo" y "mundo" se consideran cadenas diferentes.
  * la función replace es muy util para normalizar datos, por ejemplo, cambiar todos los puntos por comas en un archivo csv.