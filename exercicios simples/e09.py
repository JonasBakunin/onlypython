#Escreva um programa que solicite ao usuário que entre com as médias de todos
#os alunos da sala e para cada aluno imprime se o mesmo está aprovado (>=5),
#reprovado (< 3) ou recuperação (>=3 e <5). O código deve ser encerrado quando
#o usuário digitar uma média negativa.

while(True):

    media = input("Informe a média:");
    media = float(media);

    if (media < 0):
        break

    if(media >= 5):
        print("Aprovado.");
    elif(media >= 3 ):
        print("Recuperação");
    else:
        print("Reprovado");

