from maquina_snacks_proyecto.snack import Snack
from maquina_snacks_proyecto.servicio_snacks import ServicioSnacks

class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks() # Con este método llamaremos los servicios de la clase ServicioSnacks del archivo servicio_snacks
        self.productos = [] # Se encargará de los productos comprados, para poder generar, por ejemplo, el ticket de venta

    def maquina_snacks(self): # Método que se encargará de generar el menú
        salir = False
        print('*** Maquina de Snacks ***')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e}')

    def mostrar_menu(self):
        print(f'''Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar Nuevo Snack al Inventario
        4. Mostrar Inventario Snacks
        5. Salir''')
        return int(input('Elige una opción: '))


    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto!')
            return True
        else:
            print(f'Opción inválida: {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input("¿Qué snack quieres comprar (id)? "))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack)) # Función next, parecido a un compresor
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Snack no encontrado: {id_snack}')
    
    def mostrar_ticket(self):
        if not self.productos:
            print('No hay productos en el ticket')
            return
        total = sum(snack.precio for snack in self.productos)
        print('--- Ticket  de venta ---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - €{producto.precio:.2f}')
        print(f'\tTotal: €{total:.2f}')
    
    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print(f'Snack agregado: {nuevo_snack}')

# Programa principal
if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()
