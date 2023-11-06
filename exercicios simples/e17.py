#Refaça o exercício e15.py utilizando a biblioteca math. Importe somente os itens
#necessários dessa biblioteca.

from math import hypot

co = input("Informe o valor do cateto oposto:")
ca = input("Informe o valor do cateto adjacente: ")

co = float(co)
ca = float(ca)

hi = hypot(co, ca)

print(f"O valor da hipotenusa é {hi}")
