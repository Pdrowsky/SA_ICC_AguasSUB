import sys
from sistema_principal.telaprincipal import TelaPrincipal
from icc_graf_aguas_sub.controlador_icc_sub import ControladorSub
from icc_graf_aguas_sup.controlador_icc_sup import ControladorSup
#from extrair_dados.controlador_dados import ControladorDados
from extrair_dados.extrair_dados import ExtrairDados


class ControladorPrincipal:

    def __init__(self):
        self.tela_principal = TelaPrincipal()
        self.controlador_icc_sub = ControladorSub()
        self.controlador_icc_sup = ControladorSup()
        self.extracao_dados = ExtrairDados()


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
        self.extracao_dados.criar_objetos()
        self.extracao_dados.preparar_parametros()
        self.extracao_dados.colar_objetos()
        self.extracao_dados.salvar_planilha()

    def finalizar(self):
        sys.exit()