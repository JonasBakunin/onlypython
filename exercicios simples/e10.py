#Escreva um programa em Python que tenha uma função que
#receba como parâmetro uma lista de números inteiros e um valor inteiro. Essa
#função deve retornar uma nova lista, na qual seu conteúdo é o valor original da
#lista multiplicado pelo valor inteiro passado por parâmetro.

def multiplica_lista(lista, num):
  nova_lista = []
  for i in range(len(lista)):
        nova_lista.append(lista[i]*num)
  return nova_lista
lista = [3, 5, 10]
nova = multiplica_lista(lista, 3)
print(lista)
print(nova)
