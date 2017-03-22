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

        self.assertEquals(2, c.numeroElementos("1,38"))
        self.assertEquals(2, c.numeroElementos("   3 ,   5   "))

        self.assertEquals(3, c.numeroElementos("1,38,7"))
        self.assertEquals(4, c.numeroElementos("   3 ,   5   , 54  , 22  "))


    def test_demo_2(self):

        c = Calculadora()

        self.assertEquals( (0, 0), c.numeroElementosYMinimo(""))

        self.assertEquals((1, 1), c.numeroElementosYMinimo("1"))
        self.assertEquals((1, 5), c.numeroElementosYMinimo("5   "))

        self.assertEquals((2, 1), c.numeroElementosYMinimo("1,86"))
        self.assertEquals((2, 3), c.numeroElementosYMinimo("5  , 3 "))

        self.assertEquals((4, 2), c.numeroElementosYMinimo("2,86, 978, 4"))
        self.assertEquals((4, 5), c.numeroElementosYMinimo("5  , 43 ,      100,   754"))



    def test_demo_3(self):

        c = Calculadora()

        self.assertEquals((0, 0, 0), c.numeroElementosMinimoYMaximo(""))

        self.assertEquals((1, 1, 1), c.numeroElementosMinimoYMaximo("1"))
        self.assertEquals((1, 5, 5), c.numeroElementosMinimoYMaximo("5   "))