class Tarefa:
    def __init__(self, tarefa_id, categoria, descricao, urgencia, dias_restantes):
        self.id = tarefa_id
        self.categoria = categoria
        self.descricao = descricao
        self.urgencia = urgencia
        self.dias_restantes = dias_restantes
        self.status = "Pendente"


class ListaTarefas:
    def __init__(self):
        self.lista = []

    def criar_tarefas(self):
        tarefa_id = len(self.lista) + 1
        categoria = input("Digite a categoria da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        urgencia = input('Urgencia (1 - Baixa, 2 - Média, 3 - Alta): ')
        dias_restantes = int(input("Digite o número de dias restantes para a conclusão da tarefa: "))

        tarefa = Tarefa(
            tarefa_id,
            categoria,
            descricao,
            urgencia,
            dias_restantes
        )

        self.lista.append(tarefa)
        print('Tarefa criada com sucesso!')

    def alterar_status(self):
        if len(self.lista) == 0:
            print('Nenhuma tarefa cadastrada!')
            return

        print('\nID - Categoria - Descrição')
        for tarefa in self.lista:
            print(f'{tarefa.id} - {tarefa.categoria} - {tarefa.descricao}')

        id_tarefa = int(input('\nInforme o ID da tarefa que deseja alterar o status: '))
        for tarefa in self.lista:
            if tarefa.id == id_tarefa:
                novo_status = input('Informe o novo status (1 - Pendente | 2 - Concluída): ')
                if novo_status == '2':
                    self.lista.remove(tarefa)
                    print('Tarefa concluída e removida da lista!')
                else:
                    tarefa.status = novo_status
                    print('Status da tarefa atualizado com sucesso!')
                return

        print('Tarefa não encontrada!')

    def listar_tarefas(self):
        if len(self.lista) == 0:
            print('Nenhuma tarefa cadastrada!')
            return

        print('\nID - Categoria - Descrição - Urgência - Dias Restantes - Status')
        for tarefa in self.lista:
            print(
                tarefa.id, '-',
                tarefa.categoria, '-',
                tarefa.descricao, '-',
                tarefa.urgencia, '-',
                tarefa.dias_restantes, '-',
                tarefa.status
            )


lista_tarefas = ListaTarefas()

while True:
    print('\n 1 - Criar Tarefa')
    print(' 2 - Alterar Status da Tarefa')
    print(' 3 - Listar Tarefas')
    print(' 4 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        lista_tarefas.criar_tarefas()
    elif opcao == 2:
        lista_tarefas.alterar_status()
    elif opcao == 3:
        lista_tarefas.listar_tarefas()
    elif opcao == 4:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')
        input('Pressione Enter para continuar...')
