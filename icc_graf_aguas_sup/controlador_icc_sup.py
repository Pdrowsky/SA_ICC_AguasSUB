from icc_graf_aguas_sup.telaiccsup import TelaIccSup
from icc_graf_aguas_sup.calculo_mk_sup import MannKendallSup
from icc_graf_aguas_sup.Rotina_Graficos_ICC_Aguasup import RotinaGraficosSup


class ControladorSup:

    def __init__(self):
        self.calc_mk = MannKendallSup()
        self.tela_icc_sup = TelaIccSup()
        self.rotina_sup = RotinaGraficosSup()

    def mostrar_menu(self):
        opcoes = {0: self.sair,
                  1: self.plotar_rotina_mk_sup,
                  2: self.plotar_rotina_sup,
                  3: self.plotar_tudo}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sup.mostrar_opcoes())
            opcoes[opcao]()

    def plotar_mk(self):
        opcoes = {0: self.sair, 1: self.menu_mk_padrao,
                  2: self.menu_mk_multiniveis}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sup.opcoes_mk_base())
            opcoes[opcao]()

    def plotar_rotina_sup(self):
        self.rotina_sup.definir_diretorio()
        self.rotina_sup.plotar_base()
        self.rotina_sup.plotar_principais_conjunto()
        self.rotina_sup.plotar_cargas()
        #self.rotina_sup.plotar_multinivel()
        #self.rotina_sup.plotar_restante()

    def plotar_rotina_mk_sup(self):
        self.rotina_sup.definir_diretorio()
        self.calc_mk.plot_todos_basicos()
        self.calc_mk.plot_todos_cargas()

    def plotar_tudo(self):
        self.plotar_rotina_sup()
        self.plotar_rotina_mk_sup()

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
            opcao = (self.tela_icc_sup.opcoes_mk_padrao())
            opcoes[opcao]()

    def menu_mk_multiniveis(self):
        opcoes = {0: self.sair, 1: self.calc_mk.tendencia_mn_ph,
                  2: self.calc_mk.tendencia_mn_ferro,
                  3: self.calc_mk.tendencia_mn_acidez,
                  4: self.calc_mk.tendencia_mn_aluminio}
        opcao = 1
        while opcao != 0:
            opcao = (self.tela_icc_sup.opcoes_mk_multiniveis())
            opcoes[opcao]()
