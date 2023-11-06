#Crie um programa em Python semelhante ao exercício e20.py , para que o usuário crie
#uma lista telefônica (Nome e Telefone). Permita também que o usuário
#verifique se o telefone está na lista. Utilize dicionários.


agenda = {}

while(True):
    print(60*"*")
    print("Escolha uma opção:")
    print("1 - Inserir um contato na agenda")
    print("2 - Consultar um contato")
    print("3 - Remover um contato")
    print("4 - Imprimir agenda")
    print("5 - Sair")
    print(60*"*")
    op = input()
    op = int(op)

    if(op == 1):
        nome = input("Informe o nome que deseja inserir:")
        tel = input("Informe o telefone:")
        agenda[nome] = tel
    elif(op == 2):
        nome = input("Informe o nome que deseja consultar:")
        print(f"Nome: {nome} - Telefone: {agenda[nome]}")
    elif(op == 3):
        nome = input("Informe o nome que deseja remover:")
        del agenda[nome]
    elif(op == 4):
        for n, t in agenda.items():
            print(f"Nome: {n} - Tel:{t}")
    elif(op == 5):
        break
    else:
        print("Opção invalida!")
