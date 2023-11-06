#Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triângulo retângulo, calcule e mostre o comprimento da
#hipotenusa. (Não utilize nenhuma biblioteca para a realização desse código).
#Fórmula do cálculo da hipotenusa:
#hi = √co2 + ca2

co = input("Informe o valor do cateto oposto:")
ca = input("Informe o valor do cateto adjacente: ")

co = float(co)
ca = float(ca)

hi = (co**2 + ca**2)**0.5

print(f"O valor da hipotenusa é {hi}")
