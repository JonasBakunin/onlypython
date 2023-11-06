Exercicio sobre orientação a objetos com todas as classes e métodos em um arquivo só.
Crie um programa para gerenciamento de pessoas com os seguintes requisitos:

• Crie uma classe base “Pessoa”, com atributos como “nome”, “idade”, “e-
mail” e “telefone”.

• Crie uma classe “Paciente”, que herda da classe “Pessoa” e acrescenta
atributos como “histórico médico” e “consultas agendadas”.
• Crie uma classe “Médico”, que também herda da classe “Pessoa” e
acrescenta atributos como “especialidade” e “número de registro no
conselho de medicina”.
• Represente a relação de agendamento de consultas, utilizando composição,
ou seja, crie uma classe “Consulta” que possui atributos como “data”,
“horário”, “médico” e “paciente”.
• Crie uma classe “Hospital”, que representa o sistema de gerenciamento
#como um todo, agregando médicos, pacientes e consultas.
