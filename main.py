class Aplicativo:
    """Clase principal. Cria, Gerencia e Exibe as tarefas do usuário."""
    def __init__(self) -> None:
        self.tasks = []

    def menu(self):
        """Exibe mensagem de boas vindas e pede a adição de uma primeira tarefa."""
        print('Bem-vindo à sua nova jornada!\n\nPara começar, crie uma tarefa!')
        tarefa1 = input('Nome da sua primeira tarefa: ')
        self.tasks.append(tarefa1)
        print('Sua primeira tarefa foi criada com sucesso!')

    def task_loop(self):
        """Gerencia um loop para adição de novas tarefas."""
        print('\nPara adicionar outra tarefa, insira o nome. Se deseja prosseguir, digite "S".')
        while True:
            task = input('Nome da tarefa: ').capitalize()
            if task == 'S':
                break
            self.tasks.append(task)
            print('Tarefa adicionada!')

    def show_tasks(self):
        """Exibe a lista de tarefas do usuário."""
        print('Suas tarefas:')
        for index, task in enumerate(self.tasks, start=1):
            print(f'[{index}] - {task}')

    def console(self):
        """Exibe e trata as opções do usuário para gerenciar as tarefas."""
        print('\nSelecione uma das tarefas para gerenciar.')
        task_number = self._get_task_number()
        print('Opções: [1] Marcar como concluída | [2] Não concluída | [3] Editar tarefa | [4] Deletar tarefa')
        user_option = input('Escolha uma das opções: ')
        self._handle_options(task_number, user_option)

    def _get_task_number(self):
        """Pergunta o número da tarefa e trata possiveis exceções."""
        while True:
            task_number = input('Número da tarefa: ')
            try:
                int_task_number = int(task_number) - 1
                print(f'Tarefa {self.tasks[int_task_number]} selecionada!')
                return int_task_number
            except IndexError:
                print('Número da tarefa não encontrado! Tente novamente.')
            except ValueError:
                print('Digite um número válido!')
            except Exception as e:
                print('Erro!', e)

    def _handle_options(self, task, option):
        """Lida com a opção selecionada pelo usuário."""
        if option == 1:
            # Implementar
            ...


def main():
    app = Aplicativo()
    app.menu()
    app.task_loop()
    app.show_tasks()
    app.console()


if __name__ == '__main__':
    main()