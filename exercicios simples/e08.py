#Escreva um programa que lê o tamanho da altura de um retângulo e imprima um
#retângulo daquele tamanho com asteriscos. A largura do retângulo é fixa em 20
#asteriscos. Exemplo:
#Exemplo: Leu 5 de altura
#********************
#********************
#********************
#********************
#********************

altura = input("Informe a altura do retângulo:")
altura = int(altura)

for i in range(altura):
    print(20*"*");
