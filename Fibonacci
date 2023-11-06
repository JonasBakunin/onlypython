#programa em que o usuário digita um número e o programa diz se esse numero pertence à sequência fibonacci ou não.

def fibonacci(n):
# Função que retorna o n-ésimo número da sequência de Fibonacci.

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Pedindo o número ao usuário
numero = int(input("Informe um número: "))

# Verificando se o número pertence à sequência de Fibonacci
pertence = False
for i in range(numero+1):
    if fibonacci(i) == numero:
        pertence = True
        break

# Imprimindo a mensagem de resultado
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
