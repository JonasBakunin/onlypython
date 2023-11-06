#Faça um programa capaz de realizar a leitura do seu nome completo e seu
#curso. Imprima no console os respectivos inputs.
#Entrada 

#Informe seu nome: Maria Joaquina
#Informe seu curso: Pedagogia

#Saída

#Olá, Maria Joaquina, seu curso é Pedagogia

nome = input("Informe seu nome:")
curso = input("Informe seu curso:")

#print("Olá, " + nome + ", seu curso é " + curso);
print(f"Olá, {nome}, seu curso é {curso}");
