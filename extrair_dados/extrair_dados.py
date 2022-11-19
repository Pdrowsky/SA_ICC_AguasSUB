import openpyxl
import openpyxl as xl

wb1 = xl.load_workbook('dados_crus.xlsx')
sheet1 = wb1['Data']
wb2 = openpyxl.Workbook()
todos_resultados = []
lista_pontos = []

class Resultado:
    def __init__(self,
                 codigo = str,
                 nome = str,
                 tipo = str,
                 parametro = str,
                 resultado = str,
                 unidade = str
                 ):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.parametro = parametro
        self.resultado = resultado
        self.unidade = unidade

for linha in sheet1(2, sheet1.max_row + 1):
    resultado = Resultado(sheet1.cell(linha, 1).value, #coluna codigo
                          sheet1.cell(linha, 4).value, #coluna nome
                          sheet1.cell(linha, 5).value, #coluna tipo
                          sheet1.cell(linha, 13).value, #coluna parametro
                          sheet1.cell(linha, 14).value, #coluna resultado
                          sheet1.cell(linha, 15).value #coluna unidade
                          )
    todos_resultados.append(resultado)
    if resultado.nome not in lista_pontos:
        lista_pontos.append(resultado.nome)


for resultado in todos_resultados:
    pass