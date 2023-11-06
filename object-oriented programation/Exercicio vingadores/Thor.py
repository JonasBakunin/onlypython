from Pessoa import *
from SuperForca import *

class Thor(Pessoa, SuperForca):

    def __init__(self, nome, ocupacao, sexo, peso, altura, forca):
        self.nome = nome
        self.ocupacao = ocupacao
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.forca = forca

    def martelada(self):
        print("Thor está dando uma martelada do trovão!")

    def get_dados(self):
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)
