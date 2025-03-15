**for**  
*Estructura básica*  
for variable in iterable: # cuerpo del bucle  
* *for* variable *in* iterable::
* *for*: Palabra clave que inicia el bucle.
* *variable*: Es el nombre de la variable que tomará el valor de cada elemento del iterable en cada iteración.
* *in*: Palabra clave que conecta la variable con el iterable.
* *iterable*: Es cualquier objeto que pueda devolver sus elementos uno a la vez. Ejemplos comunes son:
  * Listas: frutas = ["manzana", "banana", "cereza"]
  * Tuplas: coordenadas = (3, 5)
  * Cadenas: mensaje = "Hola"
  * Diccionarios: persona = {"nombre": "Ana", "edad": 30}
  * Objetos range: range(inicio, fin, paso)

*Control del bucle*  
* break: Sale del bucle prematuramente.
* continue: Salta la iteración actual y pasa a la siguiente.
* else: Se ejecuta si el bucle termina sin ser interrumpido por break.