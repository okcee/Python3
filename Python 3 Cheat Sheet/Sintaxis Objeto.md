# Sintaxis Completa de un Objeto en Python

```Python
# Creación de un objeto (instanciación de la clase)
mi_objeto = NombreDeLaClase(valor_parametro1, valor_parametro2, ...)

# Acceso a los atributos de instancia
print(mi_objeto.atributo1)
mi_objeto.atributo2 = nuevo_valor

# Llamada a los métodos de instancia
resultado = mi_objeto.metodo1(otro_valor)
print(resultado)
mi_objeto.metodo2()

# Acceso a los atributos de clase (a través del objeto o de la clase)
print(mi_objeto.variable_de_clase)
print(NombreDeLaClase.variable_de_clase)

# Llamada a los métodos de clase (generalmente se llama a través de la clase)
resultado_clase = NombreDeLaClase.metodo_de_clase(argumento_clase)
print(resultado_clase)

# Llamada a los métodos estáticos (generalmente se llama a través de la clase)
resultado_estatico = NombreDeLaClase.metodo_estatico(parametro_estatico)
print(resultado_estatico)

# Uso de la representación del objeto (método __str__)
print(mi_objeto)

# Uso de la representación "oficial" del objeto (método __repr__)
print(repr(mi_objeto))
```