from icc_graf_aguas_sub.telaiccsub import TelaIccSub
from icc_graf_aguas_sub.calculo_mk import MannKendall


class ControladorSub:

    def __init__(self):
        self.tela_icc_sub = TelaIccSub()
        self.calc_mk = MannKendall

    def mostrar_menu(self):
        opcoes = {0: self.sair, 1: self.plotar_mk, 2: self.plotar_outro,
                  3: self.plotar_tudo}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sub.mostrar_opcoes())
            opcoes[opcao]()

    def plotar_mk(self):
        opcoes = {0: self.sair, 1: self.menu_mk_padrao,
                  2: self.menu_mk_multiniveis}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sub.opcoes_mk_base())
            opcoes[opcao]()

    def plotar_outro(self):
        pass

    def plotar_tudo(self):
        pass

    def sair(self):
        pass

    def menu_mk_padrao(self):
        opcoes = {0: self.sair, 1: self.calc_mk.tendencia_ph,
                  2: self.calc_mk.tendencia_ferro,
                  3: self.calc_mk.tendencia_sulfato,
                  4: self.calc_mk.tendencia_acidez,
                  5: self.calc_mk.tendencia_manganes}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sub.opcoes_mk_padrao())
            opcoes[opcao]()

    def menu_mk_multiniveis(self):
        opcoes = {0: self.sair, 1: self.calc_mk.tendencia_mn_ph,
                  2: self.calc_mk.tendencia_mn_ferro,
                  3: self.calc_mk.tendencia_mn_acidez,
                  4: self.calc_mk.tendencia_mn_aluminio}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sub.opcoes_mk_multiniveis())
            opcoes[opcao]()