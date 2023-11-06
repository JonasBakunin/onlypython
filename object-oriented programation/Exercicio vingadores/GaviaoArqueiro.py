from Pessoa import *

class GaviaoArqueiro(Pessoa):

    def __init__(self, nome, ocupacao, sexo, peso, altura):
        self.nome = nome
        self.ocupacao = ocupacao
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def atirar_flecha(self):
        print("Gavião Arqueiro está atirando flechas!")
