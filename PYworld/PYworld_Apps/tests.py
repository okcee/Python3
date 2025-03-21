from django.test import TestCase
from django.urls import reverse
from .models import Producto

class ProductoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configuración de datos de prueba para toda la clase.
        # Esto se ejecuta una vez al inicio de la clase de prueba.
        Producto.objects.create(nombre='Producto de prueba', descripcion='Descripción de prueba', precio=10.00)

    def test_producto_nombre(self):
        # Prueba el campo 'nombre' del modelo Producto.
        producto = Producto.objects.get(id=1)  # Obtiene el producto de prueba.
        field_label = producto._meta.get_field('nombre').verbose_name  # Obtiene el nombre legible del campo.
        self.assertEqual(field_label, 'nombre')  # Verifica que el nombre legible sea 'nombre'.
        self.assertEqual(producto.nombre, 'Producto de prueba')  # Verifica que el valor del campo sea correcto.

    def test_producto_precio(self):
        # Prueba el campo 'precio' del modelo Producto.
        producto = Producto.objects.get(id=1)  # Obtiene el producto de prueba.
        self.assertEqual(producto.precio, 10.00)  # Verifica que el valor del campo sea correcto.

class ListaProductosViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configuración de datos de prueba para toda la clase.
        # Crea algunos productos de prueba.
        Producto.objects.create(nombre='Producto 1', descripcion='Descripción 1', precio=20.00)
        Producto.objects.create(nombre='Producto 2', descripcion='Descripción 2', precio=30.00)

    def test_lista_productos_view(self):
        # Prueba la vista 'lista_productos'.
        response = self.client.get(reverse('lista_productos'))  # Obtiene la respuesta de la vista.
        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea exitosa (código 200).
        self.assertContains(response, 'Producto 1')  # Verifica que la respuesta contenga 'Producto 1'.
        self.assertContains(response, 'Producto 2')  # Verifica que la respuesta contenga 'Producto 2'.