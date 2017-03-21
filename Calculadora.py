import math


class Calculadora:

    def calcular(self, a, b, c):

        if c != 0:
            print(a, b, c)
        else:
            raise Exception

    def sumar(self, a, b):
        return a + b
