# Ejemplo de programación estructurada
# Definimos una lista de diccionarios, donde cada diccionario representa un cliente.
clientes = [{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'},
            {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}]
# Definimos una función llamada 'mostrar_cliente' que toma una lista de clientes y un DNI como argumentos.
# Esta función busca un cliente con el DNI proporcionado y muestra su nombre y apellidos.
def mostrar_cliente(clientes, dni):
    # Iteramos a través de la lista de clientes.
    for c in clientes:
        # Comprobamos si el DNI del cliente actual coincide con el DNI proporcionado.
        if (dni == c['dni']):
            # Si coinciden, mostramos el nombre y los apellidos del cliente.
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            # Salimos de la función después de encontrar y mostrar el cliente.
            return
    # Si no se encuentra ningún cliente con el DNI proporcionado, mostramos un mensaje.
    print('Cliente no encontrado')
# Definimos una función llamada 'borrar_cliente' que toma una lista de clientes y un DNI como argumentos.
# Esta función busca un cliente con el DNI proporcionado y lo elimina de la lista.
def borrar_cliente(clientes, dni):
    # Iteramos a través de la lista de clientes, obteniendo tanto el índice como el cliente.
    for i, c in enumerate(clientes):
        # Comprobamos si el DNI del cliente actual coincide con el DNI proporcionado.
        if (dni == c['dni']):
            # Si coinciden, eliminamos el cliente de la lista usando su índice.
            del (clientes[i])
            # Mostramos un mensaje indicando que el cliente ha sido eliminado.
            print(str(c), "> BORRADO")
            # Salimos de la función después de eliminar el cliente.
            return
    # Si no se encuentra ningún cliente con el DNI proporcionado, mostramos un mensaje.
    print('Cliente no encontrado')

# Imprimimos un encabezado para el listado de clientes.
print("==LISTADO DE CLIENTES==")
# Imprimimos la lista de clientes.
print(clientes)

# Imprimimos un encabezado para la sección de mostrar clientes por DNI.
print("\n==MOSTRAR CLIENTES POR DNI==")
# Llamamos a la función 'mostrar_cliente' para mostrar el cliente con DNI '11111111A'.
mostrar_cliente(clientes, '11111111A')
# Llamamos a la función 'mostrar_cliente' para mostrar el cliente con DNI '11111111Z' (que no existe).
mostrar_cliente(clientes, '11111111Z')

# Imprimimos un encabezado para la sección de borrar clientes por DNI.
print("\n==BORRAR CLIENTES POR DNI==")
# Llamamos a la función 'borrar_cliente' para eliminar el cliente con DNI '22222222V' (que no existe).
borrar_cliente(clientes, '22222222V')
# Llamamos a la función 'borrar_cliente' para eliminar el cliente con DNI '22222222B'.
borrar_cliente(clientes, '22222222B')

# Imprimimos un encabezado para el listado de clientes actualizado.
print("\n==LISTADO DE CLIENTES==")
# Imprimimos la lista de clientes actualizada.
print(clientes)




# Mismo ejemplo con programación orientado a objetos
# Creo una estructura (clase) para los clientes
class Cliente:
    # Constructor de la clase Cliente, se llama al crear un nuevo objeto Cliente.
    def __init__(self, dni, nombre, apellidos):
        # Inicializo los atributos del cliente con los valores proporcionados.
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    # Método para representar el objeto Cliente como una cadena (para imprimir).
    def __str__(self):
        # Formateo la cadena para mostrar el nombre y apellidos del cliente.
        return '{} {}'.format(self.nombre, self.apellidos)

# Creo otra estructura (clase) para las empresas
class Empresa:
    # Constructor de la clase Empresa, inicializa la lista de clientes.
    def __init__(self, clientes=[]):
        # Inicializo la lista de clientes de la empresa con la lista proporcionada.
        self.clientes = clientes

    # Método para mostrar un cliente por DNI.
    def mostrar_cliente(self, dni=None):
        # Itero a través de la lista de clientes de la empresa.
        for c in self.clientes:
            # Compruebo si el DNI del cliente coincide con el DNI proporcionado.
            if c.dni == dni:
                # Si coincide, imprimo la información del cliente y salgo del método.
                print(c)
                return
        # Si no se encuentra el cliente, imprimo un mensaje.
        print("Cliente no encontrado")

    # Método para borrar un cliente por DNI.
    def borrar_cliente(self, dni=None):
        # Itero a través de la lista de clientes, obteniendo el índice y el cliente.
        for i, c in enumerate(self.clientes):
            # Compruebo si el DNI del cliente coincide con el DNI proporcionado.
            if c.dni == dni:
                # Si coincide, elimino el cliente de la lista y muestro un mensaje.
                del (self.clientes[i])
                print(str(c), "> BORRADO")
                return
        # Si no se encuentra el cliente, imprimo un mensaje.
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras
# Creo un par de clientes usando la clase Cliente.
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creo una empresa con los clientes iniciales usando la clase Empresa.
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes de la empresa.
print("==LISTADO DE CLIENTES==")
# Itero sobre cada cliente de la empresa e imprimo su información.
for cliente in empresa.clientes:
    print(cliente)

# Muestro clientes por DNI.
print("\n==MOSTRAR CLIENTES POR DNI==")
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

# Borro un cliente por DNI.
print("\n==BORRAR CLIENTES POR DNI==")
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes de la empresa.
print("\n==LISTADO DE CLIENTES==")
# Itero sobre cada cliente de la empresa e imprimo su información.
for cliente in empresa.clientes:
    print(cliente)