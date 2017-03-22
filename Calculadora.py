import math


class Calculadora:

    def numeroElementos(self, arreglo):
        if arreglo is None or len(arreglo.strip()) == 0:
            return 0
        else:
            return len(arreglo.strip())