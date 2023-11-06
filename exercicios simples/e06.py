#Uma livraria está fazendo uma promoção para pagamento à vista em que o
#comprador pode escolher entre dois critérios de desconto:
#Critério A: R$ 0,25 por livro + R$ 7,50
#Critério B: R$ 0,50 por livro + R$ 2,50

#Faça um programa em que o usuário digita a quantidade de livros que deseja
#comprar e o programa calcula qual seria o valor do pagamento em ambos
#critérios.
#O programa deve afirma quais dos critérios é maior vantajoso.

livros = input("Informe a quantidade de livros:")

livros = int(livros)

criterioA = 0.25 * livros + 7.50;
criterioB = 0.5 * livros + 2.50;

if(criterioA < criterioB):
    print("O critério A é mais vantajoso.")
else:
    print("O critério B é mais vantajoso.");
