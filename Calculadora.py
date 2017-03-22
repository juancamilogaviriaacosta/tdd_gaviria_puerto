import math


class Calculadora:
    def numeroElementos(self, arreglo):
        if arreglo is None or len(arreglo.strip()) == 0:
            return 0
        else:
            return len(arreglo.split(','))

    def numeroElementosYMinimo(self, arreglo):
        if arreglo is None or len(arreglo.strip()) == 0:
            return (0, 0)
        else:
            return len(arreglo.strip().split(',')), int(min(arreglo.strip().split(',')))
