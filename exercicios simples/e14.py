#Crie um programa em Python que leia um arquivo texto com frases e realize a
#contagem de frequências de cada palavra.

with open('frases.txt', 'r') as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.lower().replace(".", "").replace(",", "").split()

frequencias = {}

for palavra in palavras:
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1


for palavra in sorted(frequencias):
    print(palavra + ":", frequencias[palavra])
