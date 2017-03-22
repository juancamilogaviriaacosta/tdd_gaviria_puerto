import math


class Calculadora:
    def numeroElementos(self, arreglo):
        if arreglo is None or len(arreglo.strip()) == 0:
            return 0
        else:
            return len(arreglo.split(','))

    def numeroElementosYMinimo(self, arreglo):
        numeroElementos = self.numeroElementos(arreglo)
        if numeroElementos == 0:
            return (0,0)
        else:
            return numeroElementos, int(min(arreglo.strip().split(',')))
