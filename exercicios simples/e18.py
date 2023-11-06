#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo. Utiliza a biblioteca math, importando apenas
#os itens que serão necessários dessa biblioteca. (Em caso de dúvidas do
#funcionamento das funções utilizadas, pesquise sua documentação no site
#oficial).

from math import sin, cos, tan, radians

angulo = input("Informe o valor do angulo:")

angulo = float(angulo)

anguloR = radians(angulo)

seno = sin(anguloR)
coseno = cos(anguloR)
tangente = tan(anguloR)

print(f"O valor de seno é {seno}, do coseno é {coseno} e da tangente é {tangente}")
