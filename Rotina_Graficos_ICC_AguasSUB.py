# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:44:19 2021

@author: Thiago
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import matplotlib.gridspec as gridspec

# Importa Dados Planilha Banco de Dados

diretorio = os.chdir(r'P:\PETROBRAS-0902-ICC-Qualidade da Água 2021\BancoDados')


dados_nivel = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Nivel')
dados_aluminio = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Aluminio')
dados_ferro = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Ferro')
dados_manganes = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Manganes')  
dados_acidez = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Acidez')
dados_sulfato = pd.read_excel('ICCAguaSub.xlsx', sheet_name='Sulfato')
dados_ph = pd.read_excel('ICCAguaSub.xlsx', sheet_name='pH')

#Coloca coluna data como indexador
dados_nivel=dados_nivel.set_index('Data')
dados_aluminio=dados_aluminio.set_index('Data')
dados_ferro=dados_ferro.set_index('Data')
dados_manganes=dados_manganes.set_index('Data')
dados_acidez=dados_acidez.set_index('Data')
dados_sulfato=dados_sulfato.set_index('Data')
dados_ph=dados_ph.set_index('Data')

#Pasta Figuras
diretorio = os.chdir(r'P:\PETROBRAS-0902-ICC-Qualidade da Água 2021\BancoDados\Figuras\AguaSub\C31')


#Plota gráficos Nível
ax=dados_nivel.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Nível')
plt.savefig('Serie_nivel1.png', bbox_inches='tight')
ax=dados_nivel.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Nível')
plt.savefig('Serie_nivel2.png', bbox_inches='tight')
ax=dados_nivel.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Nível')
plt.savefig('Serie_nivel3.png', bbox_inches='tight')

#Plota gráficos Alumínio
ax=dados_aluminio.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Alumínio (mg/L)')
plt.savefig('Serie_Aluminio1.png', bbox_inches='tight')
ax=dados_aluminio.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Alumínio (mg/L)')
plt.savefig('Serie_Aluminio2.png', bbox_inches='tight')
ax=dados_aluminio.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Alumínio (mg/L)')
plt.savefig('Serie_Aluminio3.png', bbox_inches='tight')

#Plota gráficos Ferro
ax=dados_ferro.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Ferro (mg/L)')
plt.savefig('Serie_ferro1.png', bbox_inches='tight')
ax=dados_ferro.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Ferro (mg/L)')
plt.savefig('Serie_ferro2.png', bbox_inches='tight')
ax=dados_ferro.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Ferro (mg/L)')
plt.savefig('Serie_ferro3.png', bbox_inches='tight')

#Plota gráficos Manganes
ax=dados_manganes.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Manganês (mg/L)')
plt.savefig('Serie_manganes1.png', bbox_inches='tight')
ax=dados_manganes.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Manganês (mg/L)')
plt.savefig('Serie_manganes2.png', bbox_inches='tight')
ax=dados_manganes.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Manganês (mg/L)')
plt.savefig('Serie_manganes3.png', bbox_inches='tight')

#Plota gráficos Acidez
ax=dados_acidez.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Acidez Total (mg/L)')
plt.savefig('Serie_acidez1.png', bbox_inches='tight')
ax=dados_acidez.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Acidez Total (mg/L)')
plt.savefig('Serie_acidez2.png', bbox_inches='tight')
ax=dados_acidez.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Acidez Total (mg/L)')
plt.savefig('Serie_acidez3.png', bbox_inches='tight')

#Plota gráficos Sulfato
ax=dados_sulfato.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Sulfato (mg/L)')
plt.savefig('Serie_sulfato1.png', bbox_inches='tight')
ax=dados_sulfato.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Sulfato (mg/L)')
plt.savefig('Serie_sulfato2.png', bbox_inches='tight')
ax=dados_sulfato.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='Sulfato (mg/L)')
plt.savefig('Serie_sulfato3.png', bbox_inches='tight')

#Plota gráficos pH
ax=dados_ph.iloc[:,1:13].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='pH')
plt.savefig('Serie_pH1.png', bbox_inches='tight')
ax=dados_ph.iloc[:,14:26].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='pH')
plt.savefig('Serie_pH2.png', bbox_inches='tight')
ax=dados_ph.iloc[:,27:35].plot(subplots=True,layout=(12,3), figsize=(20,40), style=['.-', '.-', '.-','.-','.-','.-','.-','.-','.-','.-','.-','.-'], ylabel='pH')
plt.savefig('Serie_pH3.png', bbox_inches='tight')


#Plota Gráfico principais poços dos conjuntos - Alumínio

PMI02_al = dados_aluminio['PMI-02']
PMI04_al = dados_aluminio['PMI-04']
PMI21_al = dados_aluminio['PMI-21']
PMI20_al = dados_aluminio['PMI-20']
PMI15_al = dados_aluminio['PMI-15']
PMI08_al = dados_aluminio['PMI-08']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PMI02_al, '.-', label='PMI-02')
ax.plot(PMI04_al, '.-', label='PMI-04')
ax.plot(PMI21_al, '.-', label='PMI-21')
ax.plot(PMI20_al, '.-', label='PMI-20')
ax.plot(PMI15_al, '.-', label='PMI-15')
ax.plot(PMI08_al, '.-', label='PMI-08')
leg = ax.legend()


ax.set(xlabel='Ano', ylabel='Alumínio (mg/L)')
ax.grid()
plt.savefig('Conjuntos_aluminio.png', bbox_inches='tight', dpi=300)

#Plota Gráfico principais poços dos conjuntos - Ferro

PMI02_fe = dados_ferro['PMI-02']
PMI04_fe = dados_ferro['PMI-04']
PMI21_fe = dados_ferro['PMI-21']
PMI20_fe = dados_ferro['PMI-20']
PMI15_fe = dados_ferro['PMI-15']
PMI08_fe = dados_ferro['PMI-08']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PMI02_fe, '.-', label='PMI-02')
ax.plot(PMI04_fe, '.-', label='PMI-04')
ax.plot(PMI21_fe, '.-', label='PMI-21')
ax.plot(PMI20_fe, '.-', label='PMI-20')
ax.plot(PMI15_fe, '.-', label='PMI-15')
ax.plot(PMI08_fe, '.-', label='PMI-08')
leg = ax.legend()


ax.set(xlabel='Ano', ylabel='Ferro Total(mg/L)')
ax.grid()

plt.savefig('Conjuntos_ferro.png', bbox_inches='tight', dpi=300)

#Plota Gráfico principais poços dos conjuntos - Manganês

PMI02_mg = dados_manganes['PMI-02']
PMI04_mg = dados_manganes['PMI-04']
PMI21_mg = dados_manganes['PMI-21']
PMI20_mg = dados_manganes['PMI-20']
PMI15_mg = dados_manganes['PMI-15']
PMI08_mg = dados_manganes['PMI-08']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PMI02_mg, '.-', label='PMI-02')
ax.plot(PMI04_mg, '.-', label='PMI-04')
ax.plot(PMI21_mg, '.-', label='PMI-21')
ax.plot(PMI20_mg, '.-', label='PMI-20')
ax.plot(PMI15_mg, '.-', label='PMI-15')
ax.plot(PMI08_mg, '.-', label='PMI-08')
leg = ax.legend()


ax.set(xlabel='Ano', ylabel='Manganês Total(mg/L)')
ax.grid()

plt.savefig('Conjuntos_manganes.png', bbox_inches='tight', dpi=300)

#Plota Gráfico principais poços dos conjuntos - Acidez

PMI02_ac = dados_acidez['PMI-02']
PMI04_ac = dados_acidez['PMI-04']
PMI21_ac = dados_acidez['PMI-21']
PMI20_ac = dados_acidez['PMI-20']
PMI15_ac = dados_acidez['PMI-15']
PMI08_ac = dados_acidez['PMI-08']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PMI02_ac, '.-', label='PMI-02')
ax.plot(PMI04_ac, '.-', label='PMI-04')
ax.plot(PMI21_ac, '.-', label='PMI-21')
ax.plot(PMI20_ac, '.-', label='PMI-20')
ax.plot(PMI15_ac, '.-', label='PMI-15')
ax.plot(PMI08_ac, '.-', label='PMI-08')
leg = ax.legend()


ax.set(xlabel='Ano', ylabel='Acidez Total(mg/L)')
ax.grid()

plt.savefig('Conjuntos_acidez.png', bbox_inches='tight', dpi=300)

#Plota Gráfico principais poços dos conjuntos - Sulfato

PMI02_so = dados_sulfato['PMI-02']
PMI04_so = dados_sulfato['PMI-04']
PMI21_so = dados_sulfato['PMI-21']
PMI20_so = dados_sulfato['PMI-20']
PMI15_so = dados_sulfato['PMI-15']
PMI08_so = dados_sulfato['PMI-08']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PMI02_so, '.-', label='PMI-02')
ax.plot(PMI04_so, '.-', label='PMI-04')
ax.plot(PMI21_so, '.-', label='PMI-21')
ax.plot(PMI20_so, '.-', label='PMI-20')
ax.plot(PMI15_so, '.-', label='PMI-15')
ax.plot(PMI08_so, '.-', label='PMI-08')
leg = ax.legend()


ax.set(xlabel='Ano', ylabel='Sulfato Total(mg/L)')
ax.grid()

plt.savefig('Conjuntos_sulfato.png', bbox_inches='tight', dpi=300)

#Plota Gráfico principais poços dos conjuntos - pH

PMI02_ph = dados_ph['PMI-02']
PMI04_ph = dados_ph['PMI-04']
PMI21_ph = dados_ph['PMI-21']
PMI20_ph = dados_ph['PMI-20']
PMI15_ph = dados_ph['PMI-15']
PMI08_ph = dados_ph['PMI-08']

fig, ax = plt.subplots()

#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PMI02_ph, '.-', label='PMI-02')
ax.plot(PMI04_ph, '.-', label='PMI-04')
ax.plot(PMI21_ph, '.-', label='PMI-21')
ax.plot(PMI20_ph, '.-', label='PMI-20')
ax.plot(PMI15_ph, '.-', label='PMI-15')
ax.plot(PMI08_ph, '.-', label='PMI-08')
leg = ax.legend()

plt.legend(loc="best", ncol = 2) #expand stretches it along the bottom # while ncol specifies the number of columns
ax.set(xlabel='Ano', ylabel='pH')
ax.grid()

plt.savefig('Conjuntos_pH.png', bbox_inches='tight', dpi=300)

#Plota gráfico Conjuntos Multinivel - Alumínio

PP01S_al = dados_aluminio['PP-01S']
PP01R_al = dados_aluminio['PP-01R']
PP02S_al = dados_aluminio['PP-02S']
PP02R_al = dados_aluminio['PP-02R']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PP01S_al, '.-', label='PP-01S')
ax.plot(PP01R_al, '.-', label='PP-01R')
ax.plot(PP02S_al, '.-', label='PP-02S')
ax.plot(PP02R_al, '.-', label='PP-02R')
ax.set_yscale('log')
leg = ax.legend()

ax.set(xlabel='Ano', ylabel='Alumínio Total (mg/L)')
ax.grid()
plt.legend(loc="best", ncol = 2) #expand stretches it along the bottom # while ncol specifies the number of columns

plt.savefig('Multinivel_aluminio.png', bbox_inches='tight', dpi=300)

#Plota gráfico Conjuntos Multinivel - Ferro

PP01S_fe = dados_ferro['PP-01S']
PP01R_fe = dados_ferro['PP-01R']
PP02S_fe = dados_ferro['PP-02S']
PP02R_fe = dados_ferro['PP-02R']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PP01S_fe, '.-', label='PP-01S')
ax.plot(PP01R_fe, '.-', label='PP-01R')
ax.plot(PP02S_fe, '.-', label='PP-02S')
ax.plot(PP02R_fe, '.-', label='PP-02R')

leg = ax.legend()

ax.set(xlabel='Ano', ylabel='Ferro Total (mg/L)')
ax.grid()
plt.legend(loc="best", ncol = 2) #expand stretches it along the bottom # while ncol specifies the number of columns

plt.savefig('Multinivel_ferro.png', bbox_inches='tight', dpi=300)

#Plota gráfico Conjuntos Multinivel - Manganês

PP01S_mg = dados_manganes['PP-01S']
PP01R_mg = dados_manganes['PP-01R']
PP02S_mg = dados_manganes['PP-02S']
PP02R_mg = dados_manganes['PP-02R']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PP01S_mg, '.-', label='PP-01S')
ax.plot(PP01R_mg, '.-', label='PP-01R')
ax.plot(PP02S_mg, '.-', label='PP-02S')
ax.plot(PP02R_mg, '.-', label='PP-02R')

leg = ax.legend()

ax.set(xlabel='Ano', ylabel='Manganês Total (mg/L)')
ax.grid()
plt.legend(loc="best", ncol = 2) # while ncol specifies the number of columns

plt.savefig('Multinivel_manganes.png', bbox_inches='tight', dpi=300)

#Plota gráfico Conjuntos Multinivel - Acidez

PP01S_ac = dados_acidez['PP-01S']
PP01R_ac = dados_acidez['PP-01R']
PP02S_ac = dados_acidez['PP-02S']
PP02R_ac = dados_acidez['PP-02R']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PP01S_ac, '.-', label='PP-01S')
ax.plot(PP01R_ac, '.-', label='PP-01R')
ax.plot(PP02S_ac, '.-', label='PP-02S')
ax.plot(PP02R_ac, '.-', label='PP-02R')

leg = ax.legend()

ax.set(xlabel='Ano', ylabel='Acidez Total (mg/L)')
ax.grid()
plt.legend(loc="best", ncol = 2) # while ncol specifies the number of columns

plt.savefig('Multinivel_acidez.png', bbox_inches='tight', dpi=300)

#Plota gráfico Conjuntos Multinivel - Sulfato

PP01S_so = dados_sulfato['PP-01S']
PP01R_so = dados_sulfato['PP-01R']
PP02S_so = dados_sulfato['PP-02S']
PP02R_so = dados_sulfato['PP-02R']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PP01S_so, '.-', label='PP-01S')
ax.plot(PP01R_so, '.-', label='PP-01R')
ax.plot(PP02S_so, '.-', label='PP-02S')
ax.plot(PP02R_so, '.-', label='PP-02R')

leg = ax.legend()

ax.set(xlabel='Ano', ylabel='Sulfato Total (mg/L)')
ax.grid()
plt.legend(loc="upper right", ncol = 1) # while ncol specifies the number of columns

plt.savefig('Multinivel_sulfato.png', bbox_inches='tight', dpi=300)

#Plota gráfico Conjuntos Multinivel - pH

PP01S_ph = dados_ph['PP-01S']
PP01R_ph = dados_ph['PP-01R']
PP02S_ph = dados_ph['PP-02S']
PP02R_ph = dados_ph['PP-02R']

fig, ax = plt.subplots()
#ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%Y'))
ax.plot(PP01S_ph, '.-', label='PP-01S')
ax.plot(PP01R_ph, '.-', label='PP-01R')
ax.plot(PP02S_ph, '.-', label='PP-02S')
ax.plot(PP02R_ph, '.-', label='PP-02R')

leg = ax.legend()

ax.set(xlabel='Ano', ylabel='pH')
ax.grid()
plt.legend(loc="best", ncol = 2) # while ncol specifies the number of columns

plt.savefig('Multinivel_ph.png', bbox_inches='tight', dpi=300)

##TESTE MANN KENDALL

import pymannkendall as mk

#tendência pH - conjuntos

mk.original_test(dados_ph['PMI-02'])
mk.original_test(dados_ph['PMI-04'])
mk.original_test(dados_ph['PMI-08'])
mk.original_test(dados_ph['PMI-15'])
mk.original_test(dados_ph['PMI-20'])
mk.original_test(dados_ph['PMI-21'])

#tendência acidez - conjuntos

mk.original_test(dados_acidez['PMI-02'])
mk.original_test(dados_acidez['PMI-04'])
mk.original_test(dados_acidez['PMI-08'])
mk.original_test(dados_acidez['PMI-15'])
mk.original_test(dados_acidez['PMI-20'])
mk.original_test(dados_acidez['PMI-21'])


#tendência alumínio - conjuntos

mk.original_test(dados_aluminio['PMI-02'])
mk.original_test(dados_aluminio['PMI-04'])
mk.original_test(dados_aluminio['PMI-08'])
mk.original_test(dados_aluminio['PMI-15'])
mk.original_test(dados_aluminio['PMI-20'])
mk.original_test(dados_aluminio['PMI-21'])

#tendência ferro - conjuntos

mk.original_test(dados_ferro['PMI-02'])
mk.original_test(dados_ferro['PMI-04'])
mk.original_test(dados_ferro['PMI-08'])
mk.original_test(dados_ferro['PMI-15'])
mk.original_test(dados_ferro['PMI-20'])
mk.original_test(dados_ferro['PMI-21'])

#tendência ferro - conjuntos

mk.original_test(dados_manganes['PMI-02'])
mk.original_test(dados_manganes['PMI-04'])
mk.original_test(dados_manganes['PMI-08'])
mk.original_test(dados_manganes['PMI-15'])
mk.original_test(dados_manganes['PMI-20'])
mk.original_test(dados_manganes['PMI-21'])


#tendência sulfato - conjuntos

mk.original_test(dados_sulfato['PMI-02'])
mk.original_test(dados_sulfato['PMI-04'])
mk.original_test(dados_sulfato['PMI-08'])
mk.original_test(dados_sulfato['PMI-15'])
mk.original_test(dados_sulfato['PMI-20'])
mk.original_test(dados_sulfato['PMI-21'])

#   MULTINÍVEIS

#tendência pH - multiníveis

mk.original_test(dados_ph['PP-01S'])
mk.original_test(dados_ph['PP-01R'])
mk.original_test(dados_ph['PP-02S'])
mk.original_test(dados_ph['PP-02R'])


#tendência acidez - multiníveis

mk.original_test(dados_acidez['PP-01S'])
mk.original_test(dados_acidez['PP-01R'])
mk.original_test(dados_acidez['PP-02S'])
mk.original_test(dados_acidez['PP-02R'])

#tendência aluminio - multiníveis

mk.original_test(dados_aluminio['PP-01S'])
mk.original_test(dados_aluminio['PP-01R'])
mk.original_test(dados_aluminio['PP-02S'])
mk.original_test(dados_aluminio['PP-02R'])

#tendência  ferro - multiníveis

mk.original_test(dados_ferro['PP-01S'])
mk.original_test(dados_ferro['PP-01R'])
mk.original_test(dados_ferro['PP-02S'])
mk.original_test(dados_ferro['PP-02R'])
