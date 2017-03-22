import math


class Calculadora:
    def numeroElementos(self, arreglo):
        if arreglo is None or len(arreglo.strip()) == 0:
            return 0
        else:
            return len(arreglo.split(','))

    def numeroElementosYMinimo(self, arreglo):
        numeroElementos = self.numeroElementos(arreglo)
        arregloSalida = []
        if numeroElementos == 0:
            return (0,0)
        else:
            for i in arreglo.split(','):
                arregloSalida.append(int(i.strip()))

            return numeroElementos, min(arregloSalida)
