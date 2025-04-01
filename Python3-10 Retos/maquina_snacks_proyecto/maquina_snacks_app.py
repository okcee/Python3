from maquina_snacks_proyecto.servicio_snacks import ServicioSnacks

class MaquinaSnacks:
    def __init__(self):
        self.servicion_snacks = ServicioSnacks() # Con este método llamaremos los servicios de la clase ServicioSnacks del archivo servicio_snacks
        self.productos = [] # Se encargará de los productos comprados, para poder generar, por ejemplo, el ticket de venta

    def maquina_snacks(self): # Método que se encargará de generar el menú
        salir = False
        print('*** Maquina de Snacks ***')
        self.servicion_snacks.mostrar_snacks()
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
            self.servicion_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto!')
            return True
        else:
            print(f'Opción inválida: {opcion}')
        return False

