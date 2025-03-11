# 1. Sintaxis de escritura y formato básicos
https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

# Encabezados
# A first-level heading
## A second-level heading
### A third-level heading

# Estilos de texto
Bold	**Texto en negrita** o __Bold text__ Ctrl+B
Cursiva	*Texto en cursiva* o _Italicized text_ Ctrl+I
Tachado	~~Texto tachato~~ o ~~mistaken text~~
Todo en negrita y cursiva	***All this text is important***
Subscript text <sub>subíndice</sub>
Superscript	text <sup>superíndice</sup>
Underlined text <sub>subrayado</sub>

# Entrecomillado de texto
Se puede entrecomillar texto con >
> Text that is a quote
Al texto entre comillas se le aplica sangría con una línea vertical en la izquierda y se muestra mediante texto en color gris.

# Código de cita
Puedes indicar un código o un comando dentro de un enunciado con comillas invertidas. El texto dentro de las comillas invertidas no será formateado.
Use `git status` to list all new or modified files that haven't yet been committed.

Para formatear código o texto en su propio bloque distintivo, usa comillas invertidas triples.
Some basic Git commands are:
```
git status
git add
git commit
```
# Modelos de color compatibles
En los problemas, las solicitudes de incorporación de cambios y los debates, puedes llamar a los colores dentro de una oración mediante comillas invertidas. Un modelo de color compatible dentro de las comillas invertidas mostrará una visualización del color.
The background color is `#ffffff` for light mode and `#000000` for dark mode.
Estos son los modelos de color admitidos actualmente.
Color   Sintaxis    Ejemplo    Resultados
HEX	`#RRGGBB`	`#0969DA`	Captura de pantalla de GitHub Markdown en la que se muestra cómo aparece el valor HEX #0969DA con un círculo azul.
RGB	`rgb(R,G,B)`	`rgb(9, 105, 218)`	Captura de pantalla de GitHub Markdown en la que se muestra cómo aparece el valor RGB 9, 105, 218 con un círculo azul.
HSL	`hsl(H,S,L)`	`hsl(212, 92%, 45%)`	Captura de pantalla de GitHub Markdown en la que se muestra cómo aparece el valor de HSL 212, 92 %, 45 % con un círculo azul.

# Vínculos
Puede crear un vínculo en línea escribiendo su texto entre corchetes [ ] y escribiendo la URL entre paréntesis ( ).
[Sintaxis de escritura y formato básicos](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

# Enlaces de sección
Si necesitas determinar el enlace de un encabezado en un archivo que estás editando, puede usar las siguientes reglas básicas:
Las letras se convierten a minúsculas.
Los espacios se reemplazan por guiones (-). Se quitan cualquier otro espacio en blanco o caracteres de puntuación.
Se quitan los espacios en blanco iniciales y finales.
Se quita el formato de marcado, dejando solo el contenido (por ejemplo, _italics_ se convierte en italics).
Si el ancla generada automáticamente para un encabezado es idéntico a una ancla anterior en el mismo documento, se genera un identificador único anexando un guión y un entero de incremento automático.

# Vínculos relativos
Un enlace relativo es un enlace que es relativo al archivo actual. Por ejemplo, si tiene un archivo Léame en la raíz del repositorio y tiene otro archivo en docs/CONTRIBUTING.md, el vínculo relativo a CONTRIBUTING.md en el archivo Léame podría tener este aspecto:
#[Contribution guidelines for this project](docs/CONTRIBUTING.md)
-- El texto del vínculo debe estar en una sola línea
-- GitHub transformará de manera automática el enlace relativo o la ruta de imagen en cualquier rama en la que te encuentres actualmente, de modo que el enlace o ruta siempre funcione. La ruta de acceso del vínculo será relativa al archivo actual. Los vínculos que comienzan por / serán relativos a la raíz del repositorio. Puede usar todos los operandos de vínculo relativos, como ./ y ../.

# Saltos de línea
En GitHub generará un salto de línea automáticamente, sin embargo, si está escribiendo en un archivo .md para crear un salto de línea en un archivo .md, deberá incluir uno de los elementos siguientes:

Incluya dos espacios al final de la primera línea.
This example  
Will span two lines

Incluya una barra diagonal inversa al final de la primera línea.
This example\
Will span two lines

Incluya una etiqueta de salto de una sola línea HTML al final de la primera línea.
This example<br/>
Will span two lines

Si deja una línea en blanco entre dos líneas, tanto los archivos .md como Markdown en problemas, en solicitudes de ext
This example

Will have a blank line separating both lines

# Imágenes
Puede mostrar una imagen agregando ! y ajustar el texto alternativo en [ ]. El texto alternativo es un texto corto equivalente a la información de la imagen. Luego, escribe el vínculo de la imagen entre paréntesis ().
Se admite el elemento de imagen HTML <picture>.

# Listas
Lista sin ordenar. Para ello, coloca -, * o + antes de una o más líneas de texto.
- George Washington
* John Adams
+ Thomas Jefferson

Lista ordenada, antecede cada línea con un número.
1. James Madison
2. James Monroe
3. John Quincy Adams

# Listas anidadas
Puedes crear una lista anidada al dejar sangría en uno o más elementos de la lista debajo de otro elemento.
En un editor de texto como Visual Studio Code, puedes alinear la lista visualmente.

# Listas de tareas
Para crear una lista de tareas, debe añadir como prefijo un guion y espacio, seguido de [ ] a los elementos de la lista. Para marcar una tarea como completada, use [x]. Si la descripción de un elemento de la lista de tareas comienza por un paréntesis, necesitará agregar el carácter de escape \

# Mencionar personas y equipos
Puedes mencionar a una persona o equipo en GitHub si escribes @ junto con su nombre de usuario o equipo

# Cargar activos
Puedes cargar activos como imágenes si las arrastras y sueltas, las seleccionas de un buscador de archivos o si las pegas. Puede cargar recursos en las incidencias, solicitudes de incorporación de cambios, comentarios y archivos .md en el repositorio.

# Usar emojis
Puedes agregar emoji a la escritura escribiendo :EMOJICODE:, dos puntos seguidos del nombre del emoji.
[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#emoji-cheat-sheet)

# Notas al pie
Puedes agregar notas al pie para tu contenido si utilizas esta sintaxis de corchetes:
Here is a simple footnote[^1].
A footnote can also have multiple lines[^2].
[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces. 
This is a second line.

# Alertas
Las alertas son una extensión Markdown basada en la sintaxis blockquote que puede utilizar para resaltar la información crítica. En GitHub, se muestran con colores e iconos distintivos para indicar la importancia del contenido.Deben usarse las alertas solo cuando sean cruciales para el éxito del usuario y limitarlas a una o dos por artículo para evitar sobrecargar al lector
> [!NOTE]
> Useful information that users should know, even when skimming content.  
> [!TIP]
> Helpful advice for doing things better or more easily.  
> [!IMPORTANT]
> Key information users need to know to achieve their goal.  
> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.  
> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.  

# Ocultar el contenido con comentarios
Puedes indicarle a GitHub que oculte el contenido del Markdown representado si colocas el contenido en un comentario HTML.
<!-- This content will not appear in the rendered Markdown -->

# Ignorar formato de Markdown
Agregar el carácter de escape \
Puedes indicarle a GitHub que ignore (u omita) el formato de Markdown si usas \ antes del carácter de Markdown.
Let's rename \*our-new-project\* to \*our-old-project\*.