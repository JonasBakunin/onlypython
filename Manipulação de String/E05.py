#Faça uma nova versão do exercício 4 que permita que o usuário escolha a
#opção de escrever os nomes e notas de alunos no arquivo “notas.txt” (esse
#arquivo possui a mesma estrutura do arquivo do exercício 4). O usuário também
#deve ter a opção de realizar os cálculos das médias conforme regras do exercício 4.

def calculaA1_A2(prova_individual, avaliacao_continuada, atividade_grupo):
    nota = (prova_individual * 0.7) + (avaliacao_continuada * 0.1) + (atividade_grupo * 0.2)
    return nota

def calculaMedia(A1, A2):
    media = (A1 + 2*A2)/3
    return media


while True:

    while True:
        try:
            print('-'*30)
            print('1 - Inserir dados no arquivo ')
            print('2 - Calcular Medias ')
            print('3 - Sair ')
            print('-'*30)
            op = int(input('Informe a opcao desejada: '))
            break
        except ValueError:
            print('Favor informar um número.')


    if op == 1:

        try:
            f = open('notas.txt', 'a')
        except IOError:
            print('Erro com o arquivo.')
            break

        nome = input('Informe o nome do aluno: ')
        p1 = input('Informe a nota P1: ')
        ma1 = input('Informe a nota Ma1: ')
        mb1 = input('Informe a nota Mb1: ')
        p2 = input('Informe a nota P2: ')
        ma2 = input('Informe a nota Ma2: ')
        mb2 = input('Informe a nota Mb2: ')

        f.write(f'\n{nome},{p1},{ma1},{mb1},{p2},{ma2},{mb2}')
        f.close()



    elif op == 2:
        try:
            f = open('notas.txt', 'r')  # abre o arquivo
        except IOError:
            print('Erro com o arquivo.')
            break

        for linha in f:  # percorrendo todas as linhas do arquivo
            linha = linha.replace('\n', '')
            linha = linha.split(',')

            nome = linha[0]
            try:
                p1 = float(linha[1])
                ma1 = float(linha[2])
                mb1 = float(linha[3])
                p2 = float(linha[4])
                ma2 = float(linha[5])
                mb2 = float(linha[6])

                A1 = calculaA1_A2(p1, ma1, mb1)
                A2 = calculaA1_A2(p2, ma2, mb2)

                media = calculaMedia(A1, A2)

                print(f'Nome = {nome} - Media Final = {media}')
            except ValueError:
                print('Erro na leitura das notas do arquivo.')

        f.close()
    else:
        break
