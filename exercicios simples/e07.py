#A cidade A possui 90.000 habitantes e a cidade B 50.000. A população da
#cidade A cresce 0,9 % ao ano enquanto que a da cidade B cresce 1,5% ao ano.
#Faça um programa que leia o número de anos e calcule qual será o número da
#população de cada cidade. O programa deve verificar se o tamanho da cidade A
#é maior que a cidade B, ou se o tamanho da cidade B é maior que a cidade A.

anos = input("Informe a quantidade de anos:");
anos = int(anos);

cidadeA = 90000;
cidadeB = 50000;

for i in range(anos):
    #cidadeA = cidadeA + cidadeA*0.9;
    #cidadeB = cidadeB + cidadeB*1.5;
    cidadeA += cidadeA*0.9;
    cidadeB += cidadeB*1.5;

if(cidadeA > cidadeB):
    print(f"Após {anos} anos, a cidade A será maior que a cidade B");
else:
    print(f"Após {anos} anos, a cidade B será maior que a cidade A");
