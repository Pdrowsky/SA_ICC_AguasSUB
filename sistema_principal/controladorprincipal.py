import sys
from SA_ICC_AguasSUB.sistema_principal.telaprincipal import TelaPrincipal
from SA_ICC_AguasSUB.icc_graf_aguas_sub.controlador_icc_sub import ControladorSub
from SA_ICC_AguasSUB.icc_graf_aguas_sup.controlador_icc_sup import ControladorSup
from SA_ICC_AguasSUB.extrair_dados.controlador_dados import ControladorDados


class ControladorPrincipal:

    def __init__(self):
        self.tela_principal = TelaPrincipal()
        self.controlador_icc_sub = ControladorSub
        self.controlador_icc_sup = ControladorSup(self)
        self.controlado_dados = ControladorDados


    def inicia(self):
        opcoes = {0: self.finalizar, 1: self.abrir_menu_sub,
                  2: self.abrir_menu_sup, 3: self.extrair_dados}

        while True:
            opcao = (self.tela_principal.tela_opcoes())
            opcoes[opcao]()


    def abrir_menu_sub(self):
        self.controlador_icc_sub.mostrar_menu()

    def abrir_menu_sup(self):
        self.controlador_icc_sup.mostrar_menu()

    def extrair_dados(self):
        self.controlado_dados.extrair_dados()
        self.controlado_dados.transcrever_dados()

    def finalizar(self):
        sys.exit()