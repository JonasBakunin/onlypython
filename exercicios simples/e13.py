#Crie um programa que calcule a média e a mediana de uma lista de números. É
#PERMITIDO O USO DE FUNÇÕES PRONTAS.

from statistics import mean, median

numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = numeros.split(",")

lista_numeros = []
for numero in range(len(numeros)):
    lista_numeros.append(float(numeros[numero]))

media = mean(lista_numeros)
mediana = median(lista_numeros)

print("Média:", media)
print("Mediana:", mediana)
