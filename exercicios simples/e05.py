#Suponha que você desenvolverá um sistema para gerenciar suas notas. Seu
#programa deve conter variáveis para guardar RA, notas N1 e N2, e média. Deve
#ser capaz de realizar a leitura desses valores via teclado e, após isso, você deve
#fazer as conversões necessárias dos tipos de dados. Imprima os valores finais no
#console.

ra = input("Informe o RA:");
N1 = input("Informe a N1:");
N2 = input("Informe a N2:");
media = input("Informe a média:");

N1 = float(N1);
N2 = float(N2);
media = float(media);

print(ra, N1, N2, media);
