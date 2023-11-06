from Pessoa import *
from SuperForca import *

class Hulk(Pessoa, SuperForca):

    def __init__(self, nome, ocupacao, sexo, peso, altura, forca):
        self.nome = nome
        self.ocupacao = ocupacao
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.forca = forca

    def get_dados(self):
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)

    def ficar_nervoso(self):
        print("HUUULLLLLKKKK ESMMAAAAGGAAA!")
        self.forca = 5000

    def vai_pescar(self):
        print("Hulk calmo!")
        self.forca = 100
