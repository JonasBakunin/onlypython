#programa que inverte uma string digitada.

# Define a string
my_string = input("Digite uma String: ")

# Converte a string para uma lista de caracteres
string_list = list(my_string)

# Define os índices iniciais e finais para a inversão
start_index = 0
end_index = len(string_list) - 1

# Itera sobre a lista trocando os caracteres correspondentes
while start_index < end_index:
    string_list[start_index], string_list[end_index] = string_list[end_index], string_list[start_index]
    start_index += 1
    end_index -= 1

# Converte a lista de volta para uma string e imprime
inverted_string = "".join(string_list)
print(inverted_string)
