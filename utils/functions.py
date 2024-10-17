from typing import Any

def get_valid_input(input_msg: str) -> Any:
    """Recebe uma mensagem para solicitar o input e lida com entradas inválidas."""
    prompt = input(input_msg).strip().upper()
    while not prompt:
        print('Entrada inválida. Por favor, tente novamente!')
        prompt = input(input_msg).strip().upper()
    return prompt

def convert_to_int(input_msg) -> int:
    """Recebe uma mensagem para solicitar o input e tenta convertê-lo para int."""
    while True:
        user_input = input(input_msg)
        try:
            int_input = int(user_input)
            return int_input
        except ValueError:
            print('Insira um número válido!')