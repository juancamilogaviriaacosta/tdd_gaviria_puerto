from unittest import TestCase
from Calculadora import Calculadora

class TestSolver(TestCase):

    def test_demo(self):

        c = Calculadora()

        self.assertEquals(0, c.numeroElementos(None))
        self.assertEquals(0, c.numeroElementos(""))
        self.assertEquals(0, c.numeroElementos(" "))

        self.assertEquals(1, c.numeroElementos("1"))
        self.assertEquals(1, c.numeroElementos("   3 "))