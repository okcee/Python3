import unittest
from archivo_a_testear import sumar, restar

class TestFunciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(3, 5), -2)

if __name__ == '__main__':
    unittest.main()