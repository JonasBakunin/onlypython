#Crie um programa em Python que dê as opções para o usuário inserir um nome
#no fim de uma lista, em uma posição definida por ele, remover um item e
#imprimir todos os nomes da lista. Faça um menu com as opções disponíveis que
#permita que o usuário possa escolher as opções enquanto quiser e escolher uma
#opção para finalizar o programa.

lista = []

while(True):
    print(60*"*")
    print("Escolha uma opção:")
    print("1 - Inserir um numero no final da lista")
    print("2 - Inserir um numero em uma posição definida da lista")
    print("3 - Remover um numero da lista")
    print("4 - Imprimir lista")
    print("5 - Sair")
    print(60*"*")
    op = input()
    op = int(op)

    if(op == 1):
        num = input("Informe o numero que deseja inserir:")
        num = float(num)
        lista.append(num)
    elif(op == 2):
        num = input("Informe o numero que deseja inserir:")
        pos = input("Informe a posição que deseja inserir:")
        num = float(num)
        pos = int(pos)
        lista.insert(pos, num)
    elif(op == 3):
        num = input("Informe o numero que deseja remover:")
        num = float(num)
        lista.remove(num)
    elif(op == 4):
        for i in range(len(lista)):
            print(lista[i])
    elif(op == 5):
        break;
    else:
        print("Opção inválida!")
