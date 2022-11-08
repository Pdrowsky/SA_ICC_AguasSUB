class TelaIccSup:

    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print('*' * 20)
        print('Opções disponíveis para águas superficiais:')
        print("""
                1 - plotar gráficos Mann Kendall
                2 - plotar gráficos algo
                3 - plotar rotina completa
                0 - sair
                """)
        opcao = input('Escolha uma opção: ')
        print('*' * 20)
        return int(opcao)