from Carta import *

class CartaBaralho(Carta):
    def __init__(self, valor, naipe):
        super().__init__(valor, naipe)
        self.peso = valor
