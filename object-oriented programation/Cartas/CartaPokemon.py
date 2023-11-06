from Carta import *

class CartaPokemon(Carta):
    def __init__(self, valor, naipe, efeito):
        super().__init__(valor, naipe)
        self.efeito = efeito
