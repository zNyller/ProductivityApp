import logging
from config import MANAGING_OPTIONS, VALID_CONSOLE_OPTIONS
from utils import messages, functions

# Configuração básica de logging
logging.basicConfig(
    level=logging.DEBUG,  # Nível mínimo para mensagens a serem exibidas
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato da mensagem
    datefmt='%d-%m-%Y %H:%M:%S' # Formato da data/hora
    ) 

class Console:

    def __init__(self, task_list) -> None:
        self.task_list = task_list

    def insert_task_loop(self) -> None:
        """Inicia um loop para adição de novas tarefas."""
        while True:
            print(messages.TASK_LOOP_MSG)
            task_name = functions.get_valid_input('\nNome da tarefa: ')
            if task_name == 'P':
                print('Prosseguindo...')
                self.task_list.show_tasks()
                break
            self.task_list.add_task(task_name)

    def show(self) -> bool | None:
        """Exibe e trata a opção do usuário para gerenciar as tarefas e a retorna."""
        print(messages.SELECT_OPTION)
        user_option = functions.get_valid_input('Insira uma das opções: ')
        return self._handle_console_input(user_option)
    
    def _handle_console_input(self, console_option) -> bool | None:
        """Verifica se a opção inserida pelo usuário é válida e lida de acordo."""
        while console_option not in VALID_CONSOLE_OPTIONS:
            print('Opção inválida. Tente novamente!')
            console_option = functions.get_valid_input('Insira uma das opções: ')
        if console_option == 'G':
            self._manage_task()
            return False
        elif console_option == 'A':
            self.insert_task_loop()
            return False
        elif console_option == 'S':
            return True
        
    def _manage_task(self) -> None:
        """Exibe a lista de tarefas atual e as opções de gerenciamento."""
        self.task_list.show_tasks()
        print(messages.SELECT_TASK)
        task_number = self._get_valid_task_number()
        self._handle_user_option(task_number)

    def _get_valid_task_number(self) -> int | None:
        """Pergunta o número da tarefa e trata possiveis exceções."""
        while True:
            task_number = functions.get_valid_input('Número da tarefa: ')
            try:
                int_task_number = int(task_number) - 1
                print(f'\nTarefa "{self.task_list.tasks[int_task_number]["nome"]}" selecionada!')
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
            user_option = functions.convert_to_int(input_msg='Insira uma das opções: ')
            proceed = self._handle_options(task_number, user_option)
            if proceed:
                break

    def _show_managing_options(self) -> None:
        for key, value in MANAGING_OPTIONS.items():
            print(f'[{key}] - {value}')

    def _handle_options(self, task_number, option) -> bool:
        """Lida com a opção selecionada pelo usuário."""
        options_map = {
            1: self.task_list.mark_as_done,
            2: self.task_list.mark_as_undone,
            3: self.task_list.edit_task,
            4: self.task_list.delete_task,
            5: self._go_back
        }
        action = options_map.get(option, self._invalid_option)
        return action(task_number)

    def _go_back(self):
        print('Retornando...')
        return True

    def _invalid_option(self, option):
        """Exibe mensagem de opção inválida e retorna False para repetir o loop."""
        print(messages.OPTION_OUT_OF_RANGE)
        return False
    
    def _exit_app(self) -> bool:
        """Exibe mensagem de saída e retorna True para encerrar o loop."""
        print('Até a próxima!')
        return True