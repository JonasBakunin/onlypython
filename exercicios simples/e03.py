#Crie uma agenda eletrônica capaz de realizar a leitura dos dados de uma
#pessoa física (Nome completo, RG, CPF, celular, e-mail). Para cada dado, exiba
#uma frase autoexplicativa no console. Após realizar a leitura dos dados, imprima
#todos no console, logo após, peça ao usuário que confirme a ação, digitando
#SIM ou NÃO.


while(True):
    nome = input("Informe o nome completo:");
    rg = input("Informe o RG:");
    cpf = input("Informe o CPF:");
    celular = input("Informe o celular: ");
    email = input("Informe o email:");

    print(f"Nome: {nome} / RG: {rg} / CPF: {cpf} / Celular: {celular} / Email: {email}");

    confirma = input("Confirma a ação? SIM ou NAO:");

    if confirma == "SIM":
        break;
