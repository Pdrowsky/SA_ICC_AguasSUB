from SA_ICC_AguasSUB.icc_graf_aguas_sub.telaiccsub import TelaIccSub


class ControladorSub:

    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        self.tela_icc_sub = TelaIccSub()

    def mostrar_menu(self):
        opcoes = {0: self.sair, 1: self.plotar_mk, 2: self.plotar_outro,
                  3: self.plotar_tudo}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sub.mostrar_opcoes())
            opcoes[opcao]()

    def plotar_mk(self):
        pass

    def plotar_outro(self):
        pass

    def plotar_tudo(self):
        pass

    def sair(self):
        pass