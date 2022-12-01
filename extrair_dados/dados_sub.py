import os
import pandas as pd


#Importa Dados Planilha Banco de Dados

diretorio = os.chdir(r'P:\PETROBRAS-0902-ICC-Qualidade da Água 2021\BancoDados')

dados_nivel = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Nivel')
dados_aluminio = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Aluminio')
dados_ferro = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Ferro')
dados_manganes = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Manganes')
dados_acidez = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Acidez')
dados_sulfato = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Sulfato')
dados_ph = pd.read_excel('ICCAguaSub.xlsx', sheet_name='pH')

#Coloca coluna data como indexador
dados_nivel = dados_nivel.set_index('Data')
dados_aluminio = dados_aluminio.set_index('Data')
dados_ferro = dados_ferro.set_index('Data')
dados_manganes = dados_manganes.set_index('Data')
dados_acidez = dados_acidez.set_index('Data')
dados_sulfato = dados_sulfato.set_index('Data')
dados_ph = dados_ph.set_index('Data')