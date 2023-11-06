#Crie um programa para gerenciamento de notas de alunos com os seguintes
#requisitos:

#• Crie um dicionário que associe o nome do aluno às suas respectivas
#notas em uma determinada disciplina.
#• Permita que o usuário adicione, remova ou atualize notas dos alunos,
#além de exibir a média da turma e as informações dos alunos.

notas_alunos = {}


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    notas = input("Digite as notas do aluno separadas por vírgulas: ")
    notas = notas.split(",")
    lista_notas = []
    
    for nota in range(len(notas)):
        lista_notas.append(float(notas[nota]))

    notas_alunos[nome] = lista_notas
    print("Notas do aluno", nome, "adicionadas/atualizadas com sucesso!")


def remover_aluno():
    nome = input("Digite o nome do aluno que deseja remover: ")
    if nome in notas_alunos:
        del notas_alunos[nome]
        print("Notas do aluno", nome, "removidas com sucesso!")
    else:
        print("Aluno", nome, "não encontrado.")

def exibir_aluno():
    nome = input("Digite o nome do aluno que deseja exibir as informações: ")
    if nome in notas_alunos:
        notas = notas_alunos[nome]
        media = sum(notas) / len(notas)
        print("Nome:", nome)
        print("Notas:", notas)
        print("Média:", media)
    else:
        print("Aluno", nome, "não encontrado.")

def exibir_media():
    notas = []
    for aluno, notas_aluno in notas_alunos.items():
        notas.extend(notas_aluno)
    media = sum(notas) / len(notas)
    print("Média da turma:", media)


while True:
    print()
    print("Menu:")
    print("1 - Adicionar/Atualizar notas de um aluno")
    print("2 - Remover notas de um aluno")
    print("3 - Exibir informações de um aluno")
    print("4 - Exibir média da turma")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        remover_aluno()
    elif opcao == "3":
        exibir_aluno()
    elif opcao == "4":
        exibir_media()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
