import os
import pandas as pd

# Importa Dados Planilha Banco de Dados

diretorio = os.chdir(r'P:\PETROBRAS-0902-ICC-Qualidade da Água 2021\BancoDados')

dados_od = pd.read_excel('ICCAguaSup.xlsx', sheet_name='OD')
dados_condutiv = pd.read_excel('ICCAguaSup.xlsx', sheet_name='Condutividade')
dados_aluminio = pd.read_excel('ICCAguaSup.xlsx', sheet_name='Aluminio')
dados_ferro = pd.read_excel('ICCAguaSup.xlsx', sheet_name='Ferro')
dados_manganes = pd.read_excel('ICCAguaSup.xlsx', sheet_name='Manganes')
dados_acidez = pd.read_excel('ICCAguaSup.xlsx', sheet_name='Acidez')
dados_sulfato = pd.read_excel('ICCAguaSup.xlsx', sheet_name='Sulfato')
dados_ph = pd.read_excel('ICCAguaSup.xlsx', sheet_name='pH')
dados_cargasacidez = pd.read_excel('ICCAguaSup.xlsx', sheet_name='CargasAcidez')
dados_cargasaluminio = pd.read_excel('ICCAguaSup.xlsx', sheet_name='CargasAluminio')
dados_cargasferro = pd.read_excel('ICCAguaSup.xlsx', sheet_name='CargasFerro')
dados_cargasmanganes = pd.read_excel('ICCAguaSup.xlsx', sheet_name='CargasManganes')
dados_cargassulfato = pd.read_excel('ICCAguaSup.xlsx', sheet_name='CargasSulfato')
dados_cargasDAM = pd.read_excel('ICCAguaSup.xlsx', sheet_name='CargasDAM')

#Coloca coluna data como indexador
dados_od=dados_od.set_index('Data')
dados_condutiv=dados_condutiv.set_index('Data')
dados_aluminio=dados_aluminio.set_index('Data')
dados_ferro=dados_ferro.set_index('Data')
dados_manganes=dados_manganes.set_index('Data')
dados_acidez=dados_acidez.set_index('Data')
dados_sulfato=dados_sulfato.set_index('Data')
dados_ph=dados_ph.set_index('Data')
dados_cargasacidez=dados_cargasacidez.set_index('Data')
dados_cargasaluminio=dados_cargasaluminio.set_index('Data')
dados_cargasferro=dados_cargasferro.set_index('Data')
dados_cargasmanganes=dados_cargasmanganes.set_index('Data')
dados_cargassulfato=dados_cargassulfato.set_index('Data')
dados_cargasDAM=dados_cargasDAM.set_index('Data')
