import messages

class TaskList:

    DONE = 'Concluída'
    UNDONE = 'Não concluída'

    def __init__(self) -> None:
        self.tasks = []

    def add_task(self: 'TaskList', name: str) -> None:
        """Armazena a tarefa com 'nome' e 'status' em um dicionário e o adiciona na lista."""
        new_task = {'nome': name, 'status': self.UNDONE}
        self.tasks.append(new_task)
        print(messages.TASK_CREATED)

    def show_tasks(self) -> None:
        """Exibe a lista de tarefas do usuário."""
        print(messages.YOUR_TASKS)
        for index, task in enumerate(self.tasks, start=1):
            print(f'[{index}] - {task["nome"]} | {task["status"]}')

    def mark_as_done(self, task_number):
        """Marca a tarefa como concluída, com base no índice recebido."""
        self.tasks[task_number]['status'] = self.DONE
        print(messages.MARKED_AS_DONE)
        return True


    def mark_as_undone(self, task_number):
        """Marca a tarefa como Não concluída, com base no índice recebido."""
        current_task = self.tasks[task_number]
        if current_task['status'] != self.UNDONE:
            current_task['status'] = self.UNDONE
            print(messages.MARKED_AS_UNDONE)
            return True
        else:
            print(messages.ALREADY_UNDONE)
            return False # Retorna False para seguir no loop até receber uma opção válida.
        
    def edit_task(self, task_number):
        """Edita a tarefa com base no índice recebido."""
        # Implementar edição
        return True


    def delete_task(self, task_number):
        """Deleta a tarefa com base no índice recebido."""
        deleted_task = self.tasks.pop(task_number)
        print(f'Tarefa "{deleted_task["nome"]}" deletada!')
        return True
