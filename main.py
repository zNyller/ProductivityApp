import logging
import messages
import utils

class Aplicativo:
    """Clase principal. Cria, Gerencia e Exibe as tarefas do usuário."""

    DONE = 'Concluída'
    UNDONE = 'Não concluída'

    def __init__(self) -> None:
        self.tasks = []
        self.options = {
            1: 'Concluir', 2: 'Desmarcar conclusão', 3: 'Editar', 4: 'Deletar', 5: 'Sair'
        }

    def menu(self):
        """Exibe mensagem de boas vindas e pede a adição de uma primeira tarefa."""
        print(messages.WELCOME_MSG)
        tarefa1 = input('Nome da sua primeira tarefa: ')
        self.tasks.append({'nome': tarefa1, 'status': self.UNDONE})
        print(messages.TASK_CREATED)

    def task_loop(self):
        """Gerencia um loop para adição de novas tarefas."""
        print(messages.TASK_LOOP_MSG)
        while True:
            task_name = input('Nome da tarefa: ').capitalize()
            if task_name == 'S':
                break
            self.add_task(task_name)

    def add_task(self, name):
        """Cria um dicionário com 'nome' e 'status' para a nova tarefa e o adiciona na lista."""
        new_task = {'nome': name, 'status': self.UNDONE}
        self.tasks.append(new_task)
        print(messages.TASK_CREATED)

    def show_tasks(self):
        """Exibe a lista de tarefas do usuário."""
        print(messages.YOUR_TASKS)
        for index, task in enumerate(self.tasks, start=1):
            print(f'[{index}] - {task["nome"]} | {task["status"]}')

    def console(self):
        """Exibe e trata as opções do usuário para gerenciar as tarefas."""
        print(messages.SELECT_TASK)
        task_number = self._get_task_number()
        for key, value in self.options.items():
            print(f'[{key}] - {value}')
        user_option = utils.convert_to_int(input_msg='Escolha uma das opções: ')
        self._handle_options(task_number, user_option)

    def _get_task_number(self):
        """Pergunta o número da tarefa e trata possiveis exceções."""
        while True:
            task_number = input('Número da tarefa: ')
            try:
                int_task_number = int(task_number) - 1
                print(f'\nTarefa {self.tasks[int_task_number]["nome"]} selecionada!')
                return int_task_number
            except IndexError:
                logging.error('Número da tarefa não encontrado! Tente novamente.')
            except ValueError:
                logging.error('Digite um número válido!')
            except Exception as e:
                logging.error('Erro!', e)

    def _handle_options(self, task, option):
        """Lida com a opção selecionada pelo usuário."""
        current_task = self.tasks[task]
        if option == 1:
            current_task['status'] = self.DONE
            print(messages.MARKED_AS_DONE)
        elif option == 2:
            if current_task['status'] != self.UNDONE:
                current_task['status'] = self.UNDONE
                print(messages.MARKED_AS_UNDONE)
            else:
                print(messages.ALREADY_UNDONE)
        elif option == 3:
            ...
        elif option == 4:
            ...
        elif option == 5:
            print('Até a próxima!')
        else:
            print(messages.OPTION_OUT_OF_RANGE)


def main():
    app = Aplicativo()
    app.menu()
    app.task_loop()
    app.show_tasks()
    app.console()
    app.show_tasks()


if __name__ == '__main__':
    main()