

#Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(20 * "-")

#Classe Paciente
class Paciente(Pessoa):
    def __init__(self, nome, idade, email, telefone, historico_medico=None, consultas_agendadas=None):
        super().__init__(nome, idade, email, telefone)
        self.historico_medico = historico_medico or []
        self.consultas_agendadas = consultas_agendadas or []

    def exibir_info(self):
        super().exibir_info()
        print(f"Histórico médico: {self.historico_medico}")
        print(f"Consultas agendadas: {self.consultas_agendadas}")
        print(20 * "-")

#Classe Médico
class Medico(Pessoa):
    def __init__(self, nome, idade, email, telefone, especialidade, numero_registro):
        super().__init__(nome, idade, email, telefone)
        self.especialidade = especialidade
        self.numero_registro = numero_registro

    def exibir_info(self):
        super().exibir_info()
        print(f"Especialidade: {self.especialidade}")
        print(f"Número de registro: {self.numero_registro}")
        print(20 * "-")

#Classe Consulta
class Consulta:
    def __init__(self, data, horario, medico, paciente):
        self.data = data
        self.horario = horario
        self.medico = medico
        self.paciente = paciente

    def exibir_info(self):
        print(f"Data: {self.data}")
        print(f"Horário: {self.horario}")
        print("Médico:")
        self.medico.exibir_info()
        print("Paciente:")
        self.paciente.exibir_info()
        print(20 * "-")


#Classe Hospital
class Hospital:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.consultas = []

    def cadastrar_medico(self, medico):
        self.medicos.append(medico)

    def cadastrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agendar_consulta(self, consulta):
        self.consultas.append(consulta)

    def exibir_medicos(self):
        print("Médicos cadastrados:")
        for medico in self.medicos:
            medico.exibir_info()
        print(20 * "-")

    def exibir_pacientes(self):
        print("Pacientes cadastrados:")
        for paciente in self.pacientes:
            paciente.exibir_info()
        print(20*"-")

    def exibir_consultas(self):
        print("Consultas agendadas:")
        for consulta in self.consultas:
            consulta.exibir_info()
        print(20 * "-")

#Principal
hospital = Hospital()


paciente1 = Paciente("Maria da Silva", 45, "maria.silva@email.com", "(11) 88888-8888",
                     historico_medico=["Cirurgia de apendicite em 2015", "Tratamento de hipertensão arterial"],
                     consultas_agendadas=["15/04/2023 - Clínico geral", "22/04/2023 - Cardiologista"])

medico1 = Medico("Dr. João Silva", 50, "joao.silva.medico@email.com",
                 "(11) 77777-7777", "Cardiologista", "CRM-SP 123456")

hospital.cadastrar_medico(medico1)
hospital.cadastrar_paciente(paciente1)


consulta1 = Consulta("15/04/2023", "14:00", medico1, paciente1)
hospital.agendar_consulta(consulta1)

# Exibir informações do Hospital
hospital.exibir_medicos()
hospital.exibir_pacientes()
hospital.exibir_consultas()
