from Pessoa import *

class ViuvaNegra(Pessoa):

    def __init__(self, nome, ocupacao, sexo, peso, altura):
        self.nome = nome
        self.ocupacao = ocupacao
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def rasteira(self):
        print("Viuva Negra está dando uma rasteira")
