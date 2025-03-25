# Resumen del Proceso de Prueba de una Página Web

**Paso 1. Definir el entorno de pruebas**

* Crear una versión separada del sitio web (réplica del sitio activo).
* Accesible solo a desarrolladores y testers de control de calidad.
* Permite probar y depurar sin afectar el sitio web en producción ni a los usuarios.
* Herramienta crucial para asegurar el correcto funcionamiento antes del lanzamiento.

**Paso 2. Desarrollar casos de prueba**

* Serie de pasos para verificar el correcto funcionamiento del sitio web.
* Objetivo: identificar problemas o errores en áreas o funciones específicas.
* Implica verificar características y funciones para asegurar el funcionamiento esperado y una experiencia de usuario positiva.
* Ejemplos:
    * Comprobar la distribución y el diseño.
    * Verificar el funcionamiento de todos los enlaces.
    * Probar la funcionalidad de búsqueda.
    * (y mucho más).

**Paso 3. Escribir y ejecutar scripts**

* Un script de automatización es código de software que ejecuta herramientas de software.
* Consta de instrucciones para automatizar las pruebas del sitio web.
* Puede incluir tareas como:
    * Comprobar la funcionalidad de la aplicación.
    * Verificar el correcto funcionamiento.
    * Identificar errores o defectos.
* Se suelen escribir en lenguajes de programación y se ejecutan con herramientas especializadas (ej. IBM UrbanCode) o de código abierto (ej. Jenkins).

**Paso 4. Analizar los resultados de las pruebas**

* Después de ejecutar scripts automatizados y pruebas manuales, se analizan los resultados.
* El análisis puede incluir:
    * Revisar casos de prueba y resultados esperados.
    * Comparar resultados esperados con resultados reales encontrados.
    * Identificar discrepancias.
* Se pueden usar herramientas y software especializados para analizar y resaltar áreas que requieren más atención (ej. hojas de cálculo mostrando áreas problemáticas).

**Paso 5. Enviar informes de error**

* Al encontrar un error o problema, se crea un informe de error para documentarlo y detallar cómo reproducirlo.
* Un informe de error suele incluir:
    * Pasos para reproducir el problema.
    * Comportamiento esperado del sitio web.
    * Comportamiento real observado.
    * Posiblemente capturas de pantalla o vídeos.
* Se envía al equipo o persona adecuada (ej. director de proyecto, desarrollador sénior) para su revisión y resolución.

