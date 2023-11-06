#Crie um programa que calcule a média e a mediana de uma lista de números.
#NÃO UTILIZE NENHUMA FUNÇÃO PRONTA PARA ISSO.

numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = numeros.split(",")

lista_numeros = []
for numero in range(len(numeros)):
    lista_numeros.append(float(numeros[numero]))

media = sum(lista_numeros) / len(lista_numeros)

numeros_ordenados = sorted(lista_numeros)

if len(lista_numeros) % 2 == 1:
    mediana = numeros_ordenados[len(lista_numeros) // 2]
else:
   mediana = (numeros_ordenados[len(lista_numeros) // 2 - 1] + numeros_ordenados[len(lista_numeros) // 2]) / 2


print("Média:", media)
print("Mediana:", mediana)
