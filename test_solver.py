from unittest import TestCase
from Calculadora import Calculadora

class TestSolver(TestCase):
    def test_demo(self):
        c = Calculadora()

        c.calcular(3, 3, 2)

        suma = c.sumar(3, 7)

        self.assertEqual(suma, 10)