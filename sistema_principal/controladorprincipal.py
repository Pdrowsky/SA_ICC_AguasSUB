import sys
from SA_ICC_AguasSUB.sistema_principal.telaprincipal import TelaPrincipal
from SA_ICC_AguasSUB.icc_graf_aguas_sub.controlador_icc_sub import ControladorSub
from SA_ICC_AguasSUB.icc_graf_aguas_sup.controlador_icc_sup import ControladorSup


class ControladorPrincipal:

    def __init__(self):
        self.tela_principal = TelaPrincipal()
        self.controlador_icc_sub = ControladorSub(self)
        self.controlador_icc_sup = ControladorSup(self)


    def inicia(self):
        opcoes = {0: self.finalizar, 1: self.abrir_menu_sub, 2: self.abrir_menu_sup}

        while True:
            opcao = (self.tela_principal.tela_opcoes())
            opcoes[opcao]()


    def abrir_menu_sub(self):
        self.controlador_icc_sub.mostrar_menu()

    def abrir_menu_sup(self):
        self.controlador_icc_sup.mostrar_menu()

    def finalizar(self):
        sys.exit()