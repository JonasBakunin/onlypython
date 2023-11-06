#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#primitivo e todas as informações possíveis sobre ele.

#Entrada

#Digite Algo: FHO

#Saída

#O tipo primitivo desse valor é: <class 'str'>

#Só tem espaços? False
#É um número? False
#É alfabético? True
#É alfanumérico? True
#Está em maiúsculas? True
#Está em minúsculas? False
#Está capitalizada? False

dado = input("Digite alguma coisa:");

print("O tipo primitivo desse valor é: ", type(dado));
print("Só tem espaços? ", dado.isspace());
print("É um número? ", dado.isnumeric());
print("É alfabético? ", dado.isalpha());
print("É alfanumérico? ", dado.isalnum());
print("Está em maiúscula? ", dado.isupper());
print("Está em minúsculo? ", dado.islower());
print("Está capitalizado? ", dado.istitle());
