#Crie um programa que solicite ao usuário uma frase e, em seguida, informe a
#quantidade de ocorrências de cada letra na frase.

def conta_letras(texto):
    letras = {}
    for letra in texto:
        if letra == " ":
            continue
        letras[letra] = letras.get(letra, 0) + 1

    return letras


texto = input("Digite uma frase: ")
qtd_letras = conta_letras(texto.lower())
for letra, qtd in qtd_letras.items():
    print(letra, ":", qtd)
