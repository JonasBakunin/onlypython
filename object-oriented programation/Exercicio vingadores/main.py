from Hulk import *
from ViuvaNegra import *
from GaviaoArqueiro import *
from HomemFerro import *
from Thor import *
from CapitaoAmerica import *

if __name__ == '__main__':

    hulk = Hulk("Bruce Banner", "Cientista", "Masculino", 80, 1.80, 100)
    viuvaNegra = ViuvaNegra("Natasha Romanof", "Agente Secreto", "Feminino", 65, 1.60)
    gaviaoArqueiro = GaviaoArqueiro("Clinton Barton", "Agente Secreto", "Masculino", 80, 1.80)
    thor = Thor("Thor", "Deus do Trovao", "Masculino", 80, 1.80, 3000)
    capitaoAmerica = CapitaoAmerica("Steve Rogers", "Soldado", "Masculino", 80, 1.80, 2500)
    homemFerro = HomemFerro("Tony Stark", "Bilionário", "Masculino", 80, 1.80, 2500)

    vingadores = [hulk, viuvaNegra, gaviaoArqueiro, thor, capitaoAmerica, homemFerro]

    for vingador in vingadores:
        print(vingador.get_dados())

    hulk.ficar_nervoso()
    hulk.get_dados()
    hulk.vai_pescar()

    homemFerro.voar()
    homemFerro.ativar_armadura()
    homemFerro.voar()
    homemFerro.get_dados()
    homemFerro.pousar()
