class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

    def receber_carta(self, listacarta):
        for i in range(len(listacarta)):
            self.cartas.append(listacarta[i])

    def jogar_carta(self, indice):
        return self.cartas.pop(indice)

    def verificar_cartas(self):
        return len(self.cartas)
