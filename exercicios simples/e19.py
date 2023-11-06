#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
#um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o
#nome do escolhido.

from random import choice

alunos = []

for i in range(4):
    aluno = input("Informe o nome do aluno:")
    alunos.append(aluno)

sorteado = choice(alunos)

print(f"O aluno sorteado foi {sorteado}")
