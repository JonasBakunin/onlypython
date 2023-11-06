from abc import ABC

class SuperForca(ABC):

    forca = 0

    def get_dados(self):
        print(f"Força: {self.forca}")
        print(20 * "*")
