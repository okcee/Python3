# El método readline()

El método readline() en Python es una herramienta fundamental para la lectura de archivos de texto. Permite leer un archivo línea por línea, lo que resulta muy útil cuando se trabaja con archivos grandes o cuando se necesita procesar el contenido de un archivo de manera secuencial.  

## Funcionamiento básico

- El método readline() se utiliza sobre un objeto de archivo abierto en modo de lectura ('r').  
- Cada vez que se llama a readline(), lee una línea completa del archivo, incluyendo el carácter de nueva línea ('\n') al final.  
- Si se llega al final del archivo, readline() devuelve una cadena vacía ('').  

### Ejemplo de uso

try:  
    with open('mi_archivo.txt', 'r') as archivo:  
        linea = archivo.readline()  
        while linea:  
            print(linea, end='')  # end='' evita líneas en blanco adicionales  
            linea = archivo.readline()  
except FileNotFoundError:  
    print("El archivo no fue encontrado.")  
except Exception as e:  
    print(f"Ocurrió un error: {e}")  

## Puntos clave  

- Lectura secuencial: readline() permite procesar archivos línea por línea, lo que es eficiente para archivos grandes.  
- Carácter de nueva línea: La cadena devuelta por readline() incluye el carácter '\n'. Puedes usar el método rstrip() para eliminarlo si es necesario.  
- Final del archivo: Cuando se alcanza el final del archivo, readline() devuelve una cadena vacía.  
- Manejo de errores: Es importante incluir un bloque try...except para manejar posibles errores, como que el archivo no exista.  
- Alternativas:  
  - readlines(): Lee todas las líneas del archivo y las devuelve como una lista.  
  - Bucle for: La forma más pythonica de leer un fichero linea por linea.  

## Consideraciones adicionales

- Para archivos muy grandes, leer línea por línea con readline() o con un bucle for puede ser más eficiente que cargar todo el archivo en la memoria con readlines().  
- El método readline() también puede recibir un argumento opcional que especifica el número máximo de caracteres a leer.  