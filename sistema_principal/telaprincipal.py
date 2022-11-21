class TelaPrincipal:

    def __init__(self):
        pass

    def tela_opcoes(self):
        print('*' * 20)
        print("""
* Sistema teste de plotagem de águas superficiais e subterrâneas *
        1 - menu de águas subterrâneas
        2 - menu de águas superficiais
        3 - extrair dados
        0 - sair
        """)
        opcao = input('Escolha uma opção: ')
        print('*' * 20)
        return int(opcao)
