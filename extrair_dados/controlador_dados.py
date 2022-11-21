from SA_ICC_AguasSUB.extrair_dados.extrair_dados import ExtrairDados


class ControladorDados:

    def __int__(self):
        self.__controlador_extrair = ExtrairDados

    def extrair_dados(self):
        self.__controlador_extrair.criar_objetos()

    def transcrever_dados(self):
        self.__controlador_extrair.preparar_parametros()
        self.__controlador_extrair.colar_objetos()
        self.__controlador_extrair.salvar_planilha()

    def sair(self):
        pass
