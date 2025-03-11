Trabajar con formato avanzado
https://docs.github.com/es/get-started/writing-on-github/working-with-advanced-formatting

# Organizar la información en tablas
Puedes construir tablas para organizar la información en comentarios, propuestas, solicitudes de extracción y wikis.
¿Quién puede utilizar esta característica? Markdown se puede usar en la interfaz web de GitHub.

## Creación de una tabla
Puede crear tablas con canalizaciones | y guiones -. Los guiones se usan para crear cada encabezado de columna, mientras que las barras verticales separan cada columna. Debes incluir una línea en blanco antes de tu tabla para que se representen correctamente.
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
Las barras verticales en cada lado de la tabla son opcionales.

Las celdas pueden variar en el ancho y no es necesario que estén perfectamente alineadas dentro de las columnas. Debe haber al menos tres guiones en cada columna de la línea de encabezamiento.

| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
Recorte de pantalla de una tabla de Markdown de GitHub con dos columnas de ancho diferente. Las filas muestran los comandos "git status" y "git diff" y sus descripciones.

Si editas fragmentos de código y tablas con frecuencia, puedes beneficiarte de habilitar una fuente de ancho fijo en todos los campos de comentarios de GitHub. Para más información, consulta Acerca de escritura y formato en GitHub.

Formatear el contenido dentro de tu tabla
Puede usar formatos, como vínculos, bloques de código insertados y estilos de texto en la tabla:

| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |
Recorte de pantalla de una tabla de Markdown de GitHub con los comandos con formato de bloques de código. En las descripciones se usa formato en negrita y cursiva.

Puede alinear el texto a la izquierda, a la derecha o en el centro de una columna al incluir dos puntos : a la izquierda, a la derecha o a ambos lados de los guiones en la línea de encabezamiento.

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
Recorte de pantalla de una tabla de Markdown con tres columnas tal y como se representan en GitHub, en el que se muestra cómo el texto de las celdas se puede alinear a la izquierda, al centro o a la derecha.

Para incluir una barra vertical | como contenido en su celda, utilice una \ antes de la barra vertical:

| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |
Recorte de pantalla de una tabla de Markdown tal y como se representa en GitHub, en el que se muestra cómo las canalizaciones, que normalmente cierran las celdas, se representan cuando están precedidas por una barra diagonal inversa.

# Organización de la información con secciones contraídas
Para simplificar el Markdown, crea una sección contraída con la etiqueta <details>.
Cualquier Markdown dentro del bloque <details> se contraerá hasta que el lector haga clic en  para expandir los detalles.
Opcionalmente, para que la sección se muestre como abierta de manera predeterminada, agregue el atributo open a la etiqueta <details>:
<details open>

# Bloques de código delimitados
Puede crear bloques de código delimitados colocando comillas simples triples ``` antes y después del bloque de código. Te recomendamos dejar una línea en blanco antes y después de los bloques de código para facilitar la lectura del formato sin procesar.
Tip1. Para preservar tu formato en una lista, asegúrate de dejar una sangría de ocho espacios en los bloques de código no delimitados.
##Resaltado de sintaxis
Puedes agregar un identificador opcional de idioma para habilitar el resaltado de la sintaxis en tu bloque de código cercado. El resaltado de sintaxis cambia el color y el estilo del código fuente para facilitar la lectura.

## Escritura de expresiones matemáticas
Usa Markdown para mostrar expresiones matemáticas en GitHub. Para habilitar una comunicación clara de las expresiones matemáticas, GitHub admite expresiones matemáticas con formato LaTeX en Markdown. Para obtener más información, consulta LaTeX/Expresiones matemáticas en Wikibooks.

La funcionalidad de representación de expresiones matemáticas de GitHub usa MathJax, un motor de visualización de código abierto basado en JavaScript. MathJax admite una amplia gama de macros de LaTeX y varias extensiones de accesibilidad útiles. Para obtener más información, consulta la documentación de MathJax y la documentación sobre extensiones de accesibilidad de MathJax.

## Escritura de expresiones insertadas
Hay dos opciones para delimitar una expresión matemática insertada con el texto. Puedes rodear la expresión con símbolos de dólar ($) o iniciar la expresión con $` y terminarla con `$. Esta última sintaxis es útil cuando la expresión que escribes contiene caracteres que se superponen con la sintaxis de Markdown.
## Escritura de expresiones como bloques
Para agregar una expresión matemática como un bloque, empieza una línea nueva y delimita la expresión con dos símbolos de dólar ($$).
Tip. Si estás escribiendo en un archivo .md, deberás usar un formato específico para crear un salto de línea, como finalizar la línea con una barra diagonal inversa, tal y como se muestra en el ejemplo siguiente. Para más información sobre el uso de saltos de línea en Markdown, consulta Sintaxis de escritura y formato básicos.

## Adjuntar archivos
Puedes transmitir información si adjuntas varios tipos de archivo a tus propuestas y solicitudes de incorporación de cambios.
Note: En el caso de los repositorios públicos, se puede acceder a los archivos cargados sin autenticación. En el caso de repositorios privados e internos, solo los usuarios con acceso al repositorio pueden ver los archivos cargados.

Para adjuntar un archivo a una propuesta o una conversación de una solicitud de extracción, arrástralo y suéltalo en el cuadro de comentarios. Como alternativa, puedes hacer clic en  en la barra de formato situada encima del cuadro de comentario para examinar, seleccionar y agregar un archivo desde el equipo.
## El tamaño máximo de archivo es:
10 MB para imágenes y gifs
10 MB para videos que se suban a un repositorio que pertenezca a un usuario u organización en un plan gratuito GitHub
100 MB para videos que se suban a un repositorio que pertenezca a un usuario u organización en un plan de pago GitHub
25MB para el resto de los archivos

## Archivos compatibles:
PNG (.png)
GIF (.gif)
JPEG (.jpg, .jpeg)
SVG (.svg)
Archivos de registro (.log)
Archivos Markdown (.md)
Documentos de Microsoft Word (.docx), PowerPoint (.pptx) y Excel (.xlsx)
Archivos de texto (.txt)
Archivos de revisión (.patch)
PDFs (.pdf)
ZIP (.zip, .gz, .tgz)
Vídeo (.mp4, .mov, .webm) La compatibilidad con códecs de vídeo es específica del explorador y es posible que un vídeo que cargues en un explorador no se pueda ver en otro. Por el momento, recomendamos utilizar H.264 para una mejor compatibilidad