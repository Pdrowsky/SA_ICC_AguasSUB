class TelaIccSub:

    def __init__(self):
        pass

    def mostrar_opcoes(self):
        print('*' * 20)
        print('Opções disponíveis para águas subterrâneas:')
        print("""
                1 - plotar gráficos Mann Kendall
                2 - plotar gráficos algo
                3 - plotar rotina completa
                0 - sair
                """)
        opcao = input('Escolha uma opção: ')
        print('*' * 20)
        return int(opcao)

    def opcoes_mk_base(self):
        print('*'*20)
        print('Que tipo de teste deseja realizar?')
        print("""
                1 - padrão
                2 - multiníveis
                0 - sair
        """)
        opcao = input('Escolha uma opção: ')
        print('*' * 20)
        return int(opcao)

    def opcoes_mk_padrao(self):
        print('*' * 5 + ' TESTE PADRÃO ' + '*' * 5)
        print('Qual parâmetro deseja testar?')
        print("""
                1 - pH
                2 - ferro
                3 - sulfato
                4 - acidez
                5 - manganês
                0 - sair
                """)
        opcao = input('Escolha uma opção: ')
        print('*' * 20)
        return int(opcao)

    def opcoes_mk_multiniveis(self):
        print('*' * 5 + ' TESTE MULTINÍVEIS ' + '*' * 5)
        print('Qual parâmetro deseja testar?')
        print("""
                        1 - pH
                        2 - ferro
                        3 - acidez
                        4 - alumínio
                        0 - sair
                        """)
        opcao = input('Escolha uma opção: ')
        print('*' * 20)
        return int(opcao)