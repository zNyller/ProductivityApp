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
        self.options = {
            1: 'Concluir', 
            2: 'Desmarcar conclusão', 
            3: 'Editar', 
            4: 'Deletar', 
            5: 'Voltar'
        }

    def run(self):
        """Loop principal do aplicativo."""
        self.running = True
        self.show_menu()
        while self.running:
            self.task_loop()
            self.show_tasks()
            continuar = self.console()
            if continuar:
                logging.info('Quebrando o loop principal')
                break
            self.show_tasks()

    def show_menu(self) -> None:
        """Exibe a mensagem de boas vindas e pede a adição de uma primeira tarefa."""
        print(messages.WELCOME_MSG)
        tarefa1 = input('Nome da sua primeira tarefa: ')
        self._add_task(tarefa1)

    def task_loop(self) -> None:
        """Gerencia um loop para adição de novas tarefas."""
        print(messages.TASK_LOOP_MSG)
        while True:
            task_name = input('Nome da tarefa: ').capitalize()
            if task_name == 'P':
                print('Prosseguindo...')
                break
            self._add_task(task_name)

    def show_tasks(self) -> None:
        """Exibe a lista de tarefas do usuário."""
        print(messages.YOUR_TASKS)
        for index, task in enumerate(self.tasks, start=1):
            print(f'[{index}] - {task["nome"]} | {task["status"]}')
        print()

    def console(self) -> None | bool:
        """Exibe e trata as opções do usuário para gerenciar as tarefas."""
        print(messages.SELECT_OPTION)
        console_option = input('Insira uma das opções: ').capitalize().strip()[0:1]
        while console_option not in self.VALID_CONSOLE_OPTIONS:
            print('Opção inválida. Tente novamente!')
            console_option = input('Insira uma das opções: ').capitalize().strip()[0:1]
        if console_option == 'G':
            return self._manage_task()
        elif console_option == 'A':
            return False
        elif console_option == 'S':
            print('Até a próxima!')
            return True
        
    def _add_task(self, name) -> None:
        """Armazena a tarefa com 'nome' e 'status' em um dicionário e o adiciona na lista."""
        new_task = {'nome': name, 'status': self.UNDONE}
        self.tasks.append(new_task)
        print(messages.TASK_CREATED)

    def _manage_task(self):
        print(messages.SELECT_TASK)
        self.show_tasks()
        task_number = self._get_task_number()
        if task_number is not False:
            for key, value in self.options.items():
                print(f'[{key}] - {value}')
            while True:
                user_option = utils.convert_to_int(input_msg='Escolha uma das opções: ')
                continuar = self._handle_options(task_number, user_option)
                if continuar:
                    return False
        else:
            # Retorna True para quebrar o loop e continuar o código
            return True

    def _get_task_number(self) -> int | bool:
        """Pergunta o número da tarefa e trata possiveis exceções."""
        while True:
            task_number = input('Número da tarefa: ').capitalize()
            if task_number is not None and task_number != 'S':
                try:
                    int_task_number = int(task_number) - 1
                    print(f'\nTarefa {self.tasks[int_task_number]["nome"]} selecionada!')
                    return int_task_number
                except IndexError:
                    print('Número da tarefa não encontrado! Tente novamente.')
                    logging.error('Input foi um número fora do range.')
                except ValueError:
                    print('Digite um número válido!')
                    logging.error('Input não foi um número inteiro!')
                except Exception as e:
                    logging.error('Erro!', e)
            elif task_number is None:
                print('Comando inválido. Tente novamente!')
            else:
                print('Até a próxima!')
                return False

    def _handle_options(self, task, option) -> bool:
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
                return False # Retorna False para seguir no loop até receber uma opção válida.
        elif option == 3:
            ...
        elif option == 4:
            ...
        elif option == 5:
            print('Retornando...')
        else:
            print(messages.OPTION_OUT_OF_RANGE)
        return True # Retorna True para quebrar o loop e continuar o código