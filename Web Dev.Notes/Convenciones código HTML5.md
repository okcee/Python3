## Seguir las convenciones de estilo de código

La **bicapitalización** es un método para dar nombre a determinados tipos de objetos. La bicapitalización de un nombre combina varias palabras sin espacios y convierte la primera palabra en minúsculas y pone en mayúscula la primera letra de las palabras siguientes. Los desarrolladores pueden utilizar la bicapitalización para dar nombre a todos sus estilos. ("tablaInformeAnual")  

La **notación con puntos** es más una convención que un estilo, pero algunos equipos separarán las palabras en un determinado tipo de objetos de código mediante un punto. ("informes.Anuales.Generar")  

El **estilo kabab** utiliza letras minúsculas para cada palabra y guiones entre palabras. Este estilo es una norma para dar nombre a los estilos de una hoja de estilo. ("mi-nuevo-estilo")  

## Aplicar elementos semánticos a las secciones

Los elementos semánticos han formado parte de la especificación HTML desde que se desarrolló HTML por primera vez.  
Son elementos autodescriptivos que los desarrolladores utilizan para organizar las secciones de un documento.  

<section> y <article> dividen las secciones lógicas o categóricas de información.
Ej: Acerca de nosotros de un blog o artículo.  

<time> define el contenido de tiempo. Este elemento ayuda a identificar contenido como el horario de apertura y cierre de una empresa.  

<nav> es útil para asignar una sección de elementos de navegación. Por ejemplo, los desarrolladores web pueden utilizarlo para poner una lista de hiperenlaces en una sección de referencia en la parte inferior de una página web.  

## Crear la sección de cabecera correctamente
La sección de cabecera de su página HTML principal es donde colocará información y referencias que todo el sitio web utilizará, se suele denominar `index.html` o `default.html`.  

Los elementos de la sección de cabecera se cargan primero. La sección de cabecera debe incluir cualquier recurso que necesite para el resto del sitio. Por ejemplo:  
- Los metadatos son información sobre un sitio web. Los metadatos también ayudan con la indexación de los motores de búsqueda y permiten a los usuarios encontrar su contenido cuando realizan una búsqueda en la web.  
- Un script es código de software que los desarrolladores web utilizan para crear interactividad, gestionar los datos y diseñar una página web. Cuanto más complejo sea el sitio web, más necesitará depender de scripts para hacer cosas interesantes y dinámicas.  
- Las fuentes determinan la tipografía de un sitio web. Las fuentes se pueden establecer en elementos individuales o de forma genérica para todos los elementos de texto de un sitio.  
- Hojas de estilo
Es una buena práctica colocar las referencias a hojas de estilo en la cabecera del sitio. Esto garantiza que todos los estilos que necesita para el sitio web estarán disponibles para los elementos que los necesitan.  

## Uso de las distintas listas

Tanto las listas ordenadas como las listas sin ordenar implementan el elemento <li></li> para añadir elementos a sus listas.  

HTML admite tres tipos de listas:  

- Las listas desordenadas, que podría considerar como listas con viñetas, que se indican mediante el elemento <ul></ul>. Puede cambiar el estilo de las viñetas redondas a otro tipo de viñetas, como cuadrado o diamante, mediante una hoja de estilo o un estilo en línea.  

```html
<ul>
<li>Elemento 1</li>
<li>Elemento 2</li>
<li>Elemento 3</li>
</ul>
```

- Las listas ordenadas, como su nombre indica, están numeradas o con letras. Se crean mediante el elemento `<ol></ol>`.  

```html
<ol>
<li>Elemento 1</li>
<li>Elemento 2</li>
<li>Elemento 3</li>
</ol>
```

- Las listas de descripciones listan términos. Cada elemento de lista incluye una descripción de su término. Se crean mediante el elemento `<dl></dl>`.  

```html
<dl>
<dt>Elemento 1</dt>
	<dd>Descripción 1</dd>
    <dt>Elemento 2</dt>
            <dd>Descripción 2</dd>
    <dt>Elemento 3</dt>
            <dd>Descripción 3</dd>
</dl>
```
