#-Faça um programa em Python que recebe uma string que representa uma cadeia de DNA e gera a cadeia complementar.
cadeia = 'ATCG'

cadeia = cadeia.replace('A','t')
cadeia = cadeia.replace('T','a')
cadeia = cadeia.replace('C','g')
cadeia = cadeia.replace('G', 'c')

cadeia = cadeia.upper()

print(cadeia)
