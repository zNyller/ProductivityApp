import logging
import messages
import utils

# Configuração básica de logging
logging.basicConfig(
    level=logging.DEBUG,  # Nível mínimo para mensagens a serem exibidas
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato da mensagem
    datefmt='%d-%m-%Y %H:%M:%S' # Formato da data/hora
    ) 

class Aplicativo:
    """Clase principal. Cria, Gerencia e Exibe as tarefas do usuário."""

    DONE = 'Concluída'
    UNDONE = 'Não concluída'
    VALID_CONSOLE_OPTIONS = ('G', 'A', 'S')

    def __init__(self) -> None:
        self.running = False
        self.tasks = []
        self.managing_options = {
            1: 'Concluir', 
            2: 'Desmarcar conclusão', 
            3: 'Editar', 
            4: 'Deletar', 
            5: 'Voltar'
        }

    def run(self):
        """Inicia o aplicativo chamando suas funções principais."""
        self.running = True
        self.show_menu()
        self.task_loop()
        self.main_loop()

    def show_menu(self) -> None:
        """Exibe a mensagem de boas-vindas e pede a adição de uma primeira tarefa."""
        print(messages.WELCOME_MSG)
        first_task = utils.get_valid_input('Nome da sua primeira tarefa: ').capitalize()
        self._add_task(first_task)

    def task_loop(self) -> None:
        """Inicia um loop para adição de novas tarefas."""
        print(messages.TASK_LOOP_MSG)
        while True:
            task_name = utils.get_valid_input('Nome da tarefa: ').capitalize()
            if task_name != 'P':
                self._add_task(task_name)
                continue
            print('Prosseguindo...')
            self._show_tasks()
            break

    def main_loop(self):
        """Gerencia o loop principal do aplicativo."""
        while self.running:
            encerrar = self.console()
            if encerrar:
                print('Até a próxima!')
                logging.info('Quebrando o loop principal')
                self.running = False

    def console(self) -> bool | None:
        """Exibe e trata as opções do usuário para gerenciar as tarefas."""
        print(messages.SELECT_OPTION)
        console_option = utils.get_valid_input('Insira uma das opções: ').upper()
        option_selected = self._handle_console_input(console_option)
        return option_selected
        
    def _add_task(self, name: str) -> None:
        """Armazena a tarefa com 'nome' e 'status' em um dicionário e o adiciona na lista."""
        new_task = {'nome': name, 'status': self.UNDONE}
        self.tasks.append(new_task)
        print(messages.TASK_CREATED)

    def _show_tasks(self) -> None:
        """Exibe a lista de tarefas do usuário."""
        print(messages.YOUR_TASKS)
        for index, task in enumerate(self.tasks, start=1):
            print(f'[{index}] - {task["nome"]} | {task["status"]}')

    def _handle_console_input(self, console_option) -> bool | None:
        """Verifica se a opção inserida pelo usuário é válida e lida de acordo."""
        while console_option not in self.VALID_CONSOLE_OPTIONS:
            print('Opção inválida. Tente novamente!')
            console_option = input('Insira uma das opções: ').upper()
        if console_option == 'G':
            return self._manage_task()
        elif console_option == 'A':
            self.task_loop()
            return False
        elif console_option == 'S':
            return True

    def _manage_task(self):
        """Exibe a lista de tarefas atual e as opções de gerenciamento."""
        print(messages.SELECT_TASK)
        self._show_tasks()
        task_number = self._get_valid_task_number()
        self._handle_user_option(task_number)

    def _get_valid_task_number(self) -> int | None:
        """Pergunta o número da tarefa e trata possiveis exceções."""
        while True:
            task_number = utils.get_valid_input('Número da tarefa: ')
            try:
                int_task_number = int(task_number) - 1
                print(f'\nTarefa "{self.tasks[int_task_number]["nome"]}" selecionada!')
                return int_task_number
            except IndexError:
                print('Número da tarefa não encontrado! Tente novamente.')
                logging.error('Input foi um número fora do range.')
            except ValueError:
                print('Digite um número válido!')
                logging.error('Input não foi um número inteiro!')
            except Exception as e:
                logging.error(f'Erro inesperado: {e}!')
            
    def _handle_user_option(self, task_number: int):
        """Exibe as opções de gerenciamento e lida com a opção escolhida pelo usuário."""
        self._show_managing_options()
        while True:
            user_option = utils.convert_to_int(input_msg='Insira uma das opções: ')
            proceed = self._handle_options(task_number, user_option)
            if proceed:
                break

    def _show_managing_options(self) -> None:
        for key, value in self.managing_options.items():
            print(f'[{key}] - {value}')

    def _handle_options(self, task_number, option) -> bool:
        """Lida com a opção selecionada pelo usuário."""
        options_map = {
            1: self._mark_as_done,
            2: self._mark_as_undone,
            3: self._edit_task,
            4: self._delete_task,
            5: self._go_back
        }
        action = options_map.get(option, self._invalid_option)
        return action(task_number)

    def _mark_as_done(self, task_number):
        self.tasks[task_number]['status'] = self.DONE
        print(messages.MARKED_AS_DONE)
        return True

    def _mark_as_undone(self, task_number):
        current_task = self.tasks[task_number]
        if current_task['status'] != self.UNDONE:
            current_task['status'] = self.UNDONE
            print(messages.MARKED_AS_UNDONE)
        else:
            print(messages.ALREADY_UNDONE)
            return False # Retorna False para seguir no loop até receber uma opção válida.
        return True
        
    def _edit_task(self, task_number):
        # Implementar edição
        return True

    def _delete_task(self, task_number):
        deleted_task = self.tasks.pop(task_number)
        print(f'Tarefa "{deleted_task["nome"]}" deletada!')
        return True

    def _go_back(self):
        print('Retornando...')
        return True

    def _invalid_option(self):
        print(messages.OPTION_OUT_OF_RANGE)
        return False