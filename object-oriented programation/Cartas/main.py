from Baralho import *
from Jogador import *

if __name__ == '__main__':
    baralho = Baralho()
    baralho.embaralhar()

    jogadores = [Jogador("Jogador 1"), Jogador("Jogador 2"), Jogador("Jogador 3"), Jogador("Jogador 4")]

    for jogador in jogadores:
        jogador.receber_carta(baralho.distribuir(5))

    for jogador in jogadores:
        print(f"{jogador.nome} tem {jogador.verificar_cartas()} cartas:")

        for carta in jogador.cartas:
            print(f"{carta.valor} de {carta.naipe}")
