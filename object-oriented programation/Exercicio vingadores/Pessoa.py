from abc import ABC

class Pessoa(ABC):

    nome = ""
    ocupacao = ""
    sexo = ""
    peso = 0
    altura = 0

    def get_dados(self):
       print(f"Nome: {self.nome}\n"
             f"Ocupação: {self.ocupacao}\n"
             f"Sexo: {self.sexo}\n"
             f"Peso: {self.peso}\n"
             f"Altura: {self.altura}")
       print(20*"*")
