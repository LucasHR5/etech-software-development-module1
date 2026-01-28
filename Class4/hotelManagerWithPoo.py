class Cliente:
    def __init__(self, nome: str, idade: int, documento: str, saldo: float, dia_estadia: int):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.saldo = saldo
        self.dia_estadia = dia_estadia
        self.hospedado = False

    def custo_total(self, preco_diaria: float):
        return self.dia_estadia * preco_diaria
    
    def __str__(self):
        status = "Hospedado" if self.hospedado else "Não hospedado"
        return f'Nome: {self.nome}, Documento: {self.documento},  Dias de Estadia: {self.dia_estadia}, Status: {status}'
    
class Hotel:
        def __init__(self):
            self.listaClientes = [
                Cliente("John Doe", 30, "12345678912", 500.0, 3),
            Cliente("Jane Smith", 25, "98765432111", 200.0, 2),
            Cliente("Alice Johnson", 28, "45678912113", 150.0, 5) 
            ]
            self.preco_diaria = 100.0  

        def buscarCliente(self, identificacao: str):
            identificacao =  str(identificacao).strip().lower()
            for cliente in self.listaClientes:
                if cliente.documento.strip().lower() == identificacao:
                    return cliente
            return None

        @staticmethod 
        def validarCpf(documento):
            return len(documento) == 11 and documento.isdigit()

        def criarCliente(self):
            print("=== Cadastro de Cliente ===")
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            documento = input("Digite o documento do cliente: ")

            if self.buscarCliente(documento):
                print("Cliente já cadastrado!")
                return
            
            if not self.validarCpf(documento):
                print("Documento inválido! Deve conter 11 dígitos.")
                return
            
            dias = int(input("Digite o número de dias de estadia: "))
            saldo = float(input("Digite o saldo disponível do cliente: "))

            novoCliente = Cliente(nome, idade, documento, saldo, dias)
            self.listaClientes.append(novoCliente)
            print("Cliente cadastrado com sucesso!")

        def listarClientes(self):
            if len(self.listaClientes) == 0:
                print("Nenhum cliente cadastrado!")
                return

            print("\n=== Lista de Clientes ===")
            for cliente in self.listaClientes:
                print(cliente)
        
        def removerCliente (self):
            documento = input("Digite o documento do cliente a ser removido: ")
            cliente = self.buscarCliente(documento)

            if not cliente:
                print("Cliente não encontrado!")
                return

            self.listaClientes.remove(cliente)
            print("Cliente removido com sucesso!")

        def atualizarCliente(self):
            cliente = self.buscarCliente(input("Digite o documento do cliente a ser atualizado: "))
            if not cliente:
                print("Cliente não encontrado!")
                return
            else:
                if cliente.idade < 18:
                    print("Cliente é menor de idade. Atualização não permitida.")
                    return
                
                custo = cliente.custo_total(self.preco_diaria)
                if cliente.saldo < custo:
                    print("Saldo insuficiente para a estadia.")
                    return
                cliente.hospedado = not cliente.hospedado

                acao = "Check-in" if cliente.hospedado else "Check-out"
                print(f"{acao} realizado com sucesso para {cliente.nome}!")

hotel = Hotel()

while True:
    print(f"\n{'='*10} Sistema de Gerenciamento de Hotel {'='*10}")
    try:
        escolha = int(input("Escolha uma opção:\n1. Cadastrar Cliente | 2. Listar Clientes | 3. Remover Cliente |4.Check-in/Checkout | n0. Sair\n"))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
        continue
    match escolha:
        case 1:
            hotel.criarCliente()
        case 2:
            hotel.listarClientes()
        case 3:
            hotel.removerCliente()
        case 4:
            hotel.atualizarCliente()
        case 0:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida! Tente novamente.")
    
            