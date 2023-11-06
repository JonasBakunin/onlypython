import Voar
from Pessoa import *
from SuperForca import *
from Voar import *

class HomemFerro(Pessoa, SuperForca, Voar):

    armadura_ativada = False

    def __init__(self, nome, ocupacao, sexo, peso, altura, forca):
        self.nome = nome
        self.ocupacao = ocupacao
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.forca = forca

    def ativar_armadura(self):
        print("Armadura ativada!")
        self.armadura_ativada = True
        self.forca = 3000

    def desativar_armadura(self):
        print("Armadura desativada!")
        self.armadura_ativada = False
        self.forca = 200

    def voar(self):
        if self.armadura_ativada:
            print ("Homem de Ferro " +Voar.voar(self))
        else:
            print("Não é possível voar pois a armadura está desativada.")

    def pousar(self):
        if self.armadura_ativada:
            print ("Homem de Ferro " + Voar.pousar(self))
        else:
            print("Homem de Ferro não está voando pois a armadura está desativada.")

    def get_dados(self):
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)
