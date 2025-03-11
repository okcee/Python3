# python -m unittest test_mi_unittest.py
''' Entonces, debemos nombrar nuestros archivos de prueba con la palabra clave test en el arranque. Importamos unittest y math'''
import mi_unittest
''' Y en nuestro caso tendremos que importar también math, para contar con PI: '''
import math
# Importa la función area desde el archivo mi_codigo.py
from mi_codigo import area
''' Lo siguiente será crear una clase que herede de la clase TestCase. En esta clase es donde vamos a poner nuestros test. '''
class TestArea(mi_unittest.TestCase):
    # crear un método cuyo nombre debe empezar por la palabra test.
    def test_area(self):
        print('-----Test valores de resultado conocido-----')
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(3), math.pi * 9)
        self.assertAlmostEqual(area(-1), math.pi)
        self.assertAlmostEqual(area(-3), math.pi * 9)
        self.assertAlmostEqual(area(2+3j), math.pi * ((2+3j)**2))
        self.assertAlmostEqual(area(True), math.pi)
    def test_area_type(self):
        self.assertRaises(TypeError, area, "string")
if __name__ == '__main__':
    mi_unittest.main()