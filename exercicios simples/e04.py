#Crie um programa que leia dois valores inteiros do teclado e escreva na tela:
#a. O dobro do primeiro número
#b. A multiplicação entre o primeiro e o segundo número
#c. O resto da divisão entre o primeiro e o segundo número;
#d. A divisão inteira entre o primeiro e o segundo número;
#e. A potência entre o primeiro e o segundo número;
#f. A raiz quadrada do segundo número;

num1 = input("Informe o primeiro número:");
num2 = input("Informe o segundo número:");

num1 = int(num1)
num2 = int(num2)

print(num1*2);
print(num1*num2);
print(num1%num2);
print(num1//num2);
print(num1**num2);
print(num2**0.5);
