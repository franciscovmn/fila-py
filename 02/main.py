class ClinicaMedica:
    def __init__(self):
        self.fila = []
        self.atendidos = 0

    def incluir_paciente(self, nome, cpf, plano):
        self.fila.append({'nome': nome, 'cpf': cpf, 'plano': plano})
        print(f"Paciente {nome} adicionado. Posição: {len(self.fila)}")

    def realizar_chamada(self):
        if self.fila:
            paciente = self.fila.pop(0)
            self.atendidos += 1
            print(f"Chamando {paciente['nome']}")
        else:
            print("Nenhum paciente na fila.")

    def consultar_posicao(self):
        print(f"Posição atual: {len(self.fila)}")

    def listar_atendidos(self):
        print(f"Pacientes atendidos: {self.atendidos}")
clinica = ClinicaMedica()
while True:
    print("1. Incluir paciente\n2. Realizar chamada\n3. Consultar posição\n4. Listar atendidos\n5. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        plano = input("Plano: ")
        clinica.incluir_paciente(nome, cpf, plano)
    elif opcao == 2:
        clinica.realizar_chamada()
    elif opcao == 3:
        clinica.consultar_posicao()
    elif opcao == 4:
        clinica.listar_atendidos()
    elif opcao == 5:
        break
