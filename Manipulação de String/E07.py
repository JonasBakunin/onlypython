#Crie um programa que verifica se uma palavra ou frase é um palíndromo.

ef eh_palindromo(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]


text = input("Digite uma palavra ou frase: ")
if eh_palindromo(text):
    print(text, "é um palíndromo!")
else:
    print(text, "não é um palíndromo.")
