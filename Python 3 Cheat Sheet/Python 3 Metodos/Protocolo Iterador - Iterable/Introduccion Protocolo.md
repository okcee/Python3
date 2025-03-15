# Protocolo de Iterador e Iterable en Python

Python proporciona mecanismos más "de bajo nivel" para la iteración a través de los protocolos de **iterador** e **iterable**, que se implementan mediante los métodos especiales `__iter__` y `__next__`. Estos métodos son la base sobre la cual funcionan los bucles `for` y otras construcciones de iteración en Python.

---

## Protocolo de Iterador e Iterable

Para que un objeto pueda ser iterado (es decir, que puedas recorrer sus elementos con un bucle `for`), debe seguir el **protocolo de iterable**. Un objeto es **iterable** si define el método `__iter__()`, que debe devolver un objeto iterador.

Un **objeto iterador** es un objeto que implementa el **protocolo de iterador**, que requiere la definición de dos métodos:

- **`__iter__()`**: Este método debe devolver el propio objeto iterador (es decir, `self`). Se utiliza para inicializar la iteración.
- **`__next__()`**: Este método debe devolver el siguiente elemento de la secuencia. Si no hay más elementos, debe elevar la excepción `StopIteration`.

---

## Cómo funcionan juntos

Cuando usas un bucle `for` sobre un objeto iterable, Python hace lo siguiente "por debajo":

1. Llama al método `__iter__()` del objeto iterable para obtener un objeto iterador.
2. Llama repetidamente al método `__next__()` del objeto iterador para obtener cada elemento de la secuencia en cada iteración del bucle.
3. El bucle `for` se detiene automáticamente cuando se eleva la excepción `StopIteration`.

---

## Ejemplo Implementando un Iterador Personalizado

Vamos a crear una clase que actúe como un iterador y genere una secuencia de números pares hasta un límite:

```python
class ParesHasta(object):
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __iter__(self):
        return self  # Devuelve el propio objeto como iterador

    def __next__(self):
        if self.actual > self.limite:
            raise StopIteration
        else:
            valor_actual = self.actual
            self.actual += 2
            return valor_actual

# Usando nuestro iterador personalizado
pares = ParesHasta(10)
for numero in pares:
    print(numero)
```

En este ejemplo:

- `ParesHasta` es un **iterable** porque implementa `__iter__()`.
- El objeto `ParesHasta` también es su propio **iterador** porque su método `__iter__()` devuelve `self`, y además implementa `__next__()`.

---

## Ejemplo Separando el Iterable del Iterador

A veces, el objeto **iterable** y el objeto **iterador** son clases separadas. Por ejemplo, una lista es **iterable**, pero el objeto que obtienes al llamar a `iter(mi_lista)` (o implícitamente al usar un bucle `for`) es el **iterador** que mantiene el estado de la iteración.

```python
mi_lista = [1, 2, 3]
iterador_lista = iter(mi_lista)

print(next(iterador_lista))  # Output: 1
print(next(iterador_lista))  # Output: 2
print(next(iterador_lista))  # Output: 3
# print(next(iterador_lista))  # Generaría StopIteration
```

Aquí, la lista `mi_lista` tiene un método `__iter__` que devuelve un objeto **iterador** diferente, el cual tiene el método `__next__`.

---

## ¿Cuándo usar `__iter__` y `__next__` directamente?

Normalmente, no necesitas implementar `__iter__` y `__next__` directamente en tu código diario. Los bucles `for`, las comprensiones y los generadores abstraen esta complejidad y hacen la iteración más sencilla y legible.

Sin embargo, implementar estos métodos es útil cuando:

- Quieres crear tus propias estructuras de datos que puedan ser iteradas.
- Necesitas un control muy específico sobre cómo se realiza la iteración.
- Estás construyendo iteradores personalizados que generan secuencias basadas en lógica compleja o fuentes de datos externas.

---

## En resumen:

| Método         | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `__iter__()`   | Define cómo obtener el objeto iterador de un iterable.                      |
| `__next__()`   | Define cómo obtener el siguiente elemento del iterador y cuándo detenerlo (`StopIteration`). |

Estos métodos son la base del **protocolo de iteración** en Python.

Aunque no los uses directamente en la mayoría de los casos, entenderlos te da una comprensión más profunda de cómo funciona la iteración en Python.
```