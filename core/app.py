import logging
import utils.messages as messages
import utils.functions as functions
from task_list import TaskList
from core.console import Console

# Configuração básica de logging
logging.basicConfig(
    level=logging.DEBUG,  # Nível mínimo para mensagens a serem exibidas
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato da mensagem
    datefmt='%d-%m-%Y %H:%M:%S' # Formato da data/hora
    ) 

class Aplicativo:
    """Clase principal. Cria, gerencia e exibe as tarefas do usuário."""

    def __init__(self) -> None:
        self.running = False
        self.task_list = TaskList()
        self.console = Console(self.task_list)

    def run(self) -> None:
        """Inicia o aplicativo chamando suas funções principais."""
        self.running = True
        self.show_welcome_menu()
        self.insert_task_loop()
        self.main_loop()

    def show_welcome_menu(self) -> None:
        """Exibe a mensagem de boas-vindas e pede a adição de uma primeira tarefa."""
        print(messages.WELCOME_MSG)
        first_task = functions.get_valid_input('Nome da sua primeira tarefa: ')
        self.task_list.add_task(first_task)

    def insert_task_loop(self) -> None:
        """Inicia um loop para adição de novas tarefas."""
        self.console.insert_task_loop()

    def main_loop(self) -> None:
        """Gerencia o loop principal do aplicativo."""
        while self.running:
            encerrar = self.console.show()
            if encerrar:
                logging.info('Quebrando o loop principal')
                self.running = False