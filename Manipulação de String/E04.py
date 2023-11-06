# Crie um arquivo chamado “notas.txt” que contenha os nomes de alunos, e 6
# notas (Ma1, Mb1, P1, Ma2, Mb2 e P2), com todos os dados separados por ‘,’
# vírgula). Posteriormente,
# Escreva um programa em Python que faça a leitura desse arquivo e exiba na tela
# o nome do aluno e a média final, calculada a partir da fórmula a seguir:

# Nota final = (A1 + (2 x A2) ) / 3

# em que,
# A1 = 70% por uma prova individual (P1), 10% por avaliação continuada (Ma1)
# e 20% Atividade em grupo (Mb1).

# A2 = 70% por uma prova individual (P2), 10% por avaliação continuada (Ma2)
# e 20% Atividade em grupo (Mb2).

def calculaA1_A2(prova_individual, avaliacao_continuada, atividade_grupo):
    nota = (prova_individual * 0.7) + (avaliacao_continuada * 0.1) + (atividade_grupo * 0.2)
    return nota

def calculaMedia(A1, A2):
    media = (A1 + 2*A2)/3
    return media


f = open('notas.txt', 'r') # abre o arquivo


for linha in f: # percorrendo todas as linhas do arquivo
    linha = linha.replace('\n', '')
    linha = linha.split(',')

    nome = linha[0]
    p1 = float(linha[1])
    ma1 = float(linha[2])
    mb1 = float(linha[3])
    p2 = float(linha[4])
    ma2 = float(linha[5])
    mb2 = float(linha[6])

    A1 = calculaA1_A2(p1, ma1, mb1)
    A2 = calculaA1_A2(p2, ma2, mb2)

    media = calculaMedia(A1, A2)

    print(f'Nome = {nome} - Media Final = {media:.1f}')

f.close()
