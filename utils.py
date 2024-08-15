def convert_to_int(input_msg):
    """Recebe uma mensagem para solicitar o input e tenta convertê-lo para int."""
    while True:
        user_input = input(input_msg)
        try:
            int_input = int(user_input)
            return int_input
        except ValueError:
            print('Insira um número válido!')