from CartaBaralho import *
import random

class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in ["Espadas", "Paus", "Copas", "Ouros"]:
            for valor in range(1, 14):
                carta = CartaBaralho(valor, naipe)
                self.cartas.append(carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, n):
        if len(self.cartas) < n:
            return None

        listacartas = []
        for i in range(n):
            listacartas.append(self.cartas.pop() )
        return listacartas
